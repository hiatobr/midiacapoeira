# -*- coding: utf-8 -*-
# this file is released under public domain and you can use without limitations

def index():
	response.flash = T("Seja bem vindx à midiacapoeira.in")
	return dict(message=T('Seja bem vindx à midiacapoeira.in'))

def chat():
	response.flash = T("Habilite javascript para midiacapoeira.in e freenode.net")
	return dict()

