import json

import numpy as np
from datetime import datetime

books_data_path = './data/books13.json'
num_cat = 38
num_random_vec = 38


def feature_transform(vec):
    len_cat = len(vec)
    random_feature = np.random.rand(len_cat)
    random_feature = sorted(random_feature, reverse=True)
    norm_feature = random_feature / np.linalg.norm(random_feature)
    return norm_feature


def load_feature_vector():
    books_data = open(books_data_path, 'r').readlines()
    _max_book = len(books_data)
    _book_feature = {}
    _book_data = {}
    for book_data in books_data:
        to_json = json.loads(book_data)
        categories = to_json['categories']
        isbn13 = int(to_json['isbn13'])
        scores = feature_transform(categories)
        feature_vector = np.zeros(num_cat)
        for (category, score) in zip(categories, scores):
            feature_vector[category - 1] = score
        _book_feature[isbn13] = feature_vector
        _book_data[isbn13] = {'author_id': int(to_json['author_id']), 'title': to_json['title'],
                              'image_url': to_json['image_url']}
    return _max_book, _book_feature, _book_data


def load_random_vec():
    _random_vec = np.random.randn(num_random_vec, num_cat)
    return _random_vec


def generate_hash(vec):
    bool_s = (np.dot(vec, np.transpose(random_vec)) > 0).astype(int)
    return ''.join(bool_s.astype('str'))


def generate_hash_table():
    _book_hash = {}
    for (isbn, feature) in book_feature.items():
        _book_hash[isbn] = generate_hash(feature)
    return _book_hash


def change_random_weight_time_by_time():
    current_time = datetime.now()
    if (current_time - last_time_changed).seconds > MAX_TIME_RANDOM:
        global random_weight
        random_weight = np.random.rand(num_random_vec)


MAX_TIME_RANDOM = 10 * 60
last_time_changed = datetime.now()
random_weight = np.random.rand(num_random_vec)
max_book, book_feature, book_data = load_feature_vector()
random_vec = load_random_vec()
book_hash = generate_hash_table()
print("Loading data done")
