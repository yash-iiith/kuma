from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains

from pypom import Page, Region


class BasePage(Page):

    URL_TEMPLATE = '/{locale}'

    def __init__(self, selenium, base_url, locale='en-US', **url_kwargs):
        super(BasePage, self).__init__(selenium, base_url, locale=locale, **url_kwargs)

    def wait_for_page_to_load(self):
        self.wait.until(lambda s: self.seed_url in s.current_url)
        el = self.find_element(By.TAG_NAME, 'html')
        self.wait.until(lambda s: el.get_attribute('data-ffo-opensanslight'))
        return self

    @property
    def header(self):
        return self.Header(self)

    @property
    def footer(self):
        return self.Footer(self)

    class Header(Region):
        _root_locator = (By.ID, 'main-header')
        _menu_locator = (By.ID, 'nav-main-menu')
        _submenu_trigger_locator = (By.CSS_SELECTOR, '#main-nav > ul:first-child > li:first-child > a:first-child')
        _submenu_locator = (By.CSS_SELECTOR, '#main-nav > ul:first-child > li:first-child > .submenu')
        _submenu_item_locator = (By.CSS_SELECTOR, '#main-nav > ul:first-child > li:first-child > .submenu > ul:first-child > li:first-child > a')

        # is displayed?
        @property
        def is_displayed(self):
            return self.root.is_displayed()

        # nav is displayed?
        @property
        def menu_is_displayed(self):
            menu = self.find_element(*self._menu_locator)
            return menu.is_displayed()

        @property
        def submenu_trigger_is_displayed(self):
            return self.find_element(*self._submenu_trigger_locator).is_displayed()

        @property
        def submenu_is_displayed(self):
            return self.find_element(*self._submenu_locator).is_displayed()

    class Footer(Region):
        _root_locator = (By.CSS_SELECTOR, 'body > footer')
        _language_locator = (By.ID, 'language')

        # is displayed?
        @property
        def is_displayed(self):
            return self.root.is_displayed()

        # language select is displayed
        @property
        def select_language_is_displayed(self):
            return self.find_element(*self._language_locator).is_displayed()

        # check lanuage selected in drop down matches locale
        @property
        def select_language_is_locale_match(self, locale):
            # get language selected
            language_selected = self.find_element(*self._language_locator).find_element('option[selected]').get_attribute('value')
            return (language_selected == locale)
