import time


def func(event, context):
    time.sleep(10)
    return {
        'status': 200,
        'data': 'OK',
    }

