import cherrypy
import os.path
import wsgiref.handlers

class Index(object):
    @cherrypy.expose
    def index(self):
        return open('index.html')

class Products(object):
    @cherrypy.expose
    def index(self):
        return open('product.html')

class Services(object):
    @cherrypy.expose
    def index(self):
        return open('services.html')

class Contact(object):
    @cherrypy.expose
    def index(self):
        return open('contact.html')

if __name__=='__main__':
    root = Index()
    root.products = Products()
    root.services = Services()
    root.contact = Contact()

    current_dir = os.path.dirname(os.path.abspath(__file__))
    conf = {
        '/images': {'tools.staticdir.on': True, 'tools.staticdir.dir': os.path.join(current_dir, 'images')},
        '/css': {'tools.staticdir.on': True, 'tools.staticdir.dir': os.path.join(current_dir, 'css')},
        '/fonts': {'tools.staticdir.on': True, 'tools.staticdir.dir': os.path.join(current_dir, 'fonts')},
        '/js': {'tools.staticdir.on': True, 'tools.staticdir.dir': os.path.join(current_dir, 'js')}
        }

    cherrypy.quickstart(root, '/', config=conf)