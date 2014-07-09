# -*- coding: utf-8 -*-
# this file is released under public domain and you can use without limitations

def index():
	response.flash = T('Seja bem vindx à ') + response.title
	return dict(message = T('Seja bem vindx à ') + response.title)

