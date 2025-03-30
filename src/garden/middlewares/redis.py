from ..decorator import chainable
from ..middleware import MiddlewareBase


class RedisMiddleware(MiddlewareBase):
    '''
    RedisMiddleware - middleware for connecting to Redis.
    '''

    name = 'redis'
    dependencies = ['redis']

    _config: dict[str, int | str | None] = {}

    @classmethod
    def config(
        cls, *, host: str = 'localhost', port: int = 6379, **kwargs
    ) -> type['RedisMiddleware']:
        cls._config = {'host': host, 'port': port, **kwargs}

        return cls

    @chainable
    async def create(self) -> 'RedisMiddleware':
        try:
            import redis.asyncio as redis
        except ImportError:
            self.log('Redis package not found, please install it')
        else:
            self._client: redis.StrictRedis = await redis.StrictRedis(
                **self._config
            )

            self.bind_object(RedisMiddleware.name, self._client)

            info = await self._client.info()
            version = info.get('redis_version', 'unknown')

            self.log(f'Redis initialized: {version}')

    @chainable
    async def destroy(self) -> 'RedisMiddleware':
        await self._client.aclose()

        self.log('Redis connection closed')
