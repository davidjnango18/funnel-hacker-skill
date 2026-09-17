# Source Intake

## Goal

Build an evidence manifest before analysis without turning intake into a blocker. Work with what exists, discover reasonable public surfaces, and record gaps after useful work begins.

## Accepted Inputs

- URLs, redirects, landing pages, sales pages, checkout pages, registration pages, forms, payment pages
- ad-library links, ad exports, screenshots, creative files, tracking/UTM observations
- transcripts, subtitles, MP4, audio, webinar/VSL replays
- PDFs, documents, CSV, email exports, researcher notes
- WhatsApp TXT/ZIP exports and detected group/channel links

## Intake Record

Create one row per source:

```yaml
source_id: SRC-001
type: meta_ad
source: https://example.test/ad
market: BR
language: pt-BR
captured_at: 2026-09-15T12:00:00-06:00
evidence_class: OBSERVED
access: public
status: captured
hash_or_version: optional
notes: "Creative and copy visible; performance data unavailable."
```

Use ISO 8601 timestamps. Preserve the initial and final URL when redirects occur. For user files, record the original filename, file type, and whether the file was modified for analysis.

## First-Pass Inventory

1. Record the target brand/product, countries, languages, and research question.
2. Register supplied assets before browsing.
3. Identify public surfaces that are proportionate to the request.
4. Deduplicate sources without deleting distinct versions, locales, dates, or creatives.
5. Record access limits, login walls, unavailable media, and ambiguous ownership.
6. Start analysis with the strongest available evidence.

## Web and Landing Capture

When reasonably observable, record:

- initial/final URL and redirects;
- headline, subheadline, offer, CTA, price, guarantee, proof, testimonials, urgency;
- forms, buttons, outbound links, payment provider, next step;
- visible upsells/order bumps and locale variants;
- observable UTMs or tracking parameters when relevant;
- embedded videos or WhatsApp links without claiming their unseen contents.

Do not replicate the website code. Capture what helps reconstruct the journey.

## Ads Intake

For each ad, attempt to record advertiser, platform, creative type, visible copy, headline, CTA, observable dates, destination, angle, hook, promise, awareness stage, and visual pattern.

Dates active or `daysRunning` are observations. They do not prove performance. Public library absence is not proof that no ads ran.

## Video Cases

- Transcript only: sufficient for spoken copy; visual fields remain `MISSING` or `NOT ASSESSED`.
- Local video: use `video-analysis` only when visual inspection changes the answer.
- Embedded but inaccessible: record one missing-evidence item and continue.
- No detected video: create no warning.

## WhatsApp Cases

- Export present: preserve chronology, timezone uncertainty, sender labels, edits/deletions when visible, links, CTAs, frequency, reminders, proof, objections, open/close cadence.
- Link without export: record one missing-evidence item and continue.
- No detected WhatsApp: create no warning.

## Missing Evidence Report

Separate:

- **Available evidence:** actually analyzed.
- **Missing evidence:** detected or strongly indicated but inaccessible.
- **Recommended additions:** optional assets likely to change or strengthen conclusions.

Do not list every imaginable artifact. Recommend only material additions.

