from .base import BasePage
from ui.locators.locators import AudiencePageLocators
from selenium.common.exceptions import TimeoutException


class LackOfButtonCreateSegment(Exception):
    pass


class LackOfButtonDeleteSegment(Exception):
    pass


class AudiencePage(BasePage):
    locators = AudiencePageLocators()

    def create_new_audience_click(self):
        check_create = False
        try:
            self.click(self.locators.CREATE_NEW_SEGMENT)
            check_create = True
        except TimeoutException:
            pass
        if check_create is False:
            try:
                self.click(self.locators.CREATE_SEGMENT)
            except TimeoutException:
                raise LackOfButtonCreateSegment

    def add_segment_window(self, ac):
        self.click(self.locators.CREATE_SEGMENT_BUTTON)
        try:
            element = self.find(self.locators.OK_AND_MOY_MIR_1)
            ac.move_to_element(element).perform()
            self.click(self.locators.OK_AND_MOY_MIR_1)
        except TimeoutException:
            element = self.find(self.locators.OK_AND_MOY_MIR_2)
            ac.move_to_element(element).perform()
            self.click(self.locators.OK_AND_MOY_MIR_2)
        self.click(self.locators.PLAY_AND_PAY_CHECKBOX)

        element = self.find(self.locators.SUBMIT_SEGMENT_BUTTON)
        ac.move_to_element(element).perform()

        self.click(self.locators.SUBMIT_SEGMENT_BUTTON)

    def input_segment_name(self, name):
        self.find(self.locators.INPUT_CREATE_SEGMENT_FORM).clear()
        self.click(self.locators.INPUT_CREATE_SEGMENT_FORM).send_keys(name)

    def submit_all_segment_click(self):
        self.click(self.locators.SUBMIT_ALL_SEGMENT_BUTTON)

    def delete_segment(self):
        try:
            self.find(self.locators.DELETE_SEGMENT)
        except TimeoutException:
            raise LackOfButtonDeleteSegment
        self.click(self.locators.DELETE_SEGMENT)
        self.click(self.locators.DELETE_BUTTON)

    def search_segment(self, name):
        self.click(self.locators.INPUT_SEARCH_SEGMENT_NAME).send_keys(name)
        self.click(self.locators.SEARCH_NAME_BUTTON)
        self.find(self.locators.LIST_SEGMENT_NAMES)
        return self.driver.find_element_by_css_selector("[title^='{}']".format(name))
