import pymongo

URI = "mongodb://chatbot:BmPspGbuVgdG@103.113.83.201:27017/?authSource=ChatBotDB&readPreference=primary"
DBNAME = "ChatBotDB"

myclient = pymongo.MongoClient(URI)
database = myclient[DBNAME]

news = database["news"].find({},{"Domain" : 1, "Category" : 1, "Title" : 1, "Url" : 1, "Content" : 1, "_id" : 0})



