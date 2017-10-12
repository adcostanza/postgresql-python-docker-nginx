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
db = DB()
db.createTable()