# Chalpak Web Framework

Chalpak is a simple and easy-to-use web framework that helps you create fast and efficient web applications

[![Chalpak version](https://img.shields.io/pypi/v/chalpak.svg)](https://pypi.org/project/chalpak)
[![PyPI version](https://badge.fury.io/py/chalpak.svg)](https://badge.fury.io/py/chalpak)
[![Documentation Status](https://badgen.net/badge/Docs/1.0.0?icon=book)](https://chalpak.versel.app/)

## Inspiration
The construction site began to write first class codes for me. I searched on Jan 4, I looked for a lot, it is very difficult to build the building. [Alcazar](https://github.com/rahmonov/alcazar) seemed very interesting to me. Thanks to [Jahongir Rakhmonov](https://github.com/rahmonov) you are most useful to me

**Install Chalpak**

```bash
pip install chalpak
```

## Usage

```python
from chalpak.app import ChalpakApp

app = Chalpak()


app.run()

```

## Examples

```python
from chalpak.app import ChalpakApp

from chalpak.response import JSONResponse, HTMLResponse, render

app = ChalpakApp(templates='templates')

@app.get("/salom/{name}")
async def index(request, name):
    return JSONResponse({"name": name})

@app.get("/html/{name}")
async def html(request, name):
    return render("index.html", request, {"name": name})

app.run()
```

## Run

```bash
jurigged -v script.py
```

