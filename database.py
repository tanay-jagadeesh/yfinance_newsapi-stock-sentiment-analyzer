import sqlite3

conn = sqlite3.connect('news.sentiment.db')

#Create a cursor
c = conn.cursor()

#Create an article table
# language=sql
c.execute("""CREATE TABLE articles (
    article_id INTEGER PRIMARY KEY AUTOINCREMENT,
    ticker TEXT,
    title TEXT,
    description TEXT,
    content TEXT,
    source TEXT,
    published_at TEXT,
    url TEXT UNIQUE,
    author TEXT
)""")

#create a stocks table
c.execute("""CREATE TABLE stocks (
    ticker TEXT PRIMARY KEY,
    company_name TEXT  
)  
""")

def insert_article(ticker, title, description, content, source, published_at, url, author):
    c.execute("INSERT INTO articles(ticker, title, description, content, source, published_at, url, author) VALUES(?, ?, ?, ?, ?, ?, ?, ?)",
              (ticker, title, description, content, source, published_at, url, author))

conn.commit()

conn.close()