from rq import Worker, Queue, Connection
import redis
import os
from decouple import config

redis_url = 'redis://localhost:6379'
conn = redis.from_url(redis_url)

if __name__ == '__main__':
    with Connection(conn):
        worker = Worker(map(Queue))
        worker.work()


redis_url = config('REDIS_URL', 'redis://localhost:6379')
conn = redis.from_url(redis_url)

if __name__ == '__main__':
    queues = [Queue('default')]

    with Connection(conn):
        worker = Worker(queues)
        print("Worker is starting...")
        worker.work()
