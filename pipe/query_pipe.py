from gateway.es_gateway import ESGateway


class Query(object):

    @staticmethod
    def process(container):
        built_query = container['query']
        try:
            raw_result = ESGateway.es.search(index=ESGateway.es_index, body=built_query)
        except:
            raw_result = {'_shards': {'failed': 1, 'successful': 0}}
        container['raw_result'] = raw_result
        return container
