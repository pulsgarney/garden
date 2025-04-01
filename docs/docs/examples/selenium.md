Selenium Example
====

This example showcases how to interact with Selenium using middlewares in Garden.

In the `Gardener` class, you specify the middlewares you wish to utilize. In this instance, we are employing the `SeleniumMiddleware` with configured details. Moreover, we set up a task to perform some simple website crawling for us.

With the `SeleniumMiddleware.config` method, you can leverage most of the code snippets required for nearly every Selenium project when setting up for web scraping, while maintaining the most flexible customization capabilities.

You can select your own webdriver and browser location to use, determine whether you need to see the browser window or keep it headless if running on a server without a desktop. You can define which proxy or user agent options to use, as well as webdriver startup option settings, stealth options, and more.

When using `SeleniumMiddleware`, a context manager method named `selenium` will be mounted under each task's `objects` property. The `objects` are also accessible under the `Gardener` itself.

With each function call, it returns a browser session. You can place your scraping logics within the context, and it will handle the creation and clean-up actions for Selenium for you.

## Code

```python
# examples/use_selenium.py

from garden import Gardener, Hedgehog
from garden.middlewares.selenium import SeleniumMiddleware
from selenium import webdriver


class TestGardener(Gardener):
    '''
    TestGardener shows how to use Selenium.
    '''

    middlewares = [
        SeleniumMiddleware.config(
            headless=False,
            proxy=None,
            binary_location='./Google Chrome for Testing',
            webdriver_location='./chromedriver',
            option_arguments=['blink-settings=imagesEnabled=true'],
        ),
    ]

    @Gardener.task('Test Task', repeat=False)
    async def test_task(self, task: Hedgehog):
        session: webdriver.Chrome

        url = 'https://github.com/'
        js = 'return document.getElementsByName("description")[0].content'

        with task.objects.selenium() as session:
            session.get(url)
            session.implicitly_wait(5)
            session.get_screenshot_as_file('screenshot.png')

            description = session.execute_script(js)
            task.log(f'description: {description}')

        task.log('test task executed 👌')


if __name__ == '__main__':
    TestGardener(name='TG').start()

```

## Output

```log
> python examples/use_selenium.py
2025-04-01 07:22:09 INFO::Hedgehog [Test Task] created
2025-04-01 07:22:09 INFO::TestGardener [TG] initiated
2025-04-01 07:22:09 INFO::TestGardener [TG] preparing
2025-04-01 07:22:09 INFO::MiddlewareManager registering middlewares[SeleniumMiddleware]
2025-04-01 07:22:09 INFO::TestGardener [TG] ready
2025-04-01 07:22:09 INFO::TestGardener [TG] running
2025-04-01 07:22:09 INFO::Hedgehog [Test Task] running
2025-04-01 07:22:10 INFO::Middleware [selenium] Selenium session initialized
2025-04-01 07:22:12 INFO::Hedgehog [Test Task] description: GitHub is where people build software. More than 150 million people use GitHub to discover, fork, and contribute to over 420 million projects.
2025-04-01 07:22:12 INFO::Middleware [selenium] Selenium session closed
2025-04-01 07:22:12 INFO::Hedgehog [Test Task] test task executed 👌
2025-04-01 07:22:12 INFO::Hedgehog [Test Task] terminated
2025-04-01 07:22:12 INFO::TestGardener [TG] stopped
2025-04-01 07:22:12 INFO::MiddlewareManager deregistering middlewares[SeleniumMiddleware]
2025-04-01 07:22:12 INFO::TestGardener [TG] terminated
2025-04-01 07:22:12 INFO::TestGardener [TG] exited
```
