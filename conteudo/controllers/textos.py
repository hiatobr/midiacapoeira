# -*- coding: utf-8 -*-
# this file is released under public domain and you can use without limitations

## Necessário para a busca com xmlrpc
#import xmlrpclib
#service = Service()

## Padrão é mostrar os últimos textos em grade na página inicial
def index():
	response.flash = 'Últimos textos'
	texts = [
		dict(
			id = text['id'],
			body = text['body'],
		)
		for text in db().select(db.text.ALL, orderby=~db.text.date)
	]
	return dict(texts=texts)

## Utilizado para visualizar um bloco de texto específico, assim como ver e enviar comentários
def ver():
	response.flash = 'Visualizar texto'
	text = db.text(request.args(0,cast=int)) or redirect(URL('index'))
	db.post_text.text_id.default = text.id
	db.tag_text.text_id.default = text.id
	formC = SQLFORM(db.post_text)
	if formC.process().accepted:
		response.flash = 'Comentário publicado'
	formT = SQLFORM(db.tag_text)
	if formT.process().accepted:
		response.flash = 'Tag adicionada'
	comments = db(db.post_text.text_id==text.id).select()
	tags = db(db.tag_text.text_id==text.id).select()
	return dict(text=text, comments=comments, tags=tags, formC=formC, formT=formT)

## Utilizado para enviar blocos de texto
def enviar():
	response.flash = 'Enviar texto'
	form = SQLFORM(db.text).process(next=URL('index'))
	return dict(form=form)

## [interna] Serve para recuperar um bloco de texto do banco de dados
## TODO: Fazer uma função de download que funcione como a ver(), fazendo download de conteúdo através do id
def download():
	return response.download(request, db)

## [interna] Serve para autenticar usuários, por enquanto só serve para permitir que pessoas administrem o conteúdo
def user():
	return dict(form=auth())

## Utilizado para buscar textos po tag, autor e email. Busca DENTRO de textos ainda não está feita.
def buscar():
	response.flash = 'Buscar em textos'
	tag = ''
	author = ''
	email = ''
	texto = ''
	tags = dict()
	authors = dict()
	emails = dict()
	textos = dict()
	if (request.vars.tag) and len(request.vars.tag):
		tag = request.vars.tag
		tags_it = db(db.tag_text.tag == tag).select(db.tag_text.text_id)
		if (tags_it):
			tags = [
				dict (
					id = db(db.text.id == tag_it.text_id).select(db.text.ALL, orderby=~db.text.date)[0]['text.id'],
					body = db(db.text.id == tag_it.text_id).select(db.text.ALL, orderby=~db.text.date)[0]['text.body'],
				)
				for tag_it in tags_it
			]
	if (request.vars.autor) and len(request.vars.autor):
		author = request.vars.autor
		authors = [
			dict (
				id = author_it['text.id'],
				body = author_it['text.body'],
			)
			for author_it in db(db.text.author == author).select(db.text.ALL, orderby=~db.text.date)
		]
	if (request.vars.email) and len(request.vars.email):
		email = request.vars.email
		emails = [
			dict (
				id = email_it['text.id'],
				body = email_it['text.body'],
			)
			for email_it in db(db.text.email == email).select(db.text.ALL, orderby=~db.text.date)
		]
	if (request.vars.texto) and len(request.vars.texto):
		texto = request.vars.texto
		textos = [
			dict (
				id = texto_it['text.id'],
				body = texto_it['text.body'],
			)
			for texto_it in db(db.text.body.contains(texto)).select(db.text.ALL, orderby=~db.text.date)
		]
	form = FORM('Busca:', BR(), 'Tag: ', INPUT(_name='tag'), BR(), 'Autor: ', INPUT(_name='autor'), BR(), 'E-mail: ', INPUT(_name='email'), BR(), 'Conteúdo do texto: ', INPUT(_name='texto'), BR(), INPUT(_type='submit'))
	return dict(tag=tag, author=author, email=email, texto=texto, tags=tags, authors=authors, emails=emails, textos=textos, form=form)

## FIXME: RSS não está funcionando!
#def rss():
#	response.generic_patterns = ['.rss']
#	items = db().select(db.text.ALL, orderby=~db.text.date)
#	return dict(
#		title = 'Narrativas Textuais',
#		link = 'https://midiacapoeira.in/textos',
#		description = 'RSS midiacapoeira.in',
#		created_on = request.now,
#		items = [
#			dict(
#				title = item.id,
#				link = URL(
#					'ver',
#					args=item.id,
#					scheme=True,
#					host=True,
#					extension=False,
#				),
#				description = XML(
#					item.body[:250],
#					sanitize=True,
#				),
#				created_on = request.now,
#			)
#			for item in items
#		],
#	)

## Utilizado para apagar e alterar textos arbitrariamente
@auth.requires_membership('admin')
def admin():
	grid = SQLFORM.smartgrid(db.text,linked_tables=['post_text'])
	return dict(grid=grid)

