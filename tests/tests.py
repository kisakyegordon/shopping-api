import unittest

class TestApi(unittest.TestCase):
    def setUp(self):
        self.test_user_name = 'testuser'
        self.test_user_password = '12334test'


    def create_user(self, name, password):
        # url =
        data = {'name': name, 'password': password}
        response = self.test_client_post(url, headers=self.get_accept_content_type_headers(), data=json,dumps(data))
        return response