import json


class NotCommentException(Exception):
    pass

class NotIssueException(Exception):
    pass

class NotRepositoryException(Exception):
    pass

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
