# Source Manifest

Manifest de ingesta de la knowledge base de Funnel Hacking. Los IDs son estables y no implican que una afirmación sea verdadera: describen la procedencia del material suministrado por el usuario. Las etiquetas de evidencia caracterizan la fuente en conjunto; una afirmación concreta puede requerir una clasificación más estricta.

## Sources

| source_id | title | author / organization | year | language | source_type | evidence_level | temporal_sensitivity | original_file(s) | derived_md | processing_status | raw_source_removed |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SRC-001 | Scientific Advertising | Claude C. Hopkins | 1923 | English | book | principle_classic | evergreen | `db_funnelhacker/scientificadvertising-claudehopkins.pdf` | `sources/hopkins-scientific-advertising.md` | COMPLETE | yes |
| SRC-002 | Breakthrough Advertising | Eugene M. Schwartz | 1966; supplied Boardroom edition | English | book | principle_classic | evergreen | `db_funnelhacker/breakthroughadvertising-eugeneschwartz.pdf` | `sources/schwartz-breakthrough-advertising.md` | COMPLETE | yes |
| SRC-003 | Influence: The Psychology of Persuasion | Robert B. Cialdini | 2007 revision of 1984 work | English | research synthesis / book | research_backed | evergreen | `db_funnelhacker/influencepsychologypersuasion-robertcialdini.pdf` | `sources/cialdini-influence.md` | COMPLETE | yes |
| SRC-004 | How Brands Grow: What Marketers Don't Know | Byron Sharp | 2014 revised ebook; first published 2010 | English | research synthesis / book | research_backed | semi-evergreen | `db_funnelhacker/howbrandsgrow-byronsharp.pdf` | `sources/sharp-how-brands-grow.md` | COMPLETE | yes |
| SRC-005 | Obviously Awesome | April Dunford | 2019 | English | book | practitioner_framework | evergreen | `db_funnelhacker/obviouslyawesome-aprildunford.pdf` | `sources/dunford-obviously-awesome.md` | COMPLETE | yes |
| SRC-006 | DotCom Secrets | Russell Brunson | 2015 | English | book | practitioner_framework | semi-evergreen | `db_funnelhacker/dotcomsecrets-russelbranson.pdf` | `sources/brunson-dotcom-secrets.md` | COMPLETE | yes |
| SRC-007 | Launch | Jeff Walker | 2014 supplied edition | English | book | practitioner_framework | semi-evergreen | `db_funnelhacker/launch-jeffwalker.pdf` | `sources/walker-launch.md` | COMPLETE | yes |
| SRC-008 | $100M Offers | Alex Hormozi | 2021 | English | book | practitioner_framework | evergreen | `db_funnelhacker/100moffers-hormozi.pdf` | `sources/hormozi-100m-offers.md` | COMPLETE | yes |
| SRC-009 | $100M Leads | Alex Hormozi | 2023 | English | book | practitioner_framework | semi-evergreen | `db_funnelhacker/100mleads-hormozi.pdf` | `sources/hormozi-100m-leads.md` | COMPLETE | yes |
| SRC-010 | Master the Essentials of Conversion Optimization | Peep Laja / ConversionXL | 2014 | English | guide | research_backed + practitioner_framework | semi-evergreen | `db_funnelhacker/essentialsconversionoptimization-conversionxl.pdf` | `sources/laja-conversionxl-cro-guide.md` | COMPLETE | yes |
| SRC-011 | The Data-Driven Conversion Optimization Guide | Peep Laja / CXL | 2026 capture; core material overlaps 2014 guide | English | saved web-page collection | research_backed + practitioner_framework | time-sensitive capture; semi-evergreen method | `db_funnelhacker/conversionxl/*.jpeg` (12 files) | `sources/laja-conversionxl-cro-guide.md` | COMPLETE | yes |
| SRC-012 | Patented Heuristic / Conversion Sequence Heuristic | MECLABS Institute | undated page; 2026 ingestion note | Spanish note from English web source | saved web-page note | research_backed + practitioner_framework | semi-evergreen | `db_funnelhacker/converted.md` | `sources/meclabs-conversion-sequence-heuristic.md` | COMPLETE | yes |

## Duplicate and edition assessment

- No byte-identical files were detected in the supplied corpus.
- `SRC-010` and `SRC-011` are distinct versions of substantially overlapping CXL material. The PDF is a 2014 guide; the JPEG collection is a 2026 capture of the web presentation. They intentionally share one derived note, which records both provenances and separates durable method from dated interface/tool references.
- The 13 JPEGs under `db_funnelhacker/conversionxl/` are pages/sections of one captured web guide, not 13 independent sources.
- The supplied `Breakthrough Advertising` file identifies the original 1966 work and includes Boardroom-edition front matter; the exact digital-file release date is not treated as the work's publication year.
- `Scientific Advertising` is a scan of the 1923 work. Its PDF metadata reflects later file processing and is not publication metadata.

## Processing states

- `INVENTORIED`: identified and integrity-checked; no deletion is allowed.
- `IN_PROGRESS`: a derived note exists but has not passed all validation gates.
- `COMPLETE`: derived knowledge, attribution, routing, originality, secret scan, and manifest checks passed; raw removal is allowed.
- `NEEDS_REVIEW`: validation failed or provenance/content is too uncertain; retain the raw source.

## Completion validation

Each row below was checked before raw removal. `PASS` means: the derived note exists; attribution/edition is documented; principal operational concepts are represented; the note is synthetic rather than a substitute for the source; the source is in this manifest; the INDEX routes to it where relevant; and the note passed the repository secret scan.

| source_id | derived_exists | attribution | core_coverage | non_substitutive | indexed | secret_scan |
| --- | --- | --- | --- | --- | --- | --- |
| SRC-001 | PASS | PASS | PASS | PASS | PASS | PASS |
| SRC-002 | PASS | PASS | PASS | PASS | PASS | PASS |
| SRC-003 | PASS | PASS | PASS | PASS | PASS | PASS |
| SRC-004 | PASS | PASS | PASS | PASS | PASS | PASS |
| SRC-005 | PASS | PASS | PASS | PASS | PASS | PASS |
| SRC-006 | PASS | PASS | PASS | PASS | PASS | PASS |
| SRC-007 | PASS | PASS | PASS | PASS | PASS | PASS |
| SRC-008 | PASS | PASS | PASS | PASS | PASS | PASS |
| SRC-009 | PASS | PASS | PASS | PASS | PASS | PASS |
| SRC-010 | PASS | PASS | PASS | PASS | PASS | PASS |
| SRC-011 | PASS | PASS | PASS | PASS | PASS | PASS |
| SRC-012 | PASS | PASS | PASS | PASS | PASS | PASS |
