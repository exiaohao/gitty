import hug
import json
import logging

from .utils.github import (
    GithubAPI,
    GithubAPIMethod,
    GithubRequest,
)

from .action import (
    do_nothing,
    parse_created,
)

from config import Config


logger = logging.getLogger('gunicorn.error')

@hug.get('/test')
@hug.default_input_format()
def hello():
    return {
        "message": "Hi! I'm gitty, a github robot.",
    }



@hug.post('/')
def capture_action(body):
    req = GithubRequest(body['payload'])

    act = {
        'created': parse_created,
        'unknown': do_nothing,
    }.get(req.action)

    return act(req)