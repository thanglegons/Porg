from flask import Flask, request
from search.pipe.search_pipe import SearchPipe
from search.pipe.update_pipe import UpdatePipe

app = Flask(__name__)


@app.route('/search')
def simple_search():
    params = request.args.to_dict()
    container = SearchPipe(params).process()
    return container['pretty_result']


@app.route('/update')
def simple_update():
    params = request.args.to_dict()
    return UpdatePipe.update_from_id(params)



app.run(host='0.0.0.0', port=1910, debug=True)
