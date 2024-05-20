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
