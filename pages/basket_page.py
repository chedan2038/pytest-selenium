from .base_page import BasePage
from .locators import BasePageLocators


class BasketPage(BasePage):

    def basket_formset_is_empty(self):
        assert not self.is_element_present(*BasePageLocators.BASKET_FORMSET), "Basket formset is not empty"

    def basket_formset_is_not_empty(self):
        assert self.is_not_element_present(*BasePageLocators.BASKET_FORMSET), "Basket formset is empty"

    def message_basket_is_empty(self):
        assert self.is_element_present(
            *BasePageLocators.BASKET_EMPTY_MESSAGE), "Message: 'Basket is empty' is not presented"

    def disappeared_message_basket_is_empty(self):
        assert self.is_not_element_present(
            *BasePageLocators.BASKET_EMPTY_MESSAGE), "Message: 'Basket is empty' is presented"
