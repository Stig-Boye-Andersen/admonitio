import markdown
import frontmatter
import os
import json
import sqlite3
from datetime import datetime


# Reads all the repositories 
def loadAndValidateRepositoriesCofiguration():
    with open('./admonitio/repositories.json', 'r') as f:
        repositoriesJSON = f.read()
        return json.loads(repositoriesJSON)

    

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

def hasValidAdmonitioFrontmatter(frontMatter):
    if not frontMatter.get('admonitio'):
        return False
    
    admonitioFrontmatter  = frontMatter.get('admonitio')

    if not admonitioFrontmatter.get('title'):
        return False

    if not admonitioFrontmatter.get('dueDate'):
        return False

    if not admonitioFrontmatter.get('notifications'):
        return False

    return True

def isAdmonitioFrontmatterValid(admonitioFrontmatter):
    
    return True

# Parse md files and insert into database
def parseMarkdownFiles(conn, markdownDirectory):
    c = conn.cursor()

    for filename in os.listdir(markdownDirectory):
        if filename.endswith('.md'):
            with open(markdownDirectory + '/' + filename, 'r') as f:
                frontMatter = frontmatter.loads(f.read())

                if hasValidAdmonitioFrontmatter(frontMatter):
                    print('A valid Admonitio frontmatter found in ' + markdownDirectory + "/" + filename)

                    admonitioFrontMatter  = frontMatter.get('admonitio')
                    title = admonitioFrontMatter.get('title')
                    dueDate = admonitioFrontMatter.get('dueDate')
                    convertedDueDate = datetime.strptime(dueDate, '%d.%m.%Y')

                    c.execute("INSERT INTO reminders(title, dueDate) VALUES(?, ?)", (title, convertedDueDate.strftime('%Y-%m-%d')))

                    reminderId = c.lastrowid
                    notifications = admonitioFrontMatter.get('notifications')    
                    for notification in notifications:
                        c.execute("INSERT INTO notifications(notification, reminder_id) VALUES(?, ?)", (notification, reminderId))
                else:
                    print('No valid Admonitio frontmatter found in ' + markdownDirectory + "/" + filename)
    conn.commit()

if __name__ == "__main__":
    conn = createDatabase()
    createTables(conn)

    repositories = loadAndValidateRepositoriesCofiguration()
    for repository in repositories:
        markdownDirectory = repository.get('name') + '/docs'
        print('Parsing all markdown files in repo ' + repository.get('name') + ' under ' + markdownDirectory)

        
        parseMarkdownFiles(conn, markdownDirectory)


    c = conn.cursor()
    c.execute("SELECT title, dueDate, DATE(dueDate,'-' || notification || ' day') as notificationDay \
               FROM reminders join notifications on reminders.id = notifications.reminder_id \
               WHERE notificationDay >= date('now') \
               ORDER BY notificationDay ASC")
    
    reminders = c.fetchall()
    for reminder in reminders:
        print(reminder)
