
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC, wait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

from utils.methods import wait_for_the_attribute_value


class TrelloBoard:
    # Trello Board
    a_list_cards_xpath = "//a[contains(@class, 'list-card js-member-droppable')]"
    div_comment_icon_xpath = "//div[@class='badge']"
    textarea_new_comment_xpath = "//div[@class='comment-frame']//div[@class='comment-box']//textarea"
    input_save_comment_xpath = "//div[@class='comment-frame']//div[@class='comment-box']//div[" \
                               "@class='comment-controls u-clearfix']//input "
    p_comment_xpath = "//div[@class='current-comment js-friendly-links js-open-card']//p"
    div_done_xpath = "//div[@class='js-list list-wrapper'][3]"
    a_element_card_done_list_xpath = "//div[@class='js-list list-wrapper'][3]//a[@class='list-card js-member-droppable ui-droppable']"
    a_element_card_to_do_list_xpath = "//div[@class='list js-list-content'][1]//div[2]//a[2]"
    a_element_class_attribute_to_be = "list-card js-member-droppable ui-droppable active-card"
    button_record_xpath = "//div[@role='presentation']//button"

    def __init__(self, driver):
        self.driver = driver

    def getCards(self):
        elements = self.driver.find_elements_by_xpath(self.a_list_cards_xpath)
        return elements

    def getCommentIcon(self):
        element = self.driver.find_element_by_xpath(self.div_comment_icon_xpath)
        if element.is_displayed():
            return True
        else:
            return False

    def setNewComment(self, newComment):
        self.driver.find_element_by_xpath(self.textarea_new_comment_xpath).clear()
        self.driver.find_element_by_xpath(self.textarea_new_comment_xpath).send_keys(newComment)

    def clickCommentIcon(self):
        WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located((By.XPATH, self.button_record_xpath)))
        self.driver.find_element_by_xpath(self.div_comment_icon_xpath).click()

    def clickSaveComment(self):
        self.driver.find_element_by_xpath(self.input_save_comment_xpath).click()

    def dragAndDropToDone(self):
        action = ActionChains(self.driver)
        WebDriverWait(self.driver, 15).until(
            EC.presence_of_element_located((By.XPATH, self.button_record_xpath)))
        source = self.driver.find_element_by_xpath(self.div_comment_icon_xpath)
        target = self.driver.find_element_by_xpath(self.div_done_xpath)
        action.drag_and_drop(source, target).perform()

    def getCommentsBoxes(self):
        elements = self.driver.find_elements_by_xpath(self.p_comment_xpath)
        return elements

    def cardExistInDoneList(self):
        return self.driver.find_element_by_xpath(self.a_element_card_done_list_xpath).is_displayed()
