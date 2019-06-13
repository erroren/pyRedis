import redis
db = redis.StrictRedis(db=0, host="192.168.12.155", port=6379)
res = db.set("name", "wuchen")
print(res)
res1 = db.get("name")
print(res1)
