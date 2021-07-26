import pytest
from assertpy.assertpy import assert_that
from pageObjects.LoginPage import LoginPage
from pageObjects.TrelloPage import TrelloPage
from pageObjects.TrelloBoard import TrelloBoard
from config import baseURL, username, password
from utils.customLogger import LogGen


class Test_UI:
    logger = LogGen.loggen()

    @pytest.mark.order(6)
    @pytest.mark.usefixtures("setup")
    def test_verify_two_cards_on_the_board(self):
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(username)
        self.lp.clickLogin()
        self.lp.setPassword(password)
        self.lp.clickLoginAtlassian()
        self.tp = TrelloPage(self.driver)
        self.tp.waitVisibilityHeader()
        self.tp.clickBoard()
        self.tb = TrelloBoard(self.driver)
        cards = self.tb.getCards()
        assert_that(len(cards)).is_equal_to(2)

    @pytest.mark.order(7)
    @pytest.mark.usefixtures("setup")
    def test_verify_card_with_comment(self):
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(username)
        self.lp.clickLogin()
        self.lp.setPassword(password)
        self.lp.clickLoginAtlassian()
        self.tp = TrelloPage(self.driver)
        self.tp.waitVisibilityHeader()
        self.tp.clickBoard()
        self.tb = TrelloBoard(self.driver)
        assert_that(self.tb.getCommentIcon()).is_true()

    @pytest.mark.order(8)
    @pytest.mark.usefixtures("setup")
    def test_add_new_comment_to_the_card(self):
        new_comment = "This is another new comment"
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(username)
        self.lp.clickLogin()
        self.lp.setPassword(password)
        self.lp.clickLoginAtlassian()
        self.tp = TrelloPage(self.driver)
        self.tp.waitVisibilityHeader()
        self.tp.clickBoard()
        self.tb = TrelloBoard(self.driver)
        self.tb.clickCommentIcon()
        self.tb.setNewComment(new_comment)
        self.tb.clickSaveComment()
        comments = self.tb.getCommentsBoxes()
        for i in comments:
            if i.text == new_comment:
                comment_found = True
            else:
                continue
        assert_that(comment_found).is_true()

    @pytest.mark.order(9)
    @pytest.mark.usefixtures("setup")
    def test_set_card_as_done(self):
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(username)
        self.lp.clickLogin()
        self.lp.setPassword(password)
        self.lp.clickLoginAtlassian()
        self.tp = TrelloPage(self.driver)
        self.tp.waitVisibilityHeader()
        self.tp.clickBoard()
        self.tb = TrelloBoard(self.driver)
        self.tb.dragAndDropToDone()
        assert_that(self.tb.cardExistInDoneList()).is_true()
