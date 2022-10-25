from selenium.webdriver.common.by import By


class CheckoutPage:

    def __init__(self, driver):
        self.driver = driver

    allphones = (By.XPATH, "//div[@class='card h-100']")
    phonename = (By.XPATH, "//div[@class='card h-100']//div/h4/a")
    addcart = (By.XPATH, "div/button")
    primarybtn = (By.XPATH, "//a[@class='nav-link btn btn-primary']")
    successbtn = (By.XPATH, "//button[@class='btn btn-success']")

    def getCardTitle(self):
        return self.driver.find_elements(*CheckoutPage.allphones)

    def phoneName(self):
        return self.driver.find_element(*CheckoutPage.phonename)

    def addCart(self):
        return self.driver.find_element(*CheckoutPage.addcart)

    def primaryBtn(self):
        return self.driver.find_element(*CheckoutPage.primarybtn)

    def successBtn(self):
        return self.driver.find_element(*CheckoutPage.successbtn)
