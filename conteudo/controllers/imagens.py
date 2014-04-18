# -*- coding: utf-8 -*-
# this file is released under public domain and you can use without limitations

## Padrão é mostrar as últimas imagens em grade na página inicial
def index():
	response.flash = 'Últimas imagens'
	imagens = db().select(db.imagem.ALL, orderby=~db.imagem.data)
	return dict(imagens=imagens)

## Utilizado para visualizar uma imagem específica, assim como ver e enviar comentários
def ver():
	response.flash = 'Visualizar imagem'
	imagem = db.imagem(request.args(0,cast=int)) or redirect(URL('index'))
	db.imagem_post.imagem_id.default = imagem.id
	form = SQLFORM(db.imagem_post)
	if form.process().accepted:
		response.flash = 'Comentário publicado'
	comentarios = db(db.imagem_post.imagem_id==imagem.id).select()
	return dict(imagem=imagem, comentarios=comentarios, form=form)

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

