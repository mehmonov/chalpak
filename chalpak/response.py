import json
from aiohttp.web_fileresponse import FileResponse as _FileResponse
from aiohttp.web_response import Response as _Response
import aiohttp_jinja2
from aiohttp.web import Request

def render(template_name: str, request: Request, context: dict):
    return aiohttp_jinja2.render_template(template_name, request, context)

class Response:
    def __init__(self, content: str, status_code: int = 200, content_type: str = 'text/html', headers: dict = None):
        self.content = content
        self.status_code = status_code
        self.content_type = content_type
        self.headers = headers

    @property
    def __response__(self):
        return _Response(text=self.content, status=self.status_code, content_type=self.content_type,
                         headers=self.headers)

class HTMLResponse(Response):
    def __init__(self, html_content: str, status_code: int = 200, headers: dict = None):
        super().__init__(content=html_content, status_code=status_code, content_type='text/html',
                         headers=headers)

class JSONResponse(Response):
    def __init__(self, json_content: dict, status_code: int = 200, headers: dict = None):
        super().__init__(content=json.dumps(json_content), status_code=status_code, content_type='application/json', headers=headers)

class FileResponse(_FileResponse):
    def __init__(self, path: str, status_code: int = 200, headers: dict = None):
        super().__init__(path, status_code=status_code, headers=headers)
