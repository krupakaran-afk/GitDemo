import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from Utilities.baseClass import BaseClass
from pageObjects.HomePage import HomePage
from testData.HomePageData import HomePageData


class TestHomePage(BaseClass):

    def test_FormSubmission(self, getData):
        homePage = HomePage(self.driver)
        homePage.getName().send_keys("name")
        homePage.getEmail().send_keys("email")
        homePage.getPassword().send_keys("gender")
        homePage.checkBox().click()
        self.selectOptionByText(homePage.dropDown(), "Male")
        homePage.radioButton().click()
        homePage.submitBtn().click()
        alertText = homePage.successBanner().text

        assert "Success" in alertText
        self.driver.refresh()

    @pytest.fixture(params=HomePageData.getTestData("Testcase2"))
    def getData(self, request):
        return request.param
