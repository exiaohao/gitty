import hug
import json
import logging

from utils.github import (
    GithubAPI,
    GithubAPIMethod,
    GithubRequest,
)

from action import (
    do_nothing,
    parse_created,
)

logger = logging.getLogger('gunicorn.error')

@hug.get('/')
def hello():
    return {
        "message": "Hi! I'm gitty, a github robot.",
    }



@hug.post('/')
def capture_action(body):
    try:
        req = GithubRequest(body['payload'])
        act = {
            'created': parse_created,
            'unknown': do_nothing,
        }.get(req.action, do_nothing)

        return act(req)
    except TypeError:
        logger.error(body)
