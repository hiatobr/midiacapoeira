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

# Disponibilizando o banco de dados para módulos.
from gluon import current
current.db = db

imageutils = local_import('imageutils', reload=True)

## Tabelas para Imagens
db.define_table(
	'imagem',
	Field(
		'arquivo',
		'upload',
		required=True,
		uploadseparate=True,
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
        Field(
                'thumbnail',
                'upload',
                uploadseparate=True,
                readable=False,
                #notnull=True,
        ),
)
db.define_table(
	'imagem_post',
	Field(
		'imagem_id',
		'reference imagem',
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
	'imagem_tag',
	Field(
		'imagem_id',
		'reference imagem'
	),
	Field(
		'tag',
		required=True,
		notnull=True,
	),
)

db.imagem.arquivo.requires = IS_NOT_EMPTY()
db.imagem.thumbnail.compute = lambda row: imageutils.THUMB(row.arquivo, 200, 200)
db.imagem_post.conteudo.requires = IS_NOT_EMPTY()
db.imagem_tag.imagem_id.requires = IS_IN_DB(db, db.imagem.id)
db.imagem_post.imagem_id.requires = IS_IN_DB(db, db.imagem.id)
db.imagem_tag.imagem_id.writable = db.imagem_tag.imagem_id.readable = False
db.imagem_post.imagem_id.writable = db.imagem_post.imagem_id.readable = False
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

