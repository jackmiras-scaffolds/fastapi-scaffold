from redis import Redis

from configs.env import env

"""
---------------------------------------------------------------------------
Redis Databases
--------------------------------------------------------------------------

Redis is an in-memory data structure store, used as a distributed, in-memory
key–value database, cache and message broker, with optional durability. Redis
supports different kinds of abstract data structures, such as strings, lists,
maps, sets, sorted sets, HyperLogLogs, bitmaps, streams, and spatial indices.

"""

if env("CACHE_CONNECTION") == "redis":
    cache = Redis(
        host=env("CACHE_HOST", "localhost"),
        port=env("CACHE_PORT", 6379),
        username=env("CACHE_USERNAME", None),
        password=env("CACHE_PASSWORD", None),
        db=env("CACHE_DB", "1"),
        decode_responses=env("CACHE_DECODE_RESPONSES", True),
    )

"""
---------------------------------------------------------------------------
Memcached Databases
--------------------------------------------------------------------------

Memcached is a general-purpose distributed memory-caching system. It is often
used to speed up dynamic database-driven websites by caching data and objects
in RAM to reduce the number of times an external data source must be read.
Memcached is free and open-source software, licensed under the Revised BSD
license.

"""

if env("CACHE_CONNECTION") == "memcached":
    pass
