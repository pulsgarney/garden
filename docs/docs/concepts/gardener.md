Gardener
====

The Gardener acts as the director and frontman of the Garden. It orchestrates the execution of tasks, manages various lifecycle hooks, and serves as the entry point to the Garden's functionality.

In general, Garden is better suited for small-scale applications or projects where there are only a few tasks to manage. We do not recommend using Garden for large-scale applications, projects that demand complex task management or task dependency trees. Although the same effect can be achieved through some elaborate setup and code organization, it is not worth the effort.

## Basic Usage

To write a Gardener class, you need to subclass `Gardener` and define your tasks using the `@Gardener.task` decorator. Each task is executed independently by the Gardener.

```python
# example.py

from garden import Gardener, Hedgehog


class TestGardener(Gardener):

    @Gardener.task('Test', repeat=False)
    async def test_task(self, task: Hedgehog):
        task.log('test task executed 👌')


if __name__ == '__main__':
    TestGardener(name='TG').start()

```

*NOTE: See [Tasks](/garden/concepts/tasks/) for more details on how to define and manage tasks.*

## Lifecycle

The Gardener also provides methods for managing the lifecycle of tasks, such as `pre_execution`, `post_execution`, `before_each_run`, and `after_each_run`.

*NOTE: See [Lifecycle](/garden/examples/lifecycle/) for more details on how to manage task lifecycles, and [Lifecycle](/garden/references/lifecycle/) for more information on execution orders.*

## Middlewares

In order to cut down on code duplication within utility functions for utilities, we can define common utility functions in middlewares and use them across different tasks. Middlewares are all self-registered upon being imported. However, for a more optimal practice, it is advisable to register the middlewares explicitly as follows:

```python
# example.py

from garden import Gardener, Hedgehog
from garden.middlewares.example import SomeMiddleware

class TestGardener(Gardener):

    middlewares = [
        SomeMiddleware.config(foo='bar'),
    ]

    @Gardener.task('Test', repeat=False)
    async def test_task(self, task: Hedgehog):
        task.log('test task executed 👌')

```

Once the middleware has been registered, it can be accessed via the `objects` attribute of either the `Hedgehog` instance or the `Gardener` instance itself. For further details and more information, refer to the examples section.

## Status

The Gardener class possesses a set of statuses which signify various stages in its lifecycle. It establishes connections with different components. Once the tasks start, it will oversee the status of each task and update the status accordingly.

```python
# garden.py

class GardenerStatus(Enum):
    '''
    GardenerStatus is an enumeration of the possible states of a Gardener.

    - INITIATED: Gardener has been initialized.
    - PREPARING: Gardener is preparing for the necessary configurations.
    - READY: Gardener is ready to run.
    - RUNNING: Gardener is running.
    - PAUSED: Gardener is paused by the user or a signal.
    - SUSPENDED: Gardener is suspended by the program.
    - STOPPED: Gardener is preparing to be terminated.
    - TERMINATED: Gardener has been terminated.
    '''

    INITIATED = 'INITIATED'
    PREPARING = 'PREPARING'
    READY = 'READY'
    RUNNING = 'RUNNING'
    PAUSED = 'PAUSED'
    SUSPENDED = 'SUSPENDED'
    STOPPED = 'STOPPED'
    TERMINATED = 'TERMINATED'

```

*NOTE: Refer to [Lifecycle](/garden/references/lifecycle/) for more information on how different states are behaved and managed in runtime.*
