from flask import Flask
from flask_pymongo import PyMongo
from utils import Red

app = Flask(__name__)
#mongo db databse connection
# here dummy is my databse name
app.config["MONGO_URI"] = "mongodb://localhost:27017/dummy"
mongo = PyMongo(app)

@app.route("/")
def home_page():
    # Here i added default cache key for redis data
    # cache key will be redis key and api rsult will be value
    # as redis supports data in key value foemat
    cache_key = "default_cache_key"
    cache_data = Red.get(cache_key)
    if cache_data:
        return cache_data
    
    # I just added loop to make query multiple times same thing
    # In real life senario we will have to grab data from multiple collection and
    # have to do calculations on top of that
    # so i just added some loop by looking into real world senario

    loop = 100000
    for i in range(loop):
        comments = mongo.db.comments.find({}, {"_id": 0})
    emails = []
    names = []
    post_ids = []
    data = [i for i in comments]

    for i in comments:
        emails.append(i["email"])
        names.append(i["name"])
        post_ids.append(i["postId"])

    api = {
        "email_count": len(emails),
        "names": len(names),
        "post_ids": len(post_ids),
        "data": data[:10]
    }
    
    # finally after all calculations done
    # i am storing the data do redis db with out key
    # so that the next time when user will come it will
    # find the key in redis db hence it will return
    # instead of coming here
    Red.set(cache_key, api)
    return api

if __name__ == '__main__':
    app.run(port=5000, debug=True)