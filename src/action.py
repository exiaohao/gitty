from utils.github import (
    GithubAPI,
    GithubAPIMethod,
)

from config import (
    Config,
    logger,
)


def do_nothing(req):
    logger.info('Get nothing todo, action:{}'.format(req.action))
    return {
        'msg': 'nothing to do',
    }

def parse_created(req):
    logger.info('Get created, req:{}'.format(req))
    github_api = GithubAPI(Config.GITHUB)
    if req.comment.body == '/close':
        return github_api.issue(req.issue.url, 'closed')
    elif req.comment.body == '/open':
        return github_api.issue(req.issue.url, 'open')
    else:
        return {
            'msg': 'nothing to do',
        }
