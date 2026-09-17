# Installing in Hermes Agent

This repository already uses Hermes' standard tap layout: each skill is under `skills/<slug>/SKILL.md`, and its support directories travel with it.

## Recommended: publish and install as a tap

Push this repository to a GitHub repository, replacing `<OWNER>/<REPO>` below with its real slug:

```powershell
hermes skills tap add <OWNER>/<REPO>
hermes skills search funnel-hacking
hermes skills inspect <OWNER>/<REPO>/funnel-hacking-orchestrator
hermes skills install <OWNER>/<REPO>/funnel-hacking-orchestrator
```

Install only the specialists a team wants available. Examples:

```powershell
hermes skills install <OWNER>/<REPO>/funnel-architecture
hermes skills install <OWNER>/<REPO>/funnel-audit
hermes skills install <OWNER>/<REPO>/translation
hermes skills install <OWNER>/<REPO>/plf-walker
hermes skills install <OWNER>/<REPO>/video-analysis
```

This tap publishes its evidence-first creative variant as `funnel-ad-creative`. If the canonical `ad-creative` from `coreyhaines31/marketingskills` is already installed, it may remain in place; install `funnel-ad-creative` only when this repository's evidence rules and self-contained Hermes references are required. The distinct name avoids a same-name/source-category collision without modifying or removing the preexisting skill.

Install `rmbc-context` alongside any DTC/RMBC specialist whose registry entry lists it as a dependency:

```powershell
hermes skills install <OWNER>/<REPO>/rmbc-context
hermes skills install <OWNER>/<REPO>/funnel-audit
```

Hermes downloads each skill's referenced `references/`, `templates/`, `scripts/`, and `assets/` alongside `SKILL.md`. The orchestrator consults this repository's central registry when used from a checkout; for isolated Hub installation it also contains a fallback routing map, so routing remains usable.

List and audit installed community skills:

```powershell
hermes skills list --source hub
hermes skills audit
hermes skills check
```

Hermes applies a security scan to community taps. Review findings rather than automatically using `--force`; dangerous verdicts cannot be overridden.

## Install one skill directly

A public GitHub repository can also provide a single skill without first adding the tap:

```powershell
hermes skills install <OWNER>/<REPO>/skills/funnel-hacking-orchestrator
```

## Development checkout

Before publishing or installing, validate locally:

```powershell
python scripts/build_catalog.py --check
python scripts/validate_skills.py --verbose
python -m unittest discover -s tests -v
```

This repository deliberately does not copy files into `$HERMES_HOME`, `%LOCALAPPDATA%`, or a home directory. Installation is an explicit user action through Hermes.

## Optional runtime setup

### Apify

Set `APIFY_TOKEN` privately only if public-ad collection is needed. Start from `.env.example`; do not commit `.env`.

### Video analysis

Run the diagnostic on the target machine:

```powershell
python skills/video-analysis/scripts/doctor.py --profile base --repair-plan --format markdown
```

The full profile additionally checks downloader, OCR, and local ASR dependencies:

```powershell
python skills/video-analysis/scripts/doctor.py --profile full --repair-plan --format markdown
```

A transcript is sufficient for spoken-message analysis. Missing optional video dependencies must not block the rest of a funnel investigation.

## Official reference

Hermes' current Skills System documentation defines custom taps, direct GitHub identifiers, the security scan, support-directory downloads, and the standard `skills/<skill>/SKILL.md` layout: <https://github.com/NousResearch/hermes-agent/blob/main/website/docs/user-guide/features/skills.md>.
