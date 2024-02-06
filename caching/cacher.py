import json
from typing import Dict, Optional

import redis

import config

conf = config.get_config()

redis = redis.Redis(host=conf["redis"]["host"], port=conf["redis"]["port"], db=conf["redis"]["db"],
                    password=conf["redis"]["password"])


def cache_response(key: str, data: Dict, ttl: Optional[int] = 10) -> None:
    json_data = json.dumps(data)
    redis.set(key, json_data, ex=ttl)


def get_response(key: str) -> Optional[Dict]:
    cached_data = redis.get(key)
    if cached_data:
        return json.loads(cached_data)
    return None
