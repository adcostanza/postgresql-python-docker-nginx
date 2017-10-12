import psycopg2
class DB:
	def __init__(self):
			self.conn = psycopg2.connect("dbname='postgres' user='postgres' host='db' password='pass'")
			
			print('Connected to database')
		
	
	def createTable(self):
		cur = self.conn.cursor()
		cur.execute("""CREATE TABLE Posts (\
						id serial PRIMARY KEY,\
						link varchar,\
						_like integer,\
						_time timestamp DEFAULT now())""")
		cur.execute("""CREATE TABLE tags (\
						id serial PRIMARY KEY,\
						tag varchar,\
						_time timestamp DEFAULT now())""")
		self.conn.commit()
		print("Table created")
	def addPost(self,link,like):
		
		cur = self.conn.cursor()
		cur.execute("""INSERT INTO Posts (link, _like) VALUES (%s, %s)""",(link,like))
		self.conn.commit()
		print("Inserted into posts", link)
	def getAllLinks(self):
		cur = self.conn.cursor()
		cur.execute("""SELECT link FROM Posts""")
		posts = cur.fetchall()
		self.conn.commit()
		#print(posts)
		return(posts)
#db.createTable()