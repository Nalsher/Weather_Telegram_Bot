import redis

def redis_conn():
    rclient = redis.Redis(host='localhost', port=6379, db=0)
    return rclient
def redis_end():
    rcon = redis_conn()
    return rcon.close()
def redis_work(name,value):
    rd = redis_conn()
    rd.set(name=name,value=value)
    rcon = redis_end()

