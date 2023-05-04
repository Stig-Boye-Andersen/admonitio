import markdown
import frontmatter
import os
import json
import sqlite3
import datetime

def getRepositories():
    with open('./admonitio/repositories.json', 'r') as f:
        repositoriesString = f.read()
        return json.loads(repositoriesString)

#create a function that creates an in memory sql lite database
def createDatabase():
    conn = sqlite3.connect(':memory:')
    c = conn.cursor()

    return conn

#Define tabels for the database
def createTables(conn):
    c = conn.cursor()
    c.execute('''CREATE TABLE reminders(id integer primary key, title text, dueDate text)''')
    c.execute('''CREATE TABLE notifications(id integer primary key, notification integer, reminder_id integer, FOREIGN KEY(reminder_id) REFERENCES reminders(id))''')
    conn.commit()

def hasAdmonitioFrontmatter(mdFrontmatter):
    if not mdFrontmatter.get('admonitio'):
        return False
    
    return True

def isAdmonitioFrontmatterValid(admonitioFrontmatter):
    if not admonitioFrontmatter.get('title'):
        return False

    if not admonitioFrontmatter.get('dueDate'):
        return False

    if not admonitioFrontmatter.get('notifications'):
        return False

    return True

#Parse md files and insert into database
def parseMdFileAndInsertIntoDb(conn, directory):
    c = conn.cursor()

    docsDirectory = directory + '/docs'

    for filename in os.listdir(docsDirectory):
        if filename.endswith('.md'):
            with open(docsDirectory + '/' + filename, 'r') as f:
                frontMatter = frontmatter.loads(f.read())

                if hasAdmonitioFrontmatter(frontMatter):
                    admonitioFrontMatter  = frontMatter.get('admonitio')
                    if isAdmonitioFrontmatterValid(admonitioFrontMatter):
                        title = admonitioFrontMatter.get('title')
                        dueDate = admonitioFrontMatter.get('dueDate')
                        c.execute("INSERT INTO reminders(title, dueDate) VALUES(?, ?)", (title, dueDate))

                        reminderId = c.lastrowid
                        notifications = admonitioFrontMatter.get('notifications')    
                        for notification in notifications:
                            c.execute("INSERT INTO notifications(notification, reminder_id) VALUES(?, ?)", (notification, reminderId))
    conn.commit()

if __name__ == "__main__":
    conn = createDatabase()
    createTables(conn)

    repositories = getRepositories()
    for repo in repositories:
        parseMdFileAndInsertIntoDb(conn, repo.get('name'))

    #Select the reminder that will expire first 
    c = conn.cursor()
    c.execute("SELECT title, dueDate, notification as notificationDate FROM reminders join notifications on reminders.id = notifications.reminder_id")
    print(c.fetchall())
