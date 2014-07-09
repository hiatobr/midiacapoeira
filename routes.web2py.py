# -*- coding: utf-8 -*-
# Este arquivo deve ser movido para a base da instalação web2py
# Copiar: `cp routes.web2py.py ../../routes.py`
# Ou link simbólico: `cd ../.. && ln -s applications/midiacapoeira.in/routes.web2py.py routes.py`

routers = dict(
	BASE=dict(
		default_application='midiacapoeira',
	),
)

routes_in = (
	('/admin/$anything', '/admin/$anything'),
	('/static/$anything', '/midiacapoeira/static/$anything'),
	('/appadmin/$anything', '/midiacapoeira/appadmin/$anything'),
	('/favicon.ico', '/midiacapoeira/static/favicon.ico'),
	('/robots.txt', '/midiacapoeira/static/robots.txt'),
)

routes_out = [(x, y) for (y, x) in routes_in[:-2]]

def __routes_doctest():
	'''
	Dummy function for doctesting routes.py.

	Use filter_url() to test incoming or outgoing routes;
	filter_err() for error redirection.

	filter_url() accepts overrides for method and remote host:
		filter_url(url, method='get', remote='0.0.0.0', out=False)

	filter_err() accepts overrides for application and ticket:
		filter_err(status, application='app', ticket='tkt')

	>>> import os
	>>> import gluon.main
	>>> from gluon.rewrite import regex_select, load, filter_url, regex_filter_out, filter_err, compile_regex
	>>> regex_select()
	>>> load(routes=os.path.basename(__file__))

	>>> os.path.relpath(filter_url('http://domain.com/favicon.ico'))
	'applications/examples/static/favicon.ico'
	>>> os.path.relpath(filter_url('http://domain.com/robots.txt'))
	'applications/examples/static/robots.txt'
	>>> filter_url('http://domain.com')
	'/init/default/index'
	>>> filter_url('http://domain.com/')
	'/init/default/index'
	>>> filter_url('http://domain.com/init/default/fcn')
	'/init/default/fcn'
	>>> filter_url('http://domain.com/init/default/fcn/')
	'/init/default/fcn'
	>>> filter_url('http://domain.com/app/ctr/fcn')
	'/app/ctr/fcn'
	>>> filter_url('http://domain.com/app/ctr/fcn/arg1')
	"/app/ctr/fcn ['arg1']"
	>>> filter_url('http://domain.com/app/ctr/fcn/arg1/')
	"/app/ctr/fcn ['arg1']"
	>>> filter_url('http://domain.com/app/ctr/fcn/arg1//')
	"/app/ctr/fcn ['arg1', '']"
	>>> filter_url('http://domain.com/app/ctr/fcn//arg1')
	"/app/ctr/fcn ['', 'arg1']"
	>>> filter_url('HTTP://DOMAIN.COM/app/ctr/fcn')
	'/app/ctr/fcn'
	>>> filter_url('http://domain.com/app/ctr/fcn?query')
	'/app/ctr/fcn ?query'
	>>> filter_url('http://otherdomain.com/fcn')
	'/app/ctr/fcn'
	>>> regex_filter_out('/app/ctr/fcn')
	'/ctr/fcn'
	>>> filter_url('https://otherdomain.com/app/ctr/fcn', out=True)
	'/ctr/fcn'
	>>> filter_url('https://otherdomain.com/app/ctr/fcn/arg1//', out=True)
	'/ctr/fcn/arg1//'
	>>> filter_url('http://otherdomain.com/app/ctr/fcn', out=True)
	'/fcn'
	>>> filter_url('http://otherdomain.com/app/ctr/fcn?query', out=True)
	'/fcn?query'
	>>> filter_url('http://otherdomain.com/app/ctr/fcn#anchor', out=True)
	'/fcn#anchor'
	>>> filter_err(200)
	200
	>>> filter_err(399)
	399
	>>> filter_err(400)
	400
	>>> filter_url('http://domain.com/welcome', app=True)
	'welcome'
	>>> filter_url('http://domain.com/', app=True)
	'myapp'
	>>> filter_url('http://domain.com', app=True)
	'myapp'
	>>> compile_regex('.*http://otherdomain.com.* (?P<any>.*)', '/app/ctr\g<any>')[0].pattern
	'^.*http://otherdomain.com.* (?P<any>.*)$'
	>>> compile_regex('.*http://otherdomain.com.* (?P<any>.*)', '/app/ctr\g<any>')[1]
	'/app/ctr\\\\g<any>'
	>>> compile_regex('/$c/$f', '/init/$c/$f')[0].pattern
	'^.*?:https?://[^:/]+:[a-z]+ /(?P<c>\\\\w+)/(?P<f>\\\\w+)$'
	>>> compile_regex('/$c/$f', '/init/$c/$f')[1]
	'/init/\\\\g<c>/\\\\g<f>'
	'''
	pass

if __name__ == '__main__':
	import doctest
	doctest.testmod()

