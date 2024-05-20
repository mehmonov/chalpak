# Chalpak Web Framework

Chalpak is a simple and easy-to-use web framework that helps you create fast and efficient web applications.
[![Chalpak version](https://img.shields.io/pypi/v/chalpak.svg)](https://pypi.org/project/chalpak)
[![PyPI version](https://badge.fury.io/py/chalpak.svg)](https://badge.fury.io/py/chalpak)
[![Documentation Status](https://readthedocs.org/projects/chalpak/badge/?version=latest)](https://chalpak.readthedocs.io/en/latest/?badge=latest)



**Install Chalpak**

```bash
pip install chalpak
```

## Usage

```python
from chalpak import Chalpak

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

