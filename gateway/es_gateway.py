from elasticsearch import Elasticsearch


class ESGateway(object):
    es = Elasticsearch([{'host': 'localhost', 'port': 9200}])
    es_index = 'prod_books_4'
