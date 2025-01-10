from chalpak.app import Chalpak

from chalpak.response import JSONResponse, HTMLResponse, render

app = Chalpak()



@app.get("/hello/{name}")
async def index(request, name):
    return JSONResponse({"name": name})

app.run()
