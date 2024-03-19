import redis


def redis_conn():
    rclient = redis.Redis(host='localhost', port=6379, db=0,decode_responses=True,charset='utf-8')
    return rclient
def redis_work(name,value):
    rd = redis_conn()
    rd.set(name=name,value=value)
    rd.close()
def redis_get(name):
    rd = redis_conn()
    abc = rd.get(name=name)
    rd.close()
    return abc