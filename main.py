from github import Github
from github import Auth

access_token = "your_access_token"

auth = Auth.Token(access_token)

gh = Github(auth=auth)


for repo in gh.get_user().get_repos():
    if repo.full_name == "dinnerchief/dinnerchief": # here is your 'main' repo
        continue
    repo.delete()
