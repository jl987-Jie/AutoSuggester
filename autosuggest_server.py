import cherrypy
from autosuggest import AutoSuggestEngine

if __name__ == '__main__':
	cherrypy.tree.mount(
		AutoSuggestEngine(), '/api/autosuggest',
		{'/':
			{'request.dispatch': cherrypy.dispatch.MethodDispatcher()}
		}
	)
	cherrypy.engine.start()
	cherrypy.engine.block()