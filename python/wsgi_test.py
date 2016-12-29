# WSGI test 
from wsgiref.simple_server import make_server

def application(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/html')])
    return [b'<h1>Hello, Web!<h1>']

def application_new(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/html')])
    body = '<h1>Hello, %s!</h1>' % (environ['PATH_INFO'][1:] or 'web')
    return [body.encode('utf-8')]


# Create Server
httpd = make_server('127.0.0.1', 8070, application_new)
print('Serving HTTP on port 8070...')
httpd.serve_forever()

