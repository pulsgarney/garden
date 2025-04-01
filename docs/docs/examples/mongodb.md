MongoDB Example
====

This example showcases how to interact with MongoDB using middlewares in Garden.

In the `Gardener` class, you specify the middlewares you wish to utilize. In this instance, we are employing the `MongoMiddleware` with configured connection details. Additionally, we defined a task to obtain all the database names in MongoDB.

When using `MongoMiddleware`, an object named `mongo` will be mounted under each task's `objects` property. The `objects` are also accessible under the `Gardener` itself.

## Code

```python
# examples/use_mongo.py

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

```

*NOTE: For any parameters in the form of key-value pairs that you wish to pass to the initiation of the MongoDB client, you can pass them as keyword arguments to the `config` method of `MongoMiddleware`.*

## Output

```log
> python examples/use_mongo.py
2025-04-01 06:47:01 INFO::Hedgehog [Test Task] created
2025-04-01 06:47:01 INFO::TestGardener [TG] initiated
2025-04-01 06:47:01 INFO::TestGardener [TG] preparing
2025-04-01 06:47:01 INFO::MiddlewareManager registering middlewares[MongoMiddleware]
2025-04-01 06:47:01 INFO::Middleware [mongo] Mongo initialized: 8.0.3
2025-04-01 06:47:01 INFO::TestGardener [TG] ready
2025-04-01 06:47:01 INFO::TestGardener [TG] running
2025-04-01 06:47:01 INFO::Hedgehog [Test Task] running
2025-04-01 06:47:01 INFO::Hedgehog [Test Task] test task executed: ['admin', 'config', 'local', 'test']
2025-04-01 06:47:01 INFO::Hedgehog [Test Task] terminated
2025-04-01 06:47:02 INFO::TestGardener [TG] stopped
2025-04-01 06:47:02 INFO::MiddlewareManager deregistering middlewares[MongoMiddleware]
2025-04-01 06:47:02 INFO::Middleware [mongo] Mongo connection closed
2025-04-01 06:47:02 INFO::TestGardener [TG] terminated
2025-04-01 06:47:02 INFO::TestGardener [TG] exited
```
