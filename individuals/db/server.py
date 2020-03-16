from http.server import HTTPServer, CGIHTTPRequestHandler

serverAddress = ('', 9000)
server = HTTPServer(serverAddress, CGIHTTPRequestHandler)
server.serve_forever()