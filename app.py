from flask import Flask, request
from search.pipe.search_pipe import SearchPipe

app = Flask(__name__)


@app.route('/search')
def simple_search():
    params = request.args.to_dict()
    container = SearchPipe(params).process()
    return container['pretty_result']


app.run(host='0.0.0.0', port=1910, debug=True)
