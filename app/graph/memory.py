import redis
import json
from app.config import settings

r = redis.Redis.from_url(settings.REDIS_URL,decode_responses=True)

def get_memory(session_id):
    data = r.get(session_id)

    if data :
         return json.loads(data)

    return []
def save_memory(session_id, history):
    r.set(session_id, json.dumps(history))