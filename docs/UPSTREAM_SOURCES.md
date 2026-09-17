# Upstream Sources

All sources are pinned in `config/upstreams.yaml`. A commit changes only after the new tree, license, skill count, local transformations, and tests have been reviewed.

| Source | Pinned commit | Selection | License |
| --- | --- | --- | --- |
| [coleschaffer/dtc-copywriting-skills](https://github.com/coleschaffer/dtc-copywriting-skills) | `57cd5a77b8bf0c60b3e565f20d2c306d5803e65d` | All 44 skills | MIT |
| [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) | `5b2c0007766c6a1cf1d53fd8fc73e979e0821022` | All 50 skills and referenced tool guides | MIT |
| [qwwiwi/plf-walker](https://github.com/qwwiwi/plf-walker) | `51f064381d02b1ac1161a3b1ccc5b71af1e082d5` | `plf-walker` plus support files | MIT |
| [kostja94/marketing-skills](https://github.com/kostja94/marketing-skills) | `70987bad4ebe9dce1f74858c1c64f3f8810f18e4` | `translation` only | MIT |
| [apify/awesome-skills](https://github.com/apify/awesome-skills) | `c4a23629e6c2ba042853840163f5a88cc371e154` | `apify-ads-intelligence` only | Apache-2.0 |
| [bydfi-official/video-analysis-skill](https://github.com/bydfi-official/video-analysis-skill) | `b2702695f6fdb50457c30e6483af4f4d6240afa7` | `video-analysis` plus support files | MIT |

## Reproducible selection

`scripts/sync_upstreams.py` contains the source URLs, pinned commits, selected paths, and transformations. Its default mode clones into a temporary directory and reports the plan without modifying vendored content. `--apply` is required to change files.

The script copies files; it does not import or execute code from the fetched repositories. Maintainers must inspect license or structural changes before applying a new pin.

## Integrity expectations

- Six exact 40-character commit SHAs must be present.
- Every imported skill must appear in the registry.
- No two imported skills may share a frontmatter name.
- Selective sources must not bring unrelated skills.
- Upstream license text must remain in `licenses/`.
- Intentional changes must be repeatable in the sync script and described in `docs/PATCHES.md`.
