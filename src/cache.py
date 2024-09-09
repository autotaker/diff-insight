import json
from typing import Any, Callable
import logging

logger = logging.getLogger(__name__)


class Cache:
    cache_dir: str = "cache"

    def __init__(self, cache_dir: str = "cache"):
        self.cache_dir = cache_dir

    def get(self, key: str) -> Any:
        """
        Get the value from the cache for the given key.

        :param key: The key to retrieve the value for
        :return: The value from the cache
        """
        try:
            with open(f"{self.cache_dir}/{key}.json", "r") as file:
                return json.load(file)
        except FileNotFoundError:
            return None

    def set(self, key: str, value: Any) -> None:
        """
        Set the value in the cache for the given key.

        :param key: The key to set the value for
        :param value: The value to store in the cache
        """
        with open(f"{self.cache_dir}/{key}.json", "w") as file:
            json.dump(value, file)

    def with_cache(self, key: str, callback: Callable[..., Any], *args: Any) -> Any:
        """
        Get the value from the cache for the given key, or call the callback to set it.

        :param key: The key to retrieve or set the value for
        :param callback: The callback to call if the value is not found in the cache
        :return: The value from the cache or the result of the callback
        """
        value = self.get(key)
        if value is None:
            logger.debug(f"Cache miss for key: {key}")
            value = callback(*args)
            logger.info(f"Setting cache for key: {key}")
            self.set(key, value)
        else:
            logger.debug(f"Cache hit for key: {key}")
        return value
