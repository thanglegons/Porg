import copy

from cache.recommend_cache import RecommendCache
import helper.helper as helper
import recommend.prepare_data as recommend_data
import numpy as np


class RecommenderSystem(object):

    def __init__(self, params):
        self.params = params
        self.cache = RecommendCache.cache

    @staticmethod
    def calculate_diff(hash1, hash2):
        num_diff = 0.0
        for i in range(len(hash1)):
            num_diff += float(hash1[i] != hash2[i]) * recommend_data.random_weight[i]
        return num_diff

    @staticmethod
    def get_top_recommend(isbn13, top):
        book_hash = recommend_data.book_hash[isbn13]
        result = []
        for (book_isbn, hash_feature) in recommend_data.book_hash.items():
            if isbn13 == book_isbn:
                continue
            num_diff = RecommenderSystem.calculate_diff(book_hash, hash_feature)
            num_diff = num_diff + np.random.rand() / 2.0
            if recommend_data.book_data[isbn13]['author_id'] == recommend_data.book_data[book_isbn]['author_id']:
                num_diff -= 3
            if recommend_data.book_data[book_isbn][
                'image_url'] == 'https://s.gr-assets.com/assets/nophoto/book/111x148-bcc042a9c91a29c1d680899eff700a03.png':
                num_diff += 1000
            result.append([num_diff, recommend_data.book_data[book_isbn]['title'], book_isbn,
                           recommend_data.book_data[book_isbn]['image_url']])
        result = sorted(result)
        result = result[:top]
        return result

    @staticmethod
    def transform(data):
        transformed_data = []
        for datum in data:
            transformed_datum = {'score': datum[0], 'title': datum[1], 'isbn': datum[2], 'image_url': datum[3]}
            transformed_data.append(transformed_datum)
        return transformed_data

    def process(self):
        recommend_data.change_random_weight_time_by_time()
        get_from_cache = copy.deepcopy(self.cache.get_item(self.params))
        if get_from_cache is not None:
            print('Get result from cache')
            return get_from_cache
        if 'id' not in self.params:
            return helper.FAILED_MESSAGE
        if not helper.is_non_negative_integer(self.params['id']):
            return helper.FAILED_MESSAGE
        if 'top' not in self.params:
            top = 10
        else:
            if not helper.is_non_negative_integer(self.params['top']):
                return helper.FAILED_MESSAGE
            top = int(self.params['top'])
        book_id = int(self.params['id'])
        if book_id not in recommend_data.book_feature.keys():
            return helper.FAILED_MESSAGE

        response = copy.deepcopy(helper.SUCCESS_MESSAGE)
        response['book_ids'] = RecommenderSystem.transform(RecommenderSystem.get_top_recommend(book_id, top))
        # Cache response
        self.cache.insert_item(self.params, copy.deepcopy(response))
        return response
