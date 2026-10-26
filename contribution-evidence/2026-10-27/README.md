# Local bug reproduction evidence

Prepared by Codex (GPT-6), an AI agent, at the fork owner's request.

The screenshots show actual browser output from a locally served Panel app.
Before: unchanged upstream main dba1b46e6.
After: a local verification branch combining the three independent fixes.

- holoviz/panel#8919: distinct negative float arguments share a cached result.
- holoviz/panel#8920: circular list and dictionary inputs raise RecursionError.
- holoviz/panel#8921: FileDownload rejects os.DirEntry despite os.PathLike support in its annotation.

Run `panel serve demo.py` to reproduce the display. This script catches each error
so that all three results can be inspected on one page.

The three fix branches are based independently on upstream main; none contains the other fixes.
The combined cache and download regression suites passed: 115 tests.
The Python source was tested on Windows with Python 3.13.1, Bokeh 3.10.1,
and Param 2.5.0b3. Ruff, isort, codespell, and git diff --check passed.
Pixi was unavailable; an isolated uv environment used the declared dependencies.
For the browser smoke test, prebuilt Panel 1.10.0 frontend assets were used locally;
no TypeScript source was changed. A full frontend rebuild and full project test suite
were not run.

No human review or maintainer acceptance is implied by these automated checks.
