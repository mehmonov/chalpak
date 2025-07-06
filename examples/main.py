from chalpak.app import Chalpak
from chalpak.response import JSONResponse

app = Chalpak()

@app.get("/")
async def home(request):
    return JSONResponse({"message": "Hello from Chalpak!"})

@app.get("/hello/{name}")
async def hello_name(request, name: str):
    return JSONResponse({"message": f"Hello, {name}!"})

if __name__ == "__main__":
    app.run()
