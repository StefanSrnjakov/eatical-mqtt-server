from http.server import BaseHTTPRequestHandler, HTTPServer
import recognition
class RequestHandler(BaseHTTPRequestHandler):
    def _send_response(self, message):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(message.encode())

    # http://localhost:8000?topic=[food|restaurant|menu]1&imgFile=imgFilename
    def do_GET(self):
        path, _, query_string = self.path.partition("?")
        if query_string == '':
            self._send_response("")
            return

        query_params = {}
        for qp in query_string.split("&"):
            keyValue = qp.split("=")
            query_params[keyValue[0]] = keyValue[1]

        topic = query_params["topic"]
        imgFileName = query_params["imgFile"]

        recognitionObj = {}
        try:
            if topic == "food":
                recognitionObj = recognition.food_recognition(imgFileName)
            if topic == "restaurant":
                recognitionObj = recognition.restaurant_recognition(imgFileName)
            if topic == "menu":
                recognitionObj = recognition.menu_recognition(imgFileName)
        except Exception as message:
            recognitionObj = {"status": False, "message": message}
        self._send_response(format(recognitionObj))

def run(server_class=HTTPServer, handler_class=RequestHandler, port=8000):
    server_address = ("", port)
    httpd = server_class(server_address, handler_class)
    print("Starting httpd on port {}".format(port))
    httpd.serve_forever()

if __name__ == '__main__':
    run()
    pass
