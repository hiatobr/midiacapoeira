# -*- coding: utf-8 -*-
# this file is released under public domain and you can use without limitations

## Padrão é mostrar as últimas imagens em grade na página inicial
def index():
	response.flash = 'Últimas imagens'
	images = db().select(db.image.ALL, orderby=~db.image.date)
	return dict(images=images)

## Utilizado para visualizar uma imagem específica, assim como ver e enviar comentários
def ver():
	response.flash = 'Visualizar imagem'
	image = db.image(request.args(0,cast=int)) or redirect(URL('index'))
	db.post_image.image_id.default = image.id
	form = SQLFORM(db.post_image)
	if form.process().accepted:
		response.flash = 'Comentário publicado'
	comments = db(db.post_image.image_id==image.id).select()
	return dict(image=image, comments=comments, form=form)

## TODO: Fazer função para enviar imagens

## [interna] Serve para recuperar uma imagem do banco de dados
## TODO: Fazer uma função de download que funcione como a ver(), fazendo download de conteúdo através do id
def download():
	return response.download(request, db)

## [interna] Serve para autenticar usuários, por enquanto só serve para permitir que pessoas administrem o conteúdo
def user():
	return dict(form=auth())

## Utilizado para apagar e alterar imagens arbitrariamente
@auth.requires_membership('admin')
def admin():
	grid = SQLFORM.smartgrid(db.image,linked_tables=['post_image'])
	return dict(grid=grid)

