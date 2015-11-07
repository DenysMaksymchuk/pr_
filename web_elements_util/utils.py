from selenium.webdriver.remote.webelement import WebElement

__author__ = 'dmakstc'


def input_text_in_field(text_field_web_elem, text, by_symbols):
    """
    Method emulates one by one symbols input into input form or block text input
    :param text_field_web_elem: textfield to input:
    :param text: message to input:
    :param by_symbols: boolean value(if true input by symbols else insert text block)
    :return:
    """
    text_field_web_elem.clear()
    if by_symbols:
        for letter in text:
            text_field_web_elem.send_keys(letter)
    else:
        text_field_web_elem.send_keys(text)


def checkbox_set_state(check_box_web_elem, is_checked):
    """
    :param check_box_web_elem: checkbox web element
    :param is_checked: boolean value(true if we want check checkbox else false)
    :return:
    """
    if is_checked:
        if not check_box_web_elem.is_selected():
            check_box_web_elem.click()
    else:
        if check_box_web_elem.is_selected():
            check_box_web_elem.click()

WebElement