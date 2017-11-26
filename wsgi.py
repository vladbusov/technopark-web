from pprint import pformat
from html import escape
from urllib.parse import parse_qsl


def getPost(environ, start_response):
    output = ["<h1>Hello, world!</h1>"]

    d = parse_qsl(environ['QUERY_STRING'])
    if environ['REQUEST_METHOD'] == 'POST':
        output.append('<h1>Post  data:</h1>')
        output.append(pformat(environ['wsgi.input'].read().decode()))

    if environ['REQUEST_METHOD'] == 'GET':
        if environ['QUERY_STRING'] != '':
            output.append('<h1>Get data:</h1>')
            for ch in d:
                output.append(' = '.join(ch))
                output.append('<br>')

    output_len = sum(len(line) for line in output)
    start_response('200 OK', [('Content-type', 'text/html'),
                              ('Content-Length', str(output_len))])
    string_output = "".join(output)
    byte_output = string_output.encode('utf-8')
    return [byte_output]