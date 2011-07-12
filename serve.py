"""Simple web server for Android that takes a picture on a GET request.

It uses the Scripting Layer for Android.
http://code.google.com/p/android-scripting/
"""
import BaseHTTPServer, android
from os import path

droid = android.Android()
FILENAME = "/sdcard/sl4a/spy/pic.jpg"
PORT = 9090

class Handler(BaseHTTPServer.BaseHTTPRequestHandler):
    def do_GET(s):
        """Respond to a GET request."""
        droid.cameraCapturePicture(FILENAME)
        picture = open(FILENAME, 'rb')
        s.send_response(200)
        s.send_header("Content-Type", "image/jpeg")
        s.end_headers()
        s.wfile.write(picture.read())

server_class = BaseHTTPServer.HTTPServer
httpd = server_class(('', PORT), Handler)
httpd.serve_forever()
