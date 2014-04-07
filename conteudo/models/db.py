# -*- coding: utf-8 -*-
# this file is released under public domain and you can use without limitations

import time

db = DAL("sqlite://storage.sqlite")

request.requires_https()
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
	'text',
	Field(
		'body',
		'text',
		required=True,
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
	Field(
		'author',
		default='Anônimx',
	),
	Field(
		'email',
	),
)
db.define_table(
	'post_text',
	Field(
		'text_id',
		'reference text',
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
	'tag_text',
	Field('text_id', 'reference text'),
	Field('tag'),
)
db.text.body.requires = IS_NOT_EMPTY()
db.post_text.body.requires = IS_NOT_EMPTY()
db.post_text.text_id.requires = IS_IN_DB(db, db.image.id)
db.post_text.text_id.readable = db.post_text.text_id.writable = False
db.tag_text.text_id.requires = IS_IN_DB(db, db.image.id)
db.tag_text.text_id.readable = db.tag_text.text_id.writable = False
## /Tabelas para Textos

