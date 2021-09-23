import unittest


class BasicTestCase(unittest.TestCase):
    _app = ''

    def __init__(self, app) -> None:
        self._app = app

    def setUp(self):
        self._app = self._app.test_client()

    def test_page_by_route(self, route):
        response = self._app.get(route, content_type='html/text')
        code = response.status_code
        if code == 200:
            return f"Test passed: {code}"
        return "Test failed"
