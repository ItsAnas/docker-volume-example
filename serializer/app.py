import time

import redis
from flask import Flask
from subprocess import Popen, PIPE

app = Flask(__name__)
cache = redis.Redis(host='redis', port=6379)

def get_hit_count():
    retries = 5
    while True:
        try:
            return cache.incr('hits')
        except redis.exceptions.ConnectionError as exc:
            if retries == 0:
                raise exc
            retries -= 1
            time.sleep(0.5)


@app.route('/')
def hello():
    s = "not found"
    try:
        g = open("/usr/share/toast/demofile2.txt", "r")
        s = g.read()
    except:
        pass
    #return HttpResponse(output)
    return s