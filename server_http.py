from http.server import BaseHTTPRequestHandler, HTTPServer
import time


class MyHttpServer(BaseHTTPRequestHandler):

    @staticmethod
    def middleware(func):
        def wrapper(self,*args, **kwargs):
            start = time.time()
            response = func(self, *args, **kwargs)
            print(f"Time taken {(time.time() - start)* 1000}* 10^-3 s")
            return response
        return wrapper

    @middleware
    def do_GET(self):
        match self.path:
            case "/query":
                self.send_response(200)
                self.send_header("Content-Type", "text/html")
                self.end_headers()
                self.wfile.write(b"<h1>Get query</h1>")
            case "/request":
                self.send_response(200)
                self.send_header("Content-Type", "text/html")
                self.end_headers()
                self.wfile.write(b"<h1>Get request</h1>")
            case _:
                self.send_response(404)
                self.send_header("Content-Type", "text/html")
                self.end_headers()
                self.wfile.write(b"<h1>Not found</h1>")
       


def run(server=HTTPServer, handler=MyHttpServer,port=8000):
    add = ('', port)
    httd = server(server_address=add,RequestHandlerClass=handler)
    print("Server running on 8000")
    httd.serve_forever()

if __name__ == "__main__":
    run()