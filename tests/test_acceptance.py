from __future__ import annotations

import json
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from route_research import installed_skills, route_case  # noqa: E402


class FunnelRoutingAcceptanceTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.available = installed_skills()
        cls.fixtures = ROOT / "tests" / "fixtures"

    def route(self, name: str) -> dict:
        case = json.loads((self.fixtures / name).read_text(encoding="utf-8"))
        return route_case(case, self.available)

    @staticmethod
    def names(result: dict) -> list[str]:
        return [item["skill_name"] for item in result["selected_skills"]]

    def test_vsl_mexico_uses_transcript_without_visual_tool(self) -> None:
        result = self.route("vsl_mexico.json")
        self.assertEqual(result["market_profile"], "es-MX")
        self.assertIn("vsl-script", self.names(result))
        self.assertNotIn("video-analysis", self.names(result))
        self.assertEqual(result["missing_evidence"], [])

    def test_plf_brazil_routes_launch_whatsapp_and_localization(self) -> None:
        result = self.route("plf_brazil.json")
        names = self.names(result)
        self.assertEqual(result["source_market"], "pt-BR")
        self.assertEqual(result["target_market"], "es-MX")
        self.assertIn("plf-walker", names)
        self.assertIn("sms", names)
        self.assertIn("translation", names)
        sms = next(item for item in result["selected_skills"] if item["skill_name"] == "sms")
        self.assertIn("chronological", sms["expected_output"])
        self.assertIn("original-language", result["localization_policy"])
        self.assertFalse(any(gap["channel"] == "whatsapp_history" for gap in result["missing_evidence"]))

    def test_inaccessible_video_is_non_blocking_and_marked_missing(self) -> None:
        result = self.route("inaccessible_video.json")
        self.assertIn("funnel-architecture", self.names(result))
        self.assertEqual([gap["channel"] for gap in result["missing_evidence"]], ["video"])

    def test_whatsapp_link_without_history_is_non_blocking(self) -> None:
        result = self.route("whatsapp_link.json")
        self.assertIn("funnel-architecture", self.names(result))
        self.assertEqual([gap["channel"] for gap in result["missing_evidence"]], ["whatsapp_history"])

    def test_absent_channels_do_not_create_noise(self) -> None:
        result = self.route("no_video_no_whatsapp.json")
        self.assertEqual(result["missing_evidence"], [])

    def test_ad_longevity_never_becomes_winner_claim(self) -> None:
        result = self.route("ad_longevity.json")
        self.assertIn("apify-ads-intelligence", self.names(result))
        warning = " ".join(result["warnings"]).lower()
        self.assertIn("not proof", warning)
        self.assertIn("roas", warning)

    def test_audit_without_revenue_marks_monetary_impact_unknown(self) -> None:
        result = self.route("audit_without_revenue.json")
        self.assertIn("funnel-audit", self.names(result))
        self.assertTrue(any("UNKNOWN" in warning for warning in result["warnings"]))

    def test_local_video_routes_visual_analysis(self) -> None:
        result = self.route("local_video_visuals.json")
        self.assertIn("video-analysis", self.names(result))
        self.assertIn("vsl-script", self.names(result))
        self.assertEqual(result["missing_evidence"], [])

    def test_simple_request_does_not_load_the_library(self) -> None:
        result = self.route("simple_landing.json")
        names = self.names(result)
        self.assertEqual(names, ["funnel-hacking-orchestrator", "cro", "copywriting", "funnel-audit"])
        self.assertLess(len(names), 10)


if __name__ == "__main__":
    unittest.main()
