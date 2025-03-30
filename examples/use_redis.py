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
