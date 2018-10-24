from utils.github import (
    GithubAPI,
    GithubAPIMethod,
)

from config import (
    Config,
    logger,
)


def do_nothing(req):
    # TODO: record unknown actions
    logger.info('Get nothing todo, action:{}'.format(req.action))
    return {
        'msg': 'nothing to do',
    }

def parse_created(req):
    # TODO: make action configable, remove if/else
    logger.info('Get created, req:{}'.format(req))
    github_api = GithubAPI(Config.GITHUB)
    if req.comment.body == '/close':
        # TODO: better response, make a wrapper
        return github_api.issue(req.issue.url, 'closed')
    elif req.comment.body == '/open':
        return github_api.issue(req.issue.url, 'open')
    else:
        return {
            'msg': 'nothing to do',
        }
