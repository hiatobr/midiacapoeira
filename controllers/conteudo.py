# -*- coding: utf-8 -*-
# this file is released under public domain and you can use without limitations

queries = local_import('queries')

def index():
	response.flash = 'Acessar e enviar conteúdo para midiacapoeira.in'
	return dict(message='Acessar e enviar conteúdo para midiacapoeira.in')

def audios():
	response.flash = 'Mentira!'
	return dict(message='Área de áudios ainda não implementada')

## Padrão é mostrar as últimas imagens em grade na página inicial
def imagens():
	response.flash = 'Últimas imagens'
#	imagens = [
#		dict(
#			id = imagem['id'],
#			arquivo = imagem['arquivo'],
#		)
#		for imagem in db().select(db.imagem.ALL, orderby=~db.imagem.data)
#	]
	imagens = db().select(db.imagem.ALL, orderby=~db.imagem.data)
	return dict(imagens=imagens)

## Utilizado para visualizar uma imagem específica, assim como ver e enviar comentários
def imagens_ver():
	response.flash = 'Visualizar imagem'

	imagem = db.imagem(request.args(0,cast=int)) or redirect(URL('imagens'))
	db.imagem_post.imagem_id.default = imagem.id
	db.imagem_tag.imagem_id.default = imagem.id

	formC = SQLFORM(
		db.imagem_post,
		labels = {
			'autor':"Autor",
			'email':"E-mail",
			'conteudo':"Conteúdo",
		},
		col3 = {
			'autor':"Não é necessário se cadastrar ou se identificar.",
			'email':"Caso fornecido, SERÁ publicado.",
			'conteudo':SPAN("Comentários podem ser apagados de forma arbitrária conforme a ", A('política do site', _href=URL('sobre', 'termos')), "."),
		},
		submit_button = 'Enviar',
		table_name = 'comentarios',
	)
	if formC.process().accepted:
		response.flash = 'Comentário publicado'
	elif formC.errors:
		response.flash = 'Comentário NÃO publicado'

	formT = SQLFORM(
		db.imagem_tag,
		labels = {
			'tag':"Adicionar tags",
		},
		submit_button = 'Enviar',
		table_name = 'tags',
	)
	if formT.process().accepted:
		response.flash = 'Tag adicionada'
	elif formC.errors:
		response.flash = 'Tag NÃO adicionada'

	comentarios = db(db.imagem_post.imagem_id==imagem.id).select()
	tags = db(db.imagem_tag.imagem_id==imagem.id).select()

	return dict(imagem=imagem, comentarios=comentarios, tags=tags, formC=formC, formT=formT)

## TODO: Fazer função para enviar imagens
## Utilizado para enviar imagens
def imagens_enviar():
	response.flash = 'Enviar imagem para ' + response.title
	form = SQLFORM(db.imagem).process(next=URL('imagens'))
	return dict(form=form)

## [interna] Serve para recuperar uma imagem do banco de dados
## TODO: Fazer uma função de download que funcione como a ver(), fazendo download de conteúdo através do id
def imagens_download():
	return response.download(request, db)

