class Transform(object):

    def __init__(self, container):
        self.container = container
        self.params = container['params']

    def process(self):
        raw_result = self.container['raw_result']
        pretty_result = {'message': "success", 'success': 1}

        if not self.checkSuccess(raw_result):
            pretty_result['message'] = "failed"
            pretty_result['success'] = 0
        else:
            data = {}
            pretty_result['data'] = data

            hits = raw_result['hits']

            total_document = hits['total']['value']
            data['total'] = total_document

            data_from_es = hits['hits']
            needed_field = {
                'id': 'id',
                'author_searchable': 'author.name',
                'author_id': 'author.id',
                'average_rating': 'rating',
                'lenders_number': 'lenders',
                'title': 'title',
                'original_publication_year': 'public_year',
                'image_url': 'image_url'
            }
            pretty_data = []
            data['data'] = pretty_data
            for datum in data_from_es:
                source = datum['_source']
                pretty_datum = {}
                for ori_field, new_field in needed_field.items():
                    if ori_field in source.keys():

                        pretty_datum[new_field] = source[ori_field]
                pretty_data.append(pretty_datum)

            if 'aggregations' in raw_result:
                aggs = raw_result['aggregations']
                pretty_aggs = []
                pretty_result['aggs'] = pretty_aggs
                # Only genre is available
                genres = aggs['genre']
                buckets = genres['buckets']
                pretty_genres = []
                for bucket in buckets:
                    pretty_genre = {'id': bucket['key'], 'count': bucket['doc_count']}
                    pretty_genres.append(pretty_genre)

                pretty_aggs.append(pretty_genres)

        self.container['pretty_result'] = pretty_result
        return self.container

    @staticmethod
    def checkSuccess(raw_result):
        if '_shards' not in raw_result.keys():
            return False
        _shards = raw_result['_shards']
        if _shards['failed'] == 1:
            return False
        return True
