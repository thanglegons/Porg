import copy

from pipe.build_query_pipe import BuildQuery
from pipe.query_pipe import Query
from pipe.transform import Transform
from pipe.paging import Paging
from cache.search_cache import SearchCache
from datetime import datetime


class SearchPipe(object):

    def __init__(self, params):
        self.container = {}
        self.params = params
        if 'page' in params.keys():
            self.container['page'] = int(params['page'])
            params.pop('page', None)
        else:
            self.container['page'] = 1
        self.container['params'] = params
        self.cache = SearchCache.cache

    def process(self):
        # Get from Cache
        get_from_cache = copy.deepcopy(self.cache.get_item(self.params))
        if get_from_cache is not None:
            print('Get result from cache')
            pre_page = self.container['page']
            self.container = get_from_cache
            self.container['page'] = pre_page
        else:
            # Build query
            print('Building query for, ', self.params)
            self.container = BuildQuery(self.container).process()
            # Query
            start = datetime.now()
            print('Query to ES in ', end='')
            self.container = Query.process(self.container)
            print((datetime.now() - start).microseconds, 'microseconds')
            # Transform
            print('Transform result')
            self.container = Transform(self.container).process()
            # Cache
            if self.container['pretty_result']['success'] == 1:
                print('Caching result')
                self.cache.insert_item(self.params, copy.deepcopy(self.container))
        # Paging
        print('Paging result')
        self.container = Paging(self.container).process()

        return self.container
