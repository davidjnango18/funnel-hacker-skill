---
name: rmbc-upgrade
description: Review and refresh the vendored RMBC skills through this repository's audited upstream sync workflow. Use when asked to update the imported DTC skill snapshot.
user-invocable: true
---

# RMBC Skills Upgrade

Use the repository-level `scripts/sync_upstreams.py` workflow. Do not self-update from a user home directory, run upstream installers, or modify global skill directories.

1. Read `docs/UPSTREAM_SOURCES.md` and `docs/PATCHES.md`.
2. Clone the approved upstreams into a temporary directory without running their scripts.
3. Review the new commits, licenses, changed `SKILL.md` files, relative dependencies, and executable changes.
4. Run `python scripts/sync_upstreams.py --from-dir <INSPECTED_CLONES> --apply`.
5. Run `python scripts/build_catalog.py` and `python scripts/validate_skills.py`.
6. Review and commit the resulting vendor diff, including the updated provenance commit.
