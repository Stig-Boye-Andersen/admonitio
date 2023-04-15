# import logging
# import logging.handlers
import markdown
import frontmatter
import os

if __name__ == "__main__":
    repoName = os.environ["REPO"]

    data = frontmatter.load(repoName + '/reminders/client-secret.md')

    print(data['reminder-date'])
    print(data['remind'])
