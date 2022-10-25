from selenium.webdriver.common.by import By


class HomePage:
    def __init__(self, driver):
        self.driver = driver

    shop = (By.XPATH, "//a[contains(@href, 'shop')]")
    name = (By.XPATH, "//input[contains(@minlength,'2')]")
    email = (By.XPATH, "//input[@name = 'email']")
    password = (By.XPATH, "//input[@id= 'exampleInputPassword1']")
    checkbox = (By.XPATH, "//input[@id= 'exampleCheck1']")
    dropdown = (By.ID, "exampleFormControlSelect1")
    radiobutton = (By.XPATH, "//input[@id= 'inlineRadio1']")
    dateofbirth = (By.XPATH, "//input[@name= 'bday']")
    submit = (By.XPATH, "//input[@class= 'btn btn-success']")
    success = (By.CLASS_NAME, "alert-success")

    def shopItems(self):
        return self.driver.find_element(*HomePage.shop)

    def getName(self):
        return self.driver.find_element(*HomePage.name)

    def getEmail(self):
        return self.driver.find_element(*HomePage.email)

    def getPassword(self):
        return self.driver.find_element(*HomePage.password)

    def checkBox(self):
        return self.driver.find_element(*HomePage.checkbox)

    def dropDown(self):
        return self.driver.find_element(*HomePage.dropdown)

    def radioButton(self):
        return self.driver.find_element(*HomePage.radiobutton)

    def dateOfBirth(self):
        return self.driver.find_element(*HomePage.dateofbirth)

    def submitBtn(self):
        return self.driver.find_element(*HomePage.submit)

    def successBanner(self):
        return self.driver.find_element(*HomePage.success)