from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):

    def add_product_to_basket(self):
        basket = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET)
        basket.click()

    def alert_check(self):
        self.alert_product_in_basket()
        self.alert_total_price()

    def alert_product_in_basket(self):
        assert self.is_element_present(
            *ProductPageLocators.SUCCESS_ALERT), "Success alert: 'product in basket' - not found"

    def alert_total_price(self):
        self.is_element_present(*ProductPageLocators.ALERT_BASKET_TOTAL)

    def alert_book_and_form_book_names_is_same(self):
        book_name = self.browser.find_element(*ProductPageLocators.FORM_BOOK_NAME).text
        alert_book_name = self.browser.find_element(*ProductPageLocators.ALERT_BOOK_NAME).text
        assert book_name == alert_book_name, "Book name in alert and book name in form is not correct"

    def total_and_book_price_is_same(self):
        total = self.browser.find_element(*ProductPageLocators.BASKET_TOTAL).text
        book = self.browser.find_element(*ProductPageLocators.BOOK_PRICE).text
        assert book == total, "Book price and total price is not same"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_ALERT), \
            "Success message is presented, but should not be"

    def should_disappeare_succes_message(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_ALERT), \
            "Success message is presented, but should be gone"
