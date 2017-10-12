CREATE TABLE Posts (id serial PRIMARY KEY,
						link varchar,
						_like integer,
						_time timestamp DEFAULT now())