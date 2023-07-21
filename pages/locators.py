from selenium.webdriver.common.by import By


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_BUTTON = (By.CSS_SELECTOR, "span>a.btn-default")
    BASKET_FORMSET = (By.CSS_SELECTOR, "#basket_formset")
    BASKET_EMPTY_MESSAGE = (By.CSS_SELECTOR, "#content_inner p")
    USER_ICON = (By.CSS_SELECTOR, "i.icon-user")


class MainPageLocators():
    pass


class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    REGISTER_EMAIL_INPUT = (By.CSS_SELECTOR, "#register_form #id_registration-email")
    REGISTER_PASSWORD_INPUT = (By.CSS_SELECTOR, "#register_form #id_registration-password1")
    REGISTER_PASSWORD_CONFIRM_INPUT = (By.CSS_SELECTOR, "#register_form #id_registration-password2")
    REGISTER_BUTTON = (By.CSS_SELECTOR, "button[name=registration_submit]")


class ProductPageLocators():
    ADD_TO_BASKET = (By.CSS_SELECTOR, "#add_to_basket_form button")
    SUCCESS_ALERT = (By.CSS_SELECTOR,
                     "[class='alert alert-safe alert-noicon alert-success  fade in']:nth-child(1) [class='alertinner ']")
    ALERT_BOOK_NAME = (By.CSS_SELECTOR,
                       "[class='alert alert-safe alert-noicon alert-success  fade in']:nth-child(1) [class='alertinner '] strong")

    ALERT_BASKET_TOTAL = (By.CSS_SELECTOR, "div[class='alertinner '] p strong")
    BASKET_TOTAL = (By.CSS_SELECTOR, ".alertinner p:nth-child(1) strong")
    BOOK_PRICE = (By.CSS_SELECTOR, ".product_main .price_color")
    FORM_BOOK_NAME = (By.CSS_SELECTOR, ".product_main h1")
