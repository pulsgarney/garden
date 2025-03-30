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
