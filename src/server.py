import hug
import json
import logging


logger = logging.getLogger('gunicorn.error')

@hug.get('/test')
@hug.default_input_format()
def hello():
    logger.info("Get", request)
    return {
        "request": request,
        "message": "ok",
    }

@hug.post('/')
def capture_action(body):
    logger.info("Post: {}".format(body))
    return {
        "request": body,
        "message": "ok",
    }