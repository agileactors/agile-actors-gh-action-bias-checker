# Gender Bias Scanner Action

<p align="center">
  <img src="./assets/logo.png" alt="Gender Bias Scanner Action logo" width="490"/>
</p>

A **GitHub Action** that scans your codebase for predefined “gender-biased” terms (e.g., `fireman`, `chairman`, etc.) and fails the run if any are found.

It is powered by lightweight embeddings and bias scoring modules (`embeddings.py`, `gender_axis.py`, `scoring.py`) that classify terms based on a configurable gender axis.

---

## Example

If any biased term appears, the Action will fail and produce a report:

```
🚨 Gender-biased terms detected (2 total):
src/utils/fire_utils.py:42:fireman
docs/architecture.md:10:chairman
```

If no biased terms are found:

```
✅ No gender-biased terms detected.
```

---

## Quick start

Create `.github/workflows/gender-bias-scan.yml`:

```yaml
name: Gender Bias Scan
on:
  pull_request:
  push:
    branches: [ main ]

jobs:
  scan:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - name: Run Gender Bias Scanner
        uses: agileactors/gender-bias-scanner-action@v1
        with:
          scan_paths: "src/**/*.py;docs/**/*.md"
          additional_terms: '["hostess","stewardess"]'
```

---

## Inputs

From [`action.yml`](./action.yml):

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `scan_paths` | string | `**/*.{py,js,ts,jsx,tsx,java,go,rb,cs,cpp,c,h,html,css,md}` | A semicolon-separated list of glob patterns to scan (e.g. `src/**/*.py;docs/**/*.md`). |
| `additional_terms` | JSON array | `[]` | Extra biased terms to check in addition to the built-in list (`terms.json`). Example: `'["hostess","stewardess"]'` |

---

## Outputs

| Name | Type | Description |
|------|------|-------------|
| `found` | string (`"true"` or `"false"`) | Whether any biased terms were detected. |
| `report` | string | Multi-line report listing matches in the format `filepath:line:matched_term`. |

Usage in later steps:

```yaml
- name: Print report
  if: always()
  run: echo "${{ steps.scan.outputs.report }}"

- name: Upload report
  if: always()
  uses: actions/upload-artifact@v4
  with:
    name: gender-bias-report
    path: bias-report.txt
```

---

## Behavior & exit codes

- **0** — No biased terms detected.  
- **1** — One or more biased terms found; report generated.  
- **2** — Misconfiguration (invalid glob, unreadable terms list, etc.).  

---

## Advanced configuration

### Add custom terms

```yaml
with:
  additional_terms: '["policeman","salesman"]'
```

### Restrict scanning

```yaml
with:
  scan_paths: "src/**/*.{ts,tsx};docs/**/*.md"
```

---

## How it works

- `scanner.py` handles traversal of files based on `scan_paths`.  
- `utils.py` provides file parsing and normalization.  
- `embeddings.py` + `gender_axis.py` create a bias detection model using word embeddings.  
- `scoring.py` computes bias scores and flags terms above threshold.  
- `main.py` wires it all together as the Docker entrypoint.

---
---

## Contributing

We ❤️ contributions! Whether it’s fixing a bug, improving documentation, or suggesting new features, your input helps make this project better for everyone.

---

## License

This project is licensed under the [MIT License](LICENSE).

You are free to use, modify, and distribute this software in both personal and commercial projects, provided that you include the original license notice.
