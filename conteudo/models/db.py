# -*- coding: utf-8 -*-
# this file is released under public domain and you can use without limitations

import time

db = DAL("sqlite://storage.sqlite")

session.connect(request, response, separate=True)

## Autenticação
from gluon.tools import *
auth = Auth(db)
auth.define_tables(username=True)
crud = Crud(db)
## /Autenticação

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
		'datetime',
		default=int(time.strftime('%s', time.localtime())),
		update=int(time.strftime('%s', time.localtime())),
		writable=False,
		readable=True,
		notnull=True,
	),
	Field(
		'autor',
		'string',
		default='Alguém',
	),
	Field(
		'fonte',
		'string',
		default='Internet',
	),
	Field(
		'licenca',
		'string',
		default='Domínio Público',
	),
	Field(
		'email',
		'string',
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
		'string',
		default='Alguém',
	),
	Field(
		'email',
		'string',
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
		'string',
		required=True,
		notnull=True,
	),
	Field(
		'rank',
		'integer',
		default=0,
		readable=True,
		writable=False,
		notnull=True,
	),
)

db.imagem.arquivo.requires = IS_NOT_EMPTY()
db.imagem_post.conteudo.requires = IS_NOT_EMPTY()
db.imagem_tag.imagem_id.requires = IS_IN_DB(db, db.imagem.id)
db.imagem_tag.imagem_id.readable = db.imagem_tag.imagem_id.writable = False
db.imagem_post.imagem_id.requires = IS_IN_DB(db, db.imagem.id)
db.imagem_post.imagem_id.readable = db.imagem_post.imagem_id.writable = False
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
		'datetime',
		default=int(time.strftime('%s', time.localtime())),
		update=int(time.strftime('%s', time.localtime())),
		writable=False,
		readable=True,
		notnull=True,
	),
	Field(
		'autor',
		'string',
		default='Alguém',
	),
	Field(
		'fonte',
		'string',
		default='Internet',
	),
	Field(
		'licenca',
		'string',
		default='Domínio Público',
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
		'string',
		default='Alguém',
	),
	Field(
		'email',
		'string',
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
		'string',
		required=True,
		notnull=True,
	),
	Field(
		'rank',
		'integer',
		default=0,
		readable=True,
		writable=False,
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

