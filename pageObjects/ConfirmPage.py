from selenium.webdriver.common.by import By


class ConfirmPage:

    def __init__(self, driver):
        self.driver = driver

    inputcountry = (By.XPATH, "//input[@type='text']")
    containcountry = (By.XPATH, "//a[contains(text(),'India')]")
    clicksubmit = (By.XPATH, "//input[@type='submit']")
    checkoutbox = (By.XPATH, "//div[@class='checkbox checkbox-primary']")
    clicksubmitA = (By.CSS_SELECTOR, "[type='submit']")
    alertmessage = (By.CLASS_NAME, "alert-success")

    def inputCountry(self):
        return self.driver.find_element(*ConfirmPage.inputcountry)

    def containCountry(self):
        return self.driver.find_element(*ConfirmPage.containcountry)

    def clickSubmit(self):
        return self.driver.find_element(*ConfirmPage.clicksubmitA)

    def checkOutBox(self):
        return self.driver.find_element(*ConfirmPage.checkoutbox)

    def alertMessage(self):
        return self.driver.find_element(*ConfirmPage.alertmessage)
