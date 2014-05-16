# -*- coding: utf-8 -*-

default_application = 'midiacapoeira'
applications = 'midiacapoeira, admin'

default_language = 'pt-br'
languages = 'pt-br'

routes_in = (
	('/', '/default/index'),
	('/chat/', '/default/chat'),
	('/sobre/', '/sobre/index'),
	('/conteudo/', '/conteudo/index'),
	('/editoriais/', '/editoriais/index'),
)

routes_out = (
	('/default/index', '/'),
	('/default/chat', '/chat/'),
	('/sobre/index', '/sobre/'),
	('/conteudo/index', '/conteudo/'),
	('/editoriais/index', '/editoriais/'),
)

