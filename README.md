# Gender Bias Scanner Action

 A GitHub Action that scans your codebase for predefined “gender-biased” terms (e.g. `fireman`, `chairman`, etc.) and fails the run if any are found.

If any biased term appears, the Action will fail and produce a report:


> 🚨 Gender-biased terms detected (2 total):
>
> src/utils/fire_utils.py:42:fireman
>
> docs/architecture.md:10:chairman

On the other hand, if no biased terms are found, the Action will pass with a success
> ✅ No gender-biased terms detected.

## Inputs
- `bias_cutoff` (optional)
A float between 0.0 and 1.0 representing the minimum confidence threshold for flagging a term.
- `scan_paths` (optional)
A semicolon-separated list of file globs to scan.

Defaults to: `**/*.{py,js,ts,jsx,tsx,java,go,rb,cs,cpp,c,h,html,css,md}`

