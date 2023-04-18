# import logging
# import logging.handlers
import markdown
import frontmatter
import os
import json

if __name__ == "__main__":
    repositoriesString = os.environ["REPOSITORIES"]
    repositoriesJSON = json.loads(repositoriesString)

    print(repositoriesJSON[0]["name"])
    #data = frontmatter.load(repoName + '/reminders/client-secret.md')

    #print(data['reminder-date'])
    #print(data['remind'])
