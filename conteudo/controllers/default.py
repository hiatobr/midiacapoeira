# -*- coding: utf-8 -*-
# this file is released under public domain and you can use without limitations

def index():
	response.flash = 'Acessar e enviar conteúdo para midiacapoeira.in'
	return dict(message='Acessar e enviar conteúdo para midiacapoeira.in')

## [interna] Serve para autenticar usuários, por enquanto só serve para permitir que pessoas administrem o conteúdo
def user():
	return dict(form=auth())

