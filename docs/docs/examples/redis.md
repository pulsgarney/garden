Redis Example
====

This example showcases how to interact with Redis using middlewares in Garden.

In the `Gardener` class, you specify the middlewares you wish to utilize. In this instance, we are employing the `RedisMiddleware` with configured connection details. Additionally, we establish two tasks: one for writing data to Redis (`Test Task - SET`) and another for retrieving the data (`Test Task - GET`).

When using `RedisMiddleware`, an object named `redis` will be mounted under each task's `objects` property. The `objects` are also accessible under the `Gardener` itself.

The `SET` task will execute repeatedly for five times. In each iteration, it sets a number to a list in Redis.

Subsequently, the `GET` task will run only once, with a one-second delay before it is triggered. This implies that by the time it runs, the `SET` task would have already completed writing data into Redis.

## Code

```python
# examples/use_redis.py

from garden import Gardener, Hedgehog
from garden.middlewares.redis import RedisMiddleware
from redis.asyncio import StrictRedis


class TestGardener(Gardener):
    '''
    TestGardener shows how to connect to Redis.
    '''

    middlewares = [
        RedisMiddleware.config(host='redis.me'),
    ]

    @Gardener.task('Test Task - SET', repeat=5)
    async def test_task(self, task: Hedgehog):
        r: StrictRedis = task.objects.redis
        await r.rpush('test', task.run_count + 1)
        task.log(f'test task executed: {task.run_count + 1}')

    @Gardener.task('Test Task - GET', repeat=False, delay=1)
    async def test_task(self, task: Hedgehog):
        r: StrictRedis = task.objects.redis
        result = await r.lrange('test', 0, -1)
        task.log(f'test task executed: {result}')


if __name__ == '__main__':
    TestGardener(name='TG').start()

```

## Output

```
> python examples/use_redis.py
2025-03-31 03:59:46 INFO::Hedgehog [Test Task - SET] created
2025-03-31 03:59:46 INFO::Hedgehog [Test Task - GET] created
2025-03-31 03:59:46 INFO::TestGardener [TG] initiated
2025-03-31 03:59:46 INFO::TestGardener [TG] preparing
2025-03-31 03:59:46 INFO::MiddlewareManager registering middlewares[RedisMiddleware]
2025-03-31 03:59:46 INFO::Middleware [redis] Redis initialized: 7.4.1
2025-03-31 03:59:46 INFO::TestGardener [TG] ready
2025-03-31 03:59:46 INFO::TestGardener [TG] running
2025-03-31 03:59:46 INFO::Hedgehog [Test Task - SET] running
2025-03-31 03:59:46 INFO::Hedgehog [Test Task - GET] running
2025-03-31 03:59:46 INFO::Hedgehog [Test Task - GET] paused
2025-03-31 03:59:46 INFO::Hedgehog [Test Task - GET] starting to run in 1.00 seconds
2025-03-31 03:59:46 INFO::Hedgehog [Test Task - SET] test task executed: 1
2025-03-31 03:59:46 INFO::Hedgehog [Test Task - SET] test task executed: 2
2025-03-31 03:59:46 INFO::Hedgehog [Test Task - SET] test task executed: 3
2025-03-31 03:59:46 INFO::Hedgehog [Test Task - SET] test task executed: 4
2025-03-31 03:59:46 INFO::Hedgehog [Test Task - SET] test task executed: 5
2025-03-31 03:59:46 INFO::Hedgehog [Test Task - SET] terminated
2025-03-31 03:59:47 INFO::Hedgehog [Test Task - GET] running
2025-03-31 03:59:47 INFO::Hedgehog [Test Task - GET] test task executed: [b'1', b'2', b'3', b'4', b'5']
2025-03-31 03:59:47 INFO::Hedgehog [Test Task - GET] terminated
2025-03-31 03:59:47 INFO::TestGardener [TG] stopped
2025-03-31 03:59:47 INFO::MiddlewareManager deregistering middlewares[RedisMiddleware]
2025-03-31 03:59:47 INFO::Middleware [redis] Redis connection closed
2025-03-31 03:59:47 INFO::TestGardener [TG] terminated
2025-03-31 03:59:47 INFO::TestGardener [TG] exited
```
