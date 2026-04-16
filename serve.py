import http.server, os
os.chdir('/Users/nachomz/Desktop/SolitareIgna')
http.server.test(HandlerClass=http.server.SimpleHTTPRequestHandler, port=8765, bind='127.0.0.1')
