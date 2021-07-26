from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from config import board_name


class TrelloPage:
    # Trello Page
    div_header_id = "header"
    button_boards_header_xpath = "//button[@data-test-id='header-boards-menu-button']"
    div_board_xpath = "//div[@title='" + board_name + "']"

    def __init__(self, driver):
        self.driver = driver

    def waitVisibilityHeader(self):
        try:
            myElem = WebDriverWait(self.driver, 15).until(EC.presence_of_element_located((By.ID, self.div_header_id)))
            print
            "Header Found"
        except TimeoutException:
            print
            "Header not found"

    def clickBoard(self):
        self.driver.find_element_by_xpath(self.div_board_xpath).click()
