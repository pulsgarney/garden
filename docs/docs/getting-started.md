First step
====

## Installation

### PyPI

```sh
pip install garden
```

### Source

For development, you can also install it in editable mode like this:

```sh
pip install -e <path/url>
```

## Your first task

This represents the fundamental usage of Garden. By subclassing the `Gardener` class and defining your tasks as methods, you are able to create a new task. Subsequently, you can initiate the task by invoking the `start` method.

```python
# example.py

from garden import Gardener


class TestGardener(Gardener):

    @Gardener.task('Test', repeat=False)
    async def test_task(task):
        task.log('test task executed 👌')


if __name__ == '__main__':
    TestGardener(name='TG').start()

```

Execute it in the same manner as any typical Python script.

```sh
python example.py
```

## How to debug

In case you wish to run the service in debug mode, you can enable it like this:

```python
# rest of the code

if __name__ == '__main__':
    TestGardener(name='TG').enable_debug().start()
```

Both the `Gardener` and `Hedgehog` instances have the methods to enable or disable debug mode. This is particularly useful for logging detailed information during development.

The key difference between enabling and disabling debug mode is that when it's enabled, when an exception occurs, it will print the traceback stack and the error message, which is helpful for debugging purposes. But when it's disabled, it only logs the error message without the traceback stack.

```python
# to enable debug mode
Gardener().enable_debug().start()

(task: Hedgehog).enable_debug()


# to disable debug mode
Gardener().disable_debug().start()

(task: Hedgehog).disable_debug()

```
