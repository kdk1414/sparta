from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.dbsparta

some_movie = db.movies.find_one({'title':'월-E'})
star_movie = some_movie['star']
print(star_movie)

