from search.gateway.es_gateway import ESGateway
import helper.helper as helper


class UpdatePipe(object):

    @staticmethod
    def update_from_id(params):
        if 'id' not in params.keys():
            return helper.FAILED_MESSAGE
        if not helper.is_integer(params['id']):
            return helper.FAILED_MESSAGE
        _index = int(params['id'])
        body_doc = {}
        if 'lenders' in params.keys():
            if not helper.is_non_negative_integer(params['lenders']):
                return helper.FAILED_MESSAGE
            body_doc['lenders_number'] = int(params['lenders'])
        if 'rating' in params.keys():
            if not helper.is_non_negative_float(params['lenders']):
                return helper.FAILED_MESSAGE
            if float(params['rating']) > 5.0:
                return helper.FAILED_MESSAGE
            body_doc['average_rating'] = float(params['rating'])
        try:
            print(body_doc)
            ESGateway.es.update(ESGateway.es_index, doc_type='_doc', id=_index, body={'doc': body_doc})
        except:
            return helper.FAILED_MESSAGE
        finally:
            return helper.SUCCESS_MESSAGE
