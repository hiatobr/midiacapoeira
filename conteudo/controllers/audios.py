# -*- coding: utf-8 -*-
# this file is released under public domain and you can use without limitations

def index():
	response.flash = 'Mentira!'
	return dict(message='Área de áudios ainda não implementada')

## [interna] Serve para autenticar usuários, por enquanto só serve para permitir que pessoas administrem o conteúdo
def user():
	return dict(form=auth())

