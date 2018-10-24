from .utils.github import (
    GithubAPI,
    GithubAPIMethod,
)


def do_nothing(_):
    return {
        'msg': 'nothing to do',
    }

def parse_created(req):
    github_api = GithubAPI(Config.GITHUB)
    if req.comment.body == '/close':
        return github_api.issue(req.issue.url, 'closed')
    elif req.comment.body == '/open':
        return github_api.issue(req.issue.url, 'open')
    else:
        return {
            'msg': 'nothing to do',
        }
