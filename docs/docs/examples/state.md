State Example
====

This example showcases how to interact with in-memory shared state using middlewares in Garden.

In the `Gardener` class, you specify the middlewares you wish to utilize. In this instance, we are employing the `StateMiddleware` with configured details. Additionally, two tasks are set up to perform some basic usage of shared states. 

When using `StateMiddleware`, an object named `state` will be mounted under each task's `objects` property. The `objects` are also accessible under the `Gardener` itself.

In this example, one task is configured to set up a listener to the system that monitors state changes. Another task reads and writes the state simultaneously. This task is set to run 20 times repeatedly with 500 replicas of itself. With each run, it increments the `count` number by one. Thus, in the end, a total of 10000 counts is expected.

The `StateMiddleware.config` method can take two parameters. One is for setting up the initial state when the program runs, and the other is for specifying a path to a JSON file to store the runtime state. If the file path exists, it will attempt to load it when the `Gardener` starts. When it shuts down, it saves all the state into that file. In this way, you can have the runtime state persistent across different runs without introducing a database or a store.

*NOTE: Since it's in JSON format, you cannot save reference objects in a loop or anything that cannot be stringified as a JSON string.*

## Code

```python
# examples/use_state.py

from garden import Gardener, Hedgehog
from garden.middlewares.state import StateMiddleware, State


def my_listener(state):
    print(f'State changed to {state}')


class TestGardener(Gardener):
    '''
    TestGardener shows how to use shared state.
    '''

    middlewares = [
        StateMiddleware.config(
            initial_state={'count': 0}, state_file='./state.json'
        ),
    ]

    @Gardener.task('Test Task - Count', repeat=20, replica=500, delay=1)
    async def test_task(self, task: Hedgehog):
        state: State = task.objects.state
        count = state.get_state().get('count')
        state.set_state({'count': count + 1})

    @Gardener.task('Test Task - Listener', repeat=False)
    async def test_task(self, task: Hedgehog):
        task.objects.state.add_listener(my_listener)


if __name__ == '__main__':
    TestGardener(name='TG').start()

```

## Output

```log
> python examples/use_state.py
2025-04-01 07:51:52 INFO::Hedgehog [Test Task - Count [replica:1]] created
2025-04-01 07:51:52 INFO::Hedgehog [Test Task - Count [replica:2]] created
2025-04-01 07:51:52 INFO::Hedgehog [Test Task - Count [replica:3]] created
            ...
State changed to {'count': 9998}
State changed to {'count': 9999}
State changed to {'count': 10000}
            ...
2025-04-01 07:51:53 INFO::Hedgehog [Test Task - Count [replica:499]] terminated
2025-04-01 07:51:53 INFO::Hedgehog [Test Task - Count [replica:500]] terminated
2025-04-01 07:51:54 INFO::TestGardener [TG] stopped
2025-04-01 07:51:54 INFO::MiddlewareManager deregistering middlewares[StateMiddleware]
2025-04-01 07:51:54 INFO::State state saved to file: ./state.json
2025-04-01 07:51:54 INFO::TestGardener [TG] terminated
2025-04-01 07:51:54 INFO::TestGardener [TG] exited
```

*NOTE: Log content has been trim down to save space.*
