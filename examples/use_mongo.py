from garden import Gardener, Hedgehog
from garden.middlewares.mongo import MongoMiddleware
from pymongo import AsyncMongoClient


class TestGardener(Gardener):
    '''
    TestGardener shows how to connect to MongoDB.
    '''

    middlewares = [
        MongoMiddleware.config(
            host='mongo.me', port=27017, username='test', password='p@ss'
        ),
    ]

    @Gardener.task('Test Task', repeat=False)
    async def test_task(self, task: Hedgehog):
        mongo: AsyncMongoClient = task.objects.mongo
        names = await mongo.list_database_names()
        task.log(f'test task executed: {names}')


if __name__ == '__main__':
    TestGardener(name='TG').start()
