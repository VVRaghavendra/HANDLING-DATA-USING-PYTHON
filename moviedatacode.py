import sqlite3
conn = sqlite3.connect('movies.db')
c=conn.cursor()
#c.execute("""CREATE TABLE movies(
    #            name text,
   #             actor text,
   #             actress text,
  #              director text,
 #               yearofrelease integer
                
 #               )""")
#c.execute("INSERT INTO movies VALUES ('helllo','Ram','seetha','vyas','1789')")
#c.execute("INSERT INTO movies VALUES ('krishna','Ravi','priya','sreenu','1990')")
#c.execute("INSERT INTO movies VALUES ('time','prabhu','rajini','Raja','2010')")
#c.execute("INSERT INTO movies VALUES ('dream','Rasool','sheela','varun','2011')")
#c.execute("INSERT INTO movies VALUES ('success','narayan','laxmi','mouli','2020')")
c.execute("SELECT * FROM movies")
print(c.fetchall())
print("the next line is with parameters")
c.execute("SELECT * FROM movies WHERE actor = 'Ravi'")
print(c.fetchone())

conn.commit()
conn.close()
 
