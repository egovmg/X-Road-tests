# -*- coding: utf-8 -*-
# Example for using WebDriver object: driver = get_driver() e.g driver.current_url
from QAutoLibrary.extension import TESTDATA
from selenium.webdriver.common.by import By
from QAutoLibrary.QAutoSelenium import *
from time import sleep

class Cs_conf_mgm_enter_pin(CommonUtils):
    """
    Pagemodel

    Changelog:

    * 27.07.2017
        | Docstrings updated
    """
    # Pagemodel timestamp: 20160811111146
    # Pagemodel url: https://xroad-lxd-cs.lxd:4000/configuration_management
    # Pagemodel area: (759, 387, 402, 201)
    # Pagemodel screen resolution: (1920, 1080)
    # Use project settings: True
    # Used filters: id, css_selector, class_name, link_text, xpath
    # Xpath type: xpath-position
    # Create automated methods: True
    # Depth of css path: 3
    # Minimize css selector: True
    # Use css pattern: False
    # Allow non unique css pattern: False
    # Pagemodel template: False
    # Use testability: True
    # testability attribute: data-name
    # Use contains text in xpath: True
    # Exclude dynamic table filter: True
    # Row count: 5
    # Element count: 20
    # Big element filter width: 55
    # Big element filter height: 40
    # Not filtered elements: button, strong, select
    # Canvas modeling: False
    # Pagemodel type: normal
    # Links found: 0
    # Page model constants:
    MENUBAR_MAXIMIZE = (By.XPATH, u'//div[9]/div[1]/div[1]/button[1]') # x: 1058 y: 386 width: 51 height: 49, tag: button, type: submit, name: None, form_id: , checkbox: , table_id: 5, href:
    MENUBAR_CLOSE = (By.XPATH, u'//div[9]/div[1]/div[1]/button[2]') # x: 1109 y: 386 width: 51 height: 49, tag: button, type: submit, name: None, form_id: , checkbox: , table_id: 5, href:
    TITLE = (By.ID, u'ui-id-8') # x: 770 y: 400 width: 67 height: 21, tag: span, type: , name: None, form_id: , checkbox: , table_id: , href: None
    PIN = (By.XPATH, u'//div[9]/div[2]/div[1]/table[1]/tbody[1]/tr[1]/td[1]') # x: 775 y: 451 width: 57 height: 43, tag: td, type: , name: None, form_id: , checkbox: , table_id: 5, href:
    ID_ACTIVATE_TOKEN_PIN = (By.ID, u'activate_token_pin') # x: 836 y: 456 width: 306 height: 33, tag: input, type: password, name: activate_token_pin, form_id: , checkbox: , table_id: 5, href:
    BUTTON_OK = (By.XPATH, u'//div[9]/div[3]/div[1]/button[1]') # x: 1110 y: 544 width: 45 height: 37, tag: button, type: button, name: None, form_id: , checkbox: , table_id: 5, href:
    # Dynamic objects:
    CLOSE_BUTTON = (By.XPATH, u'(//div[@aria-describedby = \'activate_token_dialog\']//span[@class = \'ui-button-text\' and text() = \'Close\'])[2]') # x: 1049 y: 555 width: 39 height: 18, tag: span, type: , name: None, form_id: , checkbox: , table_id: , href: None
    OK_BUTTON = (By.XPATH, u'//*[contains(@aria-describedby,\"activate_token_dialog\")]/div/div/button[1]/span') # x: 1124 y: 559 width: 18 height: 18, tag: span, type: , name: None, form_id: , checkbox: , table_id: , href: None

    def input_text_to_id_activate_token_pin(self, parameters=None):
        """
        Input text to activate token pin

        :param parameters:  Test data section dictionary
        """
        # AutoGen method
        self.input_text(self.ID_ACTIVATE_TOKEN_PIN, parameters['pin'])

    def click_button_ok(self):
        """
        Click button to ok the dialog

        """
        # AutoGen method
        self.click_element(self.OK_BUTTON)

    def close_dialog(self, parameters=None):
        """

        :param parameters:  Test data section dictionary
        """
        self.click_element(self.CLOSE_BUTTON)

    def verify_pin_dialog_is_open(self):
        """
        Verify pin dialog

        """
        self.element_should_be_present(self.ID_ACTIVATE_TOKEN_PIN)
