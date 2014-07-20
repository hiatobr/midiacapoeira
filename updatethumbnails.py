# -*- coding: utf-8 -*-
#
# Script-gambiarra para gerar thumbnails para imagens que tenham sido
# acrescentadas ao banco de dados antes de a geração de thumbnails ter
# sido implementada.
# 
# Este script deve ser rodado por meio do seguinte comando: 
#
# $ ./web2py.py -S midiacapoeira -M -R applications/updatethumbnails.py
#

imageutils = local_import('imageutils')

imagens = db(db.imagem.thumbnail == None).select()

for img in imagens:
    img.update_record(thumbnail=imageutils.THUMB(img.arquivo, 200,
        200))
