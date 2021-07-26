import this

import pytest
import requests

from assertpy.assertpy import assert_that
from config import BASE_URI, TOKEN, API_KEY, board_name
from utils.print_helpers import pretty_print

board_id = ''


@pytest.mark.order(1)
def test_create_board():
    response = requests.post(BASE_URI + '/boards/?key=' + API_KEY + '&token=' + TOKEN + '&name=' + board_name)
    response_text = response.json()
    pretty_print(response_text)

    # Validating response status code and name field in json response
    assert_that(response.status_code).is_equal_to(200)
    assert_that(response_text.get('name')).is_not_empty().contains(board_name)
    this.board_id = response_text.get('id')

    # GET Request to verify the board exists
    response = requests.get(BASE_URI + '/boards/' + this.board_id + '?key=' + API_KEY + '&token=' + TOKEN)
    assert_that(response.status_code).is_equal_to(200)


@pytest.mark.order(2)
def test_create_three_cards():
    # GET Request to obtain all the lists for specific board
    response = requests.get(BASE_URI + '/boards/' + this.board_id + '/lists?key=' + API_KEY + '&token=' + TOKEN)
    response_text = response.json()
    assert_that(response.status_code).is_equal_to(200)

    # Saving list id
    list_id = response_text[0].get('id')

    # For loop to execute POST Request to create 3 cards
    for x in range(3):
        response = requests.post(
            BASE_URI + '/cards?key=' + API_KEY + '&token=' + TOKEN + '&idList=' + list_id + '&name'
                                                                                            '=board'
            + str(x))
        assert_that(response.status_code).is_equal_to(200)


@pytest.mark.order(3)
def test_edit_one_card():
    # GET Request to obtain all the cards for specific board
    response = requests.get(BASE_URI + '/boards/' + this.board_id + '/cards?key=' + API_KEY + '&token=' + TOKEN)
    response_text = response.json()
    assert_that(response.status_code).is_equal_to(200)

    # Saving card id
    card_id = response_text[0].get('id')

    # PUT Request to update first card
    response = requests.put(BASE_URI + '/cards/' + card_id + '?key=' + API_KEY + '&token=' + TOKEN + '&name'
                                                                                                     '=board_'
                                                                                                     'edited'
                                                                                                     '&desc'
                                                                                                     '=card_edited_for'
                                                                                                     '_plentific')
    assert_that(response.status_code).is_equal_to(200)


@pytest.mark.order(4)
def test_delete_one_card():
    # GET Request to obtain all the cards for specific board
    response = requests.get(BASE_URI + '/boards/' + this.board_id + '/cards?key=' + API_KEY + '&token=' + TOKEN)
    response_text = response.json()
    assert_that(response.status_code).is_equal_to(200)

    # Saving card id for the last card
    card_id = response_text[len(response_text) - 1].get('id')

    # PUT Request to update first card
    response = requests.delete(BASE_URI + '/cards/' + card_id + '?key=' + API_KEY + '&token=' + TOKEN)
    assert_that(response.status_code).is_equal_to(200)


@pytest.mark.order(5)
def test_add_comment_card():
    comment= 'New comment :)'
    # GET Request to obtain all the cards for specific board
    response = requests.get(BASE_URI + '/boards/' + this.board_id + '/cards?key=' + API_KEY + '&token=' + TOKEN)
    response_text = response.json()
    assert_that(response.status_code).is_equal_to(200)

    # Saving card id for the last card
    card_id = response_text[len(response_text) - 1].get('id')

    # POST Request to create a new comment in the last card
    response = requests.post(
        BASE_URI + '/cards/' + card_id + '/actions/comments?key=' + API_KEY + '&token=' + TOKEN + '&text=' + comment)
    assert_that(response.status_code).is_equal_to(200)
