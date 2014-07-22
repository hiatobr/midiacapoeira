# -*- coding: utf-8 -*-

from gluon import current


def tagQuery(tags, ctbl, ttbl, query = 0, op = 'or', field =
    'texto_id'):
    '''
    Busca no banco de dados por conteúdo marcado pelas tags em <tags>.
    A operação é recursiva, tag por tag, juntando o resultado de uma
    busca ao resultado referente à tag anterior. Essa junção pode ser por
    intersecção (op = 'and') ou por união (op = 'or').
    Esta implementação preza por generalidade, de modo que a função
    pode ser utilizada para buscar qualquer tipo de conteúdo, desde
    que a variável <field> seja corretamente preenchida na chamada da
    função.
    
    <ctbl> = tabela de conteúdo
    <ttbl> = tabela de tags
    '''
    
    db = current.db
    
    try:
        # Escolhe uma tag e procura por índices de textos que a contêm
        tag_ref = db(ttbl.tag==tags.pop()).select(ttbl[field]).as_list()
        tag_ref = map(list.pop, map(dict.values, tag_ref))
        
        if query and op == 'or':
            return tagQuery(tags, ctbl, ttbl, ctbl.id.belongs(tag_ref) |
                    query)
        elif query and op == 'and':
            return tagQuery (tags, ctbl, ttbl,
                    ctbl.id.belongs(tag_ref) & query)
        else:
            return tagQuery(tags, ctbl, ttbl, ctbl.id.belongs(tag_ref))

    except IndexError:
        return db(query).select(ctbl.ALL).as_list()

