from elasticsearch import Elasticsearch


class ESGateway(object):
    es = Elasticsearch([{'host': '3.1.80.54', 'port': 9200}])
    es_index = 'prod_books_5'
