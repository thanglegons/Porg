from elasticsearch import Elasticsearch
import json

from flask import jsonify

from pipe.build_query_pipe import *

print(build_function())

params = {'q': 'star wars'}
container = {'params': params}
b = BuildQuery(container)

body = b.process()
body = json.loads(body)

es = Elasticsearch([{'host': 'localhost', 'port': 9200}])

res = es.search(index="prod_books_3", body=json.loads(body))

print(jsonify(res))