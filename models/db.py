# -*- coding: utf-8 -*-
# this file is released under public domain and you can use without limitations

import time

session.connect(request, response, separate=True)

## Autenticação
from gluon.tools import *
auth = Auth(db)
auth.define_tables(username=True)
crud = Crud(db)
## /Autenticação

## Tabelas para Imagens
db.define_table(
	'image',
	Field(
		'file',
		'upload',
		required=True,
		uploadseparate=True,
		notnull=True,
	),
	Field(
		'date',
		default=int(time.strftime('%s', time.localtime())),
		update=int(time.strftime('%s', time.localtime())),
		writable=False,
		readable=True,
		notnull=True,
	),
)
db.define_table(
	'post_image',
	Field(
		'image_id',
		'reference image',
	),
	Field(
		'author',
		default='Anônimx',
	),
	Field(
		'email',
	),
	Field(
		'body',
		'text',
		required=True,
		notnull=True,
	),
)
db.define_table(
	'tag_image',
	Field('image_id', 'reference image'),
	Field('tag'),
)
db.tag_image.image_id.requires = IS_IN_DB(db, db.image.id)
db.post_image.image_id.requires = IS_IN_DB(db, db.image.id)
db.tag_image.image_id.writable = db.tag_image.image_id.readable = False
db.post_image.image_id.writable = db.post_image.image_id.readable = False
## /Tabelas para Imagens

## Tabelas para Textos
db.define_table(
	'texto',
	Field(
		'conteudo',
		'text',
		required=True,
		notnull=True,
	),
	Field(
		'data',
		default=int(time.strftime('%s', time.localtime())),
		update=int(time.strftime('%s', time.localtime())),
		writable=False,
		readable=True,
		notnull=True,
	),
	Field(
		'autor',
		default='Alguém',
	),
	Field(
		'fonte',
	),
	Field(
		'licenca',
	),
	Field(
		'email',
	),
)
db.define_table(
	'texto_post',
	Field(
		'texto_id',
		'reference texto',
	),
	Field(
		'autor',
		default='Alguém',
	),
	Field(
		'email',
	),
	Field(
		'conteudo',
		'text',
		required=True,
		notnull=True,
	),
)
db.define_table(
	'texto_tag',
	Field(
		'texto_id',
		'reference texto'
	),
	Field(
		'tag',
		required=True,
		notnull=True,
	),
)

db.texto.conteudo.requires = IS_NOT_EMPTY()
db.texto_post.conteudo.requires = IS_NOT_EMPTY()
db.texto_post.texto_id.requires = IS_IN_DB(db, db.texto.id)
db.texto_post.texto_id.readable = db.texto_post.texto_id.writable = False
db.texto_tag.texto_id.requires = IS_IN_DB(db, db.texto.id)
db.texto_tag.texto_id.readable = db.texto_tag.texto_id.writable = False
## /Tabelas para Textos

