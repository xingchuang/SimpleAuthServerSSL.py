#-*- coding:utf-8 -*-
import SimpleHTTPServer
class handler(SimpleHTTPServer.SimpleHTTPRequestHandler):
    def do_GET(self):
        if (self.path == '/auth-smtp'):
            # verify 'Auth-User', 'Auth-Pass', 'Client-IP'
            print self.headers.dict
            if self.headers.get('Auth-Protocol') == 'smtp' and  self.headers.get('Auth-User') == 'xiaoyu' and self.headers.get('Auth-Pass') == 'xiaoyu':
                self.send_response(200)
                self.send_header("Auth-Status", "OK");
                self.send_header("Auth-Server", "127.0.0.1");
                self.send_header("Auth-Port", "26");
                self.end_headers()
                return


addr = ('', 10025)
httpd = SimpleHTTPServer.BaseHTTPServer.HTTPServer(addr, handler)
httpd.serve_forever()
