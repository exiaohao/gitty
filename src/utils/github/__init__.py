import json
import requests


class NotCommentException(Exception):
    pass

class NotIssueException(Exception):
    pass

class NotRepositoryException(Exception):
    pass

class MethodNotAllowed(Exception):
    pass


def github_api(config, url):
    q = requests.post(url, data=config)
    return q.json()

class GithubAPIMethod:
    ISSUE_CLOSE = 'closed'
    ISSUE_OPEN = 'open'

    ISSUE_METHODS = [
        ISSUE_CLOSE,
        ISSUE_OPEN,
    ]

class HTTPRequest:
    GET = 'get'
    POST = 'post'
    PATCH = 'patch'

class GithubAPI:
    def __init__(self, github_config):
        self.github_config = github_config
    
    def _request(self, url, method, **data):
        if method == HTTPRequest.PATCH:
            q = requests.patch(
                url=url,
                json=data,
                headers={
                    "Authorization": "token {}".format(self.github_config['token']),
                })
            return q.json()

    def issue(self, url, method, **kwargs):
        if method not in GithubAPIMethod.ISSUE_METHODS:
            raise MethodNotAllowed
        # TODO: check is issue resource
        return self._request(url, HTTPRequest.PATCH, **{"state": method})


class GithubRequest:
    def __init__(self, payload_raw):
        self.payload_raw = payload_raw
        self.parse()

    def parse(self):
        self.payload = json.loads(self.payload_raw)
    
    @property
    def action(self):
        return self.payload.get('action', 'unknown')

    @property
    def comment(self):
        comment_dict = self.payload.get('comment', {})
        if not comment_dict:
            raise NotCommentException

        class Comment:
            pass
        c = Comment()
        
        for k, v in comment_dict.items():
            setattr(c, k, v)
        return c
    
    @property
    def issue(self):
        issue_dict = self.payload.get('issue', {})
        if not issue_dict:
            raise NotIssueException
        
        class Issue:
            pass
        
        i = Issue()
        for k, v in issue_dict.items():
            setattr(i, k, v)
        return i
    
    @property
    def repository(self):
        repository_dict = self.payload.get('repository', {})
        if not repository_dict:
            raise NotRepositoryException

        class Repository:
            pass
        
        r = Repository()
        for k, v in repository_dict.items():
            setattr(r, k, v)
        return r
