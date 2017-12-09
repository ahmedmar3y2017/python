import cherrypy
	  
class HelloWorld(object):
    # Index Url 
    def index(self):
        return "Hello World!"
    index.exposed = True
    #  This is url
    def regex(self):
        return "regex ya man "
    regex.exposed = True



cherrypy.quickstart(HelloWorld())