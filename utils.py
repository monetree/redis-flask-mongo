import redis
rds = redis.StrictRedis(port=6379, db=0)
#redis connection

import json


#redis custom class to store and retrive api data
class Red:
    def set(cache_key, api):
        #dumps is to convert json data to string because redis accept string data
        api = json.dumps(api)
        # syntax to store response first param is key and second is value
        rds.set(cache_key, api)
        # here is the expire time for cache data you can change the time(in seconds)
        rds.expire(cache_key, 432000)

    def get(cache_key):
        #check the key if exist
        cacheData = rds.get(cache_key)
        if cacheData:
            # as we stored api response in string format
            # we have to convert it into json data
            cacheData = cacheData.decode("utf-8")
            cacheData = cacheData.replace("'", "\"")
            cacheData = json.loads(cacheData)
            return cacheData
        else:
            # if key is not exist it will return None
            # so that we can again recheck our db for result
            return None