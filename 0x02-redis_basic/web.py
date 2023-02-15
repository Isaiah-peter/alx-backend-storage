#!/usr/bin/env python3
"""   implement a get_page function (prototype:
 def get_page(url: str) -> str:).
 The core of the function is very simple.
 It uses the requests module to obtain
   the HTML content of a particular URL and returns it. """
import redis
import requests
r = redis.Redis()
count = 0


def get_page(url: str) -> str:
    """ track how many times a particular URL was accessed in the key
        "count:{url}"
        and cache the result with an expiration time of 10 seconds """
    r.set(f"cached:{url}", count)
    resp = requests.get(url)
    r.incr(f"count:{url}")
    r.setex(f"cached:{url}", 10, r.get(f"cached:{url}"))
    return resp.text


if __name__ == "__main__":
    get_page('http://slowwly.robertomurray.co.uk')
