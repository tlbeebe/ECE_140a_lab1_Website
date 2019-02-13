from wsgiref.simple_server import make_server # the wsgiref webserver (default with Python)
from pyramid.config import Configurator

from pyramid.response import Response
from pyramid.response import FileResponse
from pyramid.renderers import render_to_response

''' Routes '''
def basic_route(req):
  return FileResponse('Homepage.html')

def view_route(req):
  return FileResponse('dht22.html') #We make one page per sensor, so we can place both temp and humidity here

def view_route(req):
    return FileResponse('lightSensor.html')

def view_route(req):
    return FileResponse('soundSensor.html')


''' Main Application '''
def main() :
  with Configurator() as config:

    # basic_route
    config.add_route('template_route', '/')
    config.add_view(basic_route, route_name='template_route')

    # view_route
    config.add_route('codepen_example', '/codepen')
    config.add_view(view_route, route_name='codepen_example')

    # for template_route / template_route2
    config.include('pyramid_jinja2')
    config.add_jinja2_renderer('.html')

    config.add_route('DHT22', '/DHT22')
    config.add_view(basic_route, route_name='DHT22')

    config.add_route('lightSensor', '/lightSensor')
    config.add_view(basic_route, route_name='lightSensor')

    config.add_route('soundSensor', '/soundSensor')
    config.add_view(basic_route, route_name='soundSensor')

    # add static folder to search path
    config.add_static_view(name='/', path='./public', cache_max_age=3600) #Change file location

    # create the webserver config
    app = config.make_wsgi_app()

  # run the server
  server = make_server('127.0.0.1', 8080, app)
  print("The server is now running on: http://127.0.0.1:8080")

  try:
    server.serve_forever()
  except KeyboardInterrupt:
    print("\nExiting...")
    exit(0)

if __name__ == '__main__':
  main()