## Utilizado para buscar imagens por tag, fonte, autor, email, licença.
def imagens_buscar():
	response.flash = 'Buscar imagens'

	tag = ''
	fonte = ''
	autor = ''
	email = ''
	licenca = ''
	imagem = ''
	tags = dict()
	fontes = dict()
	autores = dict()
	emails = dict()
	licencas = dict()
	imagens = dict()

	if (request.vars.tag) and len(request.vars.tag):
		tag = request.vars.tag
		tags_it = db(db.imagem_tag.tag == tag).select(db.imagem_tag.imagem_id)
		if (tags_it):
			tags = [
				dict (
					id = db(db.imagem.id == tag_it.imagem_id).select(db.imagem.ALL, orderby=~db.imagem.data)[0]['imagem.id'],
					arquivo = db(db.imagem.id == tag_it.imagem_id).select(db.imagem.ALL, orderby=~db.imagem.data)[0]['imagem.arquivo'],
				)
				for tag_it in tags_it
			]
	if (request.vars.fonte) and len(request.vars.fonte):
		fonte = request.vars.fonte
		fontes = [
			dict (
				id = fonte_it['imagem.id'],
				arquivo = fonte_it['imagem.arquivo'],
			)
			for fonte_it in db(db.imagem.fonte == fonte).select(db.imagem.ALL, orderby=~db.imagem.data)
		]
	if (request.vars.autor) and len(request.vars.autor):
		autor = request.vars.autor
		autores = [
			dict (
				id = autor_it['imagem.id'],
				arquivo = autor_it['imagem.arquivo'],
			)
			for autor_it in db(db.imagem.autor == autor).select(db.imagem.ALL, orderby=~db.imagem.data)
		]
	if (request.vars.email) and len(request.vars.email):
		email = request.vars.email
		emails = [
			dict (
				id = email_it['imagem.id'],
				arquivo = email_it['imagem.arquivo'],
			)
			for email_it in db(db.imagem.email == email).select(db.imagem.ALL, orderby=~db.imagem.data)
		]
	if (request.vars.licenca) and len(request.vars.licenca):
		licenca = request.vars.licenca
		licencas = [
			dict (
				id = licenca_it['imagem.id'],
				arquivo = licenca_it['imagem.arquivo'],
			)
			for licenca_it in db(db.imagem.licenca == licenca).select(db.imagem.ALL, orderby=~db.imagem.data)
		]
	if (request.vars.imagem) and len(request.vars.imagem):
		imagem = request.vars.imagem
		imagens = [
			dict (
				id = imagem_it['text.id'],
				arquivo = imagem_it['imagem.arquivo'],
			)
			for imagem_it in db(db.imagem.arquivo.contains(imagem)).select(db.imagem.ALL, orderby=~db.imagem.data)
		]

	form = FORM('Tag: ', INPUT(_name='tag'), BR(), 'Autor: ', INPUT(_name='autor'), BR(), 'E-mail: ', INPUT(_name='email'), BR(), 'Imagem: ', INPUT(_name='imagem'), BR(), INPUT(_type='submit'))

	return dict(tag=tag, fonte=fonte, autor=autor, email=email, licenca=licenca, imagem=imagem, tags=tags, fontes=fontes, autores=autores, emails=emails, imagens=imagens, licencas=licencas, form=form)

## Utilizado para apagar e alterar imagens arbitrariamente
#@auth.requires_membership('admin')
#def imagens_admin():
#	grid = SQLFORM.smartgrid(db.image,linked_tables=['post_image'])
#	return dict(grid=grid)

## Padrão é mostrar os últimos textos em grade na página inicial
def textos():
	response.flash = 'Últimos textos'
	textos = [
		dict(
			id = texto['id'],
			conteudo = texto['conteudo'],
		)
		for texto in db().select(db.texto.ALL, orderby=~db.texto.data)
	]
	return dict(textos=textos)

## Utilizado para visualizar um bloco de texto específico, assim como ver e enviar comentários e tags
def textos_ver():
	response.flash = 'Visualizar texto'

	texto = db.texto(request.args(0,cast=int)) or redirect(URL('textos'))

	db.texto_post.texto_id.default = texto.id
	db.texto_tag.texto_id.default = texto.id

	formC = SQLFORM(
		db.texto_post,
		labels = {
			'autor':"Autor",
			'email':"E-mail",
			'conteudo':"Conteúdo",
		},
		col3 = {
			'autor':"Não é necessário se cadastrar ou se identificar.",
			'email':"Caso fornecido, SERÁ publicado.",
			'conteudo':SPAN("Comentários podem ser apagados de forma arbitrária conforme a ", A('política do site', _href=URL('init', 'sobre', 'termos')), "."),
		},
		submit_button = 'Enviar',
		table_name = 'comentarios',
	)
	if formC.process().accepted:
		response.flash = 'Comentário publicado'
	elif formC.errors:
		response.flash = 'Comentário NÃO publicado'

	formT = SQLFORM(
		db.texto_tag,
		labels = {
			'tag':"Adicionar tags",
		},
		submit_button = 'Enviar',
		table_name = 'tags',
	)
	if formT.validate(keepvalues=True):
		response.flash = 'Tag adicionada'
                tags = map(lambda tag: tag.strip(' #'), request.post_vars.tag.split(','))

                # Checar se as tags adicionadas já não existem.
                s = db(db.texto_tag.texto_id==texto.id).select()
                old_tags = [row.tag for row in s]
                for tag in tags:
                    if tag not in old_tags:
                        db.texto_tag.insert(texto_id=texto.id, tag=tag)
	elif formC.errors:
		response.flash = 'Tag NÃO adicionada'

	comentarios = db(db.texto_post.texto_id==texto.id).select()
	tags = db(db.texto_tag.texto_id==texto.id).select()

	return dict(texto=texto, comentarios=comentarios, tags=tags, formC=formC, formT=formT)

