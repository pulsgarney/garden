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
