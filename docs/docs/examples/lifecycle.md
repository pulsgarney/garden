Lifecycle Example
====

This example showcases how the overall lifecycle hooks operate within the Garden.

When you create a subclass of `Gardener` and define tasks using the decorator `@Gardener.task`, each time the `Gardener` is executed, it passes through specific hooks throughout the runtime processes.

At the very outset of a run, there will be a `pre_execution()` hook, and at the end, a `post_execution()` hook. You can utilize these hooks to carry out initializations, check statuses, prepare materials, and perform clean-up afterwards, amongst other things. These hooks can be either synchronous or asynchronous methods. Choose the approach that best suits your scenario.

Similarly, there are also a `before_each_run()` and a `after_each_run()` that can be used as hooks. These two will be executed before and after each task run respectively. You may use them to check various aspects, implement conditional delays, or change properties within the `Hedgehog`, and so on.

## Code

```python
# examples/lifecycle.py

from garden import Gardener, Hedgehog


class TestGardener(Gardener):
    '''
    TestGardener shows how lifecycle hooks work.
    '''

    @Gardener.task('Test Task', repeat=2)
    def test_task(self, task: Hedgehog):
        self.probe_into()
        task.log('test task executed 👌')

    def before_each_run(self, hedgehog: Hedgehog):
        # Called before each time task is executed
        self.log('before each run')

    def after_each_run(self, hedgehog: Hedgehog):
        # Called after each time task is executed
        self.log('after each run')

    def probe_into(self):
        # other functions that is not a task
        self.log('probe into')

    def pre_execution(self):
        # Called before everything is executed
        self.log('pre execution')

    def post_execution(self):
        # Called after everything is executed
        self.log('post execution')


if __name__ == '__main__':
    TestGardener(name='TG').start()

```

## Output

```
> python examples/lifecycle.py
2025-03-31 03:35:25 INFO::Hedgehog [Test Task] created
2025-03-31 03:35:25 INFO::TestGardener [TG] initiated
2025-03-31 03:35:25 INFO::TestGardener [TG] preparing
2025-03-31 03:35:25 INFO::TestGardener [TG] ready
2025-03-31 03:35:25 INFO::TestGardener [TG] pre execution
2025-03-31 03:35:25 INFO::TestGardener [TG] running
2025-03-31 03:35:25 INFO::Hedgehog [Test Task] running
2025-03-31 03:35:25 INFO::TestGardener [TG] before each run
2025-03-31 03:35:25 INFO::TestGardener [TG] probe into
2025-03-31 03:35:25 INFO::Hedgehog [Test Task] test task executed 👌
2025-03-31 03:35:25 INFO::TestGardener [TG] after each run
2025-03-31 03:35:25 INFO::TestGardener [TG] before each run
2025-03-31 03:35:25 INFO::TestGardener [TG] probe into
2025-03-31 03:35:25 INFO::Hedgehog [Test Task] test task executed 👌
2025-03-31 03:35:25 INFO::TestGardener [TG] after each run
2025-03-31 03:35:25 INFO::Hedgehog [Test Task] terminated
2025-03-31 03:35:25 INFO::TestGardener [TG] stopped
2025-03-31 03:35:25 INFO::TestGardener [TG] post execution
2025-03-31 03:35:25 INFO::TestGardener [TG] terminated
2025-03-31 03:35:25 INFO::TestGardener [TG] exited
```
