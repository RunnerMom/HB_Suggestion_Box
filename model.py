#hackbright day 19
#sql web app exercise
#Gowri and Eva team

#Assignment definition: Users are students of hackbright
# Posts are ideas for hackbright improvements or speakers
# votes represent the user's ability to show support for an idea



import sqlite3
import traceback

DB = None
CONN = None

class Student(object):
    def __init__(self, first_name, last_name, github):
        self.first_name = first_name
        self.last_name = last_name
        self.github = github

    def add_student_to_db(self):
        sql = """INSERT into Students VALUES (?, ?, ?)"""   #expects 3 args
        DB.execute(sql, (self.first_name, self.last_name, self.github))
        CONN.commit()

    def get_student_by_github(github):
        sql = """SELECT first_name, last_name, github 
        FROM Students
        WHERE github = ?"""
        DB.execute(sql, (github,))
        record = DB.fetchone()

        return record


# get post by title
class Post(object):
    def __init__(self, title, body, author, timestamp):
        self.title = title
        self.body= body
        self.author = author
        self.timestamp = timestamp

    def add_post_to_db(self):
        sql = """INSERT into Posts (title, body, author, created_at) VALUES (?, ?, ?, ?)"""
        DB.execute(sql, (self.title, self.body, self.author, self.timestamp))
        CONN.commit()

    def get_post_id_by_title(self):
        sql = """SELECT id FROM Posts WHERE title = ?"""
        DB.execute(sql, (self.title,))
        record = DB.fetchone()

        return record        

    def get_post_by_title(self):
        sql = """SELECT * FROM Posts WHERE title = ?"""
        DB.execute(sql, (self.title,))
        record = DB.fetchone()

        return record

    def get_posts_by_author(self):
        sql = """SELECT * FROM Posts WHERE author = ?"""
        DB.execute(sql, (self.author,))
        records = DB.fetchall()

        return records


class Vote(object):
    def __init__(self, voter_id, post_id):
        self.voter_id=voter_id
        self.post_id=post_id

    def add_vote_to_db(self):
        sql = """INSERT into Votes VALUES (?, ?)  """
        DB.execute(sql, (self.voter_id,self.post_id))
        CONN.commit()

    def count_votes_by_post_id(self, post_id):
        sql = """SELECT COUNT(*) FROM Votes WHERE post_id = ?"""
        DB.execute(sql, self.post_id)
        record = DB.fetchone()

        return record

def connect_to_db():
    global DB, CONN
    CONN = sqlite3.connect("hackbright.db")
    DB = CONN.cursor()

def get_all_posts():
    sql = """SELECT * FROM Posts"""
    DB.execute(sql)
    records = DB.fetchall()

    return records
