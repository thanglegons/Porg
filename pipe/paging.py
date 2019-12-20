class Paging(object):

    def __init__(self, container):
        self.container = container
        self.item_per_page = 5

    def process(self):
        if self.container['pretty_result']['success'] == 0:
            return self.container
        page_index = self.container['page']
        data = self.container['pretty_result']['data']['data']
        total = self.container['pretty_result']['data']['total']

        index_start = (page_index - 1) * self.item_per_page
        index_end = min(page_index * self.item_per_page, total)
        data = data[index_start:index_end]
        self.container['pretty_result']['data']['data'] = data

        return self.container
