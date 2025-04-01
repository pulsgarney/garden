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
