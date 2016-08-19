from pypom import Region
from selenium.webdriver.common.by import By

from pages.base import BasePage


class ArticlePage(BasePage):

    URL_TEMPLATE = '/{locale}/docs/User:anonymous:uitest'

    _document_title_locator = (By.CSS_SELECTOR, 'title')
    _page_buttons_locator = (By.CSS_SELECTOR, '#document-main .page-buttons')
    _language_menu_locator = (By.ID, 'languages-menu')
    _edit_button_locator = (By.ID, 'edit-button')
    _advanced_menu_locator = (By.ID, 'advanced-menu')
    _page_title_locator = (By.CSS_SELECTOR, '#wiki-document-head h1')
    _article_locator = (By.ID, 'wikiArticle')

    # wrapper containing article is displayed
    @property
    def article_is_displayed(self):
        return self.find_element(*self._article_locator).is_displayed()

    # document title contains page title
    def title_in_title(self, selenium):
        document_title_text = selenium.title
        page_title_text = self.find_element(*self._page_title_locator).text
        return page_title_text in document_title_text

    def title_text_has_length(self, selenium):
        document_title_text = selenium.title
        return len(document_title_text) > 1

    # test all buttons are there
    @property
    def language_menu_is_displayed(self):
        return self.find_element(*self._language_menu_locator).is_displayed()

    @property
    def edit_button_is_displayed(self):
        return self.find_element(*self._edit_button_locator).is_displayed()

    @property
    def advanced_menu_is_displayed(self):
        return self.find_element(*self._advanced_menu_locator).is_displayed()