## Utilizado para enviar blocos de texto
def textos_enviar():
	response.flash = 'Enviar texto para ' + response.title
	form = SQLFORM(db.texto).process(next=URL('textos'))
	return dict(form=form)

## [interna] Serve para recuperar um bloco de texto do banco de dados
## TODO: Fazer uma função de download que funcione como a ver(), fazendo download de conteúdo através do id
def textos_download():
	return response.textos_download(request, db)

### [interna] Serve para autenticar usuários, por enquanto só serve para permitir que pessoas administrem o conteúdo
#def user():
#	return dict(form=auth())

## Utilizado para buscar textos por tag, fonte, autor, email, licença. Busca DENTRO de textos ainda não está feita.
def textos_buscar():
	response.flash = 'Buscar em textos'

	tag = ''
	fonte = ''
	autor = ''
	email = ''
	licenca = ''
	texto = ''
	tags = dict()
	fontes = dict()
	autores = dict()
	emails = dict()
	licencas = dict()
	textos = dict()

	if (request.vars.tag) and len(request.vars.tag):
            tag = [t.strip(' #') for t in request.vars.tag.split(',')]
            query = queries.tagQuery(list(tag), db.texto, db.texto_tag)
            
            if (query):
		tags = [
			dict (
				id = txt['id'],
				conteudo = txt['conteudo'],
			)
                        for txt in sorted(query, key=lambda k: k['data'])
			]
	if (request.vars.fonte) and len(request.vars.fonte):
		fonte = request.vars.fonte
		fontes = [
			dict (
				id = fonte_it['texto.id'],
				conteudo = fonte_it['texto.conteudo'],
			)
			for fonte_it in db(db.texto.fonte == fonte).select(db.texto.ALL, orderby=~db.texto.data)
		]
	if (request.vars.autor) and len(request.vars.autor):
		autor = request.vars.autor
		autores = [
			dict (
				id = autor_it['texto.id'],
				conteudo = autor_it['texto.conteudo'],
			)
			for autor_it in db(db.texto.autor == autor).select(db.texto.ALL, orderby=~db.texto.data)
		]
	if (request.vars.email) and len(request.vars.email):
		email = request.vars.email
		emails = [
			dict (
				id = email_it['texto.id'],
				conteudo = email_it['texto.conteudo'],
			)
			for email_it in db(db.texto.email == email).select(db.texto.ALL, orderby=~db.texto.data)
		]
	if (request.vars.licenca) and len(request.vars.licenca):
		licenca = request.vars.licenca
		licencas = [
			dict (
				id = licenca_it['texto.id'],
				conteudo = licenca_it['texto.conteudo'],
			)
			for licenca_it in db(db.texto.licenca == licenca).select(db.texto.ALL, orderby=~db.texto.data)
		]
	if (request.vars.texto) and len(request.vars.texto):
		texto = request.vars.texto
		textos = [
			dict (
				id = texto_it['text.id'],
				conteudo = texto_it['texto.conteudo'],
			)
			for texto_it in db(db.texto.conteudo.contains(texto)).select(db.texto.ALL, orderby=~db.texto.data)
		]

	form = FORM('Tags: ', INPUT(_name='tag'), BR(), 'Autor: ', INPUT(_name='autor'), BR(), 'E-mail: ', INPUT(_name='email'), BR(), 'Conteúdo do texto: ', INPUT(_name='texto'), BR(), INPUT(_type='submit'))

	return dict(tag=tag, fonte=fonte, autor=autor, email=email, licenca=licenca, texto=texto, tags=tags, fontes=fontes, autores=autores, emails=emails, textos=textos, licencas=licencas, form=form)

## FIXME: RSS não está funcionando!
#def textos_rss():
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

def videos():
	response.flash = 'Mentira!'
	return dict(message='Área de vídeos ainda não implementada')

### Utilizado para apagar e alterar textos arbitrariamente
#@auth.requires_membership('admin')
#def admin():
#	grid = SQLFORM.smartgrid(db.text,linked_tables=['post_text'])
#	return dict(grid=grid)

