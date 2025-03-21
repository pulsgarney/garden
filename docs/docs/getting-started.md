First step
====

## Installation

### Install from pypi

```sh
pip install garden
```

### Install from source

```sh
pip install -e <project path / url>
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