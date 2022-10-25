import inspect

import pytest
import logging
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait


@pytest.mark.usefixtures("setup")
class BaseClass:

    def getlogger(self):
        loggerName = inspect.stack()[1][3]
        logger = logging.getLogger(loggerName)

        filehandler = logging.FileHandler('logfile.log')
        formatter = logging.Formatter("%(asctime)s :  %(levelname)s : %(name)s : %(message)s")
        filehandler.setFormatter(formatter)
        logger.addHandler(filehandler)

        logger.setLevel(logging.INFO)
        return logger

    def verifyLinkPresence(self, text):
        wait = WebDriverWait(self.driver, 10).until(expected_conditions.presence_of_element_located((By.XPATH, text)))

    def selectOptionByText(self, locator, text):
        gender = Select(locator)
        gender.select_by_visible_text(text)
