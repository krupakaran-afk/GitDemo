import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from Utilities.baseClass import BaseClass
from pageObjects.CheckoutPage import CheckoutPage
from pageObjects.ConfirmPage import ConfirmPage
from pageObjects.HomePage import HomePage


class TestOne(BaseClass):

    def test_e2e(self):
        log = self.getlogger()
        phonenames = []
        homePage = HomePage(self.driver)
        homePage.shopItems().click()
        log.info("Getting all the shop items")
        checkoutPage = CheckoutPage(self.driver)
        phones = checkoutPage.getCardTitle()
        print(phones)
        for ele in phones:
            phonenames = checkoutPage.phoneName().text
            if phonenames == "Blackberry":
                ele.checkoutPage.addCart().click()
        log.info(phonenames)

        checkoutPage.primaryBtn().click()
        checkoutPage.successBtn().click()
        self.driver.implicitly_wait(2)

        confirmpage = ConfirmPage(self.driver)

        confirmpage.inputCountry().send_keys("India")
        log.info("Entering country name as India")
        #wait = WebDriverWait(self.driver, 10)
        #wait.until(expected_conditions.presence_of_element_located(confirmpage.containCountry()))
        self.verifyLinkPresence("//a[contains(text(),'India')]")
        confirmpage.containCountry().click()
        confirmpage.checkOutBox().click()
        confirmpage.clickSubmit().click()
        successText = confirmpage.alertMessage().text
        log.info("Text received from application is "+successText)

        assert "Succ" in successText
