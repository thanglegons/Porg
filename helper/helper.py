SUCCESS_MESSAGE = {'message': 'success', 'success': 1}
FAILED_MESSAGE = {'message': 'failed', 'success': 0}


def is_integer(_str):
    return _str.isdigit()


def is_non_negative_integer(_str):
    return is_integer(_str) and int(_str) >= 0


def is_float(_str):
    _str = _str.replace('.', '', 1)
    return _str.isdigit()


def is_non_negative_float(_str):
    return is_float(_str) and float(_str) >= 0.0
