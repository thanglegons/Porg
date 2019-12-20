from flask import Flask, jsonify, request
from gateway.es_gateway import ESGateway
from pipe.search_pipe import SearchPipe

app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    results = ESGateway.es.get(index='prod_books', doc_type='title', id = 1)
    return jsonify(results['_source'])


@app.route('/search')
def simple_search():
    params = request.args.to_dict()
    # print(params)
    #
    # container = {'params': params}
    # b = BuildQuery(container)
    #
    # body = b.process()
    # body = json.loads(body['query'])
    #
    # print(body)
    # # print(jsonify(body))
    #
    # res = ESGateway.es.search(index="prod_books_3", body=body)
    # # print(type(res))
    container = SearchPipe(params).process()
    print(container)
    return container['pretty_result']


app.run(port=5000, debug=True)
