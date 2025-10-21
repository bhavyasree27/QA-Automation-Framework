from framework.base.base_test import BaseTest

class TestLogin(BaseTest):
    def test_valid_login(self):
        self.driver.get("https://example.com/login")
        self.driver.find_element("id", "username").send_keys("admin")
        self.driver.find_element("id", "password").send_keys("password123")
        self.driver.find_element("id", "login").click()
        assert "Dashboard" in self.driver.title
