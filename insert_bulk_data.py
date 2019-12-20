from flask import Flask, json
from search.gateway.es_gateway import ESGateway

es = ESGateway.es

print(es)

app = Flask(__name__)

userful_names = ['description', 'title', 'average_rating', 'author_id', 'categories', 'isbn13', 'original_publication_year']
additional_names = ['author_searchable', 'lenders_number']

books_data_path = 'search/data/books13.json'
author_data_path = 'search/data/authors.json'

books_data = open(books_data_path, 'r').readlines()
authors_data = open(author_data_path, 'r').readlines()

# print(len(books_data))

id_to_author = {}
for author_data in authors_data:
    data = json.loads(author_data)
    id_to_author[data['id']] = data['name']

count = 0

for book_data in books_data:
    es_query_body = {}
    to_json = json.loads(book_data)
    for name in userful_names:
        if name == 'average_rating':
            es_query_body[name] = float(to_json[name])
        elif name == 'isbn13':
            es_query_body['id'] = to_json[name]
        else:
            es_query_body[name] = to_json[name]
    es_query_body['author_searchable'] = id_to_author[to_json['author_id']]
    es_query_body['lenders_number'] = 0
    _id = int(to_json['isbn13'])
    count += 1

    if count % 100 == 0:
        print(count, "loaded")

    result = es.index(index='prod_books_5', doc_type='title', id=_id, body=es_query_body)
