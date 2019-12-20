from pipe.build_query_pipe import BuildQuery
from pipe.query_pipe import Query
from pipe.transform import Transform
from pipe.paging import Paging


class SearchPipe(object):

    def __init__(self, params):
        self.container = {}
        if 'page' in params.keys():
            self.container['page'] = int(params['page'])
            params.pop('page', None)
        else:
            self.container['page'] = 1
        self.container['params'] = params

    def process(self):
        # Get from Cache
        # Build query
        self.container = BuildQuery(self.container).process()
        # Query
        self.container = Query.process(self.container)
        # Transform
        self.container = Transform(self.container).process()
        # Paging
        self.container = Paging(self.container).process()
        return self.container


