import pystache


def build_function():
    prefer_high_lender = """
    "source": "Math.log(2 + (doc['lenders_number'].value + 1) * (doc['average_rating'].value))"
    """
    return {"function": prefer_high_lender}


def build_sort():
    sort_by_score = """"_score": {
            "order": "desc"
        }"""
    return {"sort": sort_by_score}


def build_aggs(params):
    print(params)
    if "category" in params.keys():
        return {}
    aggs = """"genre": {
            "terms": {
                "field": "categories",
                "size": 5
            }
        }"""
    return {"aggs": aggs}


class BuildQuery(object):

    def __init__(self, container):
        self.container = container
        self.params = container['params']
        self.renderer = pystache.Renderer()

    def process(self):
        build_dict = {}
        build_dict.update(self.build_queries(self.params))
        build_dict.update(build_function())
        build_dict.update({"size": 1000})
        build_dict.update(build_sort())
        build_dict.update(build_aggs(self.params))
        full_query_path = './template/full_query.mustache'
        result = self.renderer.render_path(full_query_path, build_dict)
        result = result.replace('&quot;', '"')
        result = result.replace('&#x27;', '\'')
        self.container.update({"query": result})
        return self.container

    def build_queries(self, params):
        # q, search_filter, category
        all_queries = []
        if "q" in params.keys():
            q = params["q"]
            if "search_filter" in params.keys():
                q_filter = params["search_filter"]
                all_queries.append(self.renderer.render_path('./template/query/query_filter.mustache',
                                                             {"field": q_filter, "q": q}))
            else:
                all_queries.append(self.renderer.render_path('./template/query/query_all.mustache',
                                                         {"q": q}))
        if "category" in params.keys():
            q_category = params["category"]
            all_queries.append(self.renderer.render_path('./template/query/query_category.mustache',
                                                         {"category_id": q_category}))

        return {"queries": ','.join(all_queries)}
