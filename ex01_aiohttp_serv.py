from aiohttp import web


async def index(request: web.Request):
    print(request.query_string)
    body = None
    with open("index.html") as f:
        body = f.read()
        
    return web.Response(
        body=body, 
        status=200,
        content_type="text/html")


async def hello(request):
    return web.Response(
        body="<h2>Hello from hello</h2>", 
        status=200)


if __name__ == "__main__":
    app = web.Application()
    app.add_routes([web.get("/", index), web.get("/hello", hello)])
    
    web.run_app(app, host="localhost", port=7070)