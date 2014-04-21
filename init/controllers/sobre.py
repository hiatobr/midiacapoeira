# -*- coding: utf-8 -*-
# this file is released under public domain and you can use without limitations

def index():
	response.flash = T("Sobre midiacapoeira.in")
	return dict(message=T("Sobre o projeto midiacapoeira.in"))

def editoriais():
	response.flash = T("Informações sobre editoriais")
	return dict(message=T("Sobre os editoriais de midiacapoeira.in"))

def licenca():
	response.flash = T("Licença")
	return dict(message=T("Licença do site e de conteúdo para midiacapoeira.in"))

def links():
	response.flash = T("Links externos")
	return dict(message=T("Links relacionados ao projeto midiacapoeira.in"))

def manifesto():
	response.flash = T("Manifesto")
	return dict(message=T("Subterfúgio ideológico para a criação de midiacapoeira.in"))

def politica():
	response.flash = T("Política do site")
	return dict(message=T("Política do site para midiacapoeira.in"))

def referencias():
	response.flash = T("Referências e influências")
	return dict(message=T("Influências, parcerias e ferramentas utilizadas para construir o site midiacapoeira.in"))

def termos():
	response.flash = T("Termos de uso do serviço")
	return dict(message=T("Termos de uso de serviço para midiacapoeira.in"))

