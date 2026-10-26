import os
from pathlib import Path

import panel as pn

pn.extension()


@pn.cache
def identity(value):
    return value


@pn.cache
def size(value):
    return len(value)


def check(title, expected, callback):
    try:
        actual = callback()
        status = 'PASS' if actual == expected else 'FAIL'
    except Exception as error:
        actual = f'{type(error).__name__}: {error}'
        status = 'FAIL'
    return pn.pane.Markdown(
        f'## {title}\n**{status}**\n\nExpected: `{expected}`\n\nObserved: `{actual}`',
        width=800,
    )


values = [1]
values.append(values)
sample_dir = Path(__file__).parent / 'sample'
sample_dir.mkdir(exist_ok=True)
(sample_dir / 'report.txt').write_text('data', encoding='utf-8')


def download_data():
    with os.scandir(sample_dir) as entries:
        return pn.widgets.FileDownload(next(entries), embed=True).data


pn.Column(
    '# Panel local bug reproductions',
    f'Source checkout: `{pn.__version__}`',
    check('1. Distinct negative floats in pn.cache', [-1.0, -2.0], lambda: [identity(-1.0), identity(-2.0)]),
    check('2. Circular list in pn.cache', 2, lambda: size(values)),
    check('3. FileDownload with os.DirEntry', 'data:text/plain;charset=UTF-8;base64,ZGF0YQ==', download_data),
    width=900,
).servable()
