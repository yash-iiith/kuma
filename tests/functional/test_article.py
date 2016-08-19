import pytest

from pages.article import ArticlePage


# page title
@pytest.mark.smoke
@pytest.mark.nondestructive
def test_title_in_title(base_url, selenium):
    page = ArticlePage(selenium, base_url).open()
    assert page.title_in_title(selenium)


@pytest.mark.smoke
@pytest.mark.nondestructive
def test_title_text_has_length(base_url, selenium):
    page = ArticlePage(selenium, base_url).open()
    assert page.title_text_has_length(selenium)


# article
@pytest.mark.smoke
@pytest.mark.nondestructive
def test_article_is_displayed(base_url, selenium):
    page = ArticlePage(selenium, base_url).open()
    assert page.article_is_displayed


# page buttons
@pytest.mark.smoke
@pytest.mark.nondestructive
def test_language_menu_is_displayed(base_url, selenium):
    page = ArticlePage(selenium, base_url).open()
    assert page.language_menu_is_displayed


@pytest.mark.smoke
@pytest.mark.nondestructive
def test_edit_button_is_displayed(base_url, selenium):
    page = ArticlePage(selenium, base_url).open()
    assert page.edit_button_is_displayed


@pytest.mark.smoke
@pytest.mark.nondestructive
def test_advanced_menu_is_displayed(base_url, selenium):
    page = ArticlePage(selenium, base_url).open()
    assert page.advanced_menu_is_displayed


"""
The tests below are duplicates of ones in test_home, how can I avoid this?
"""


# header tests
@pytest.mark.smoke
@pytest.mark.nondestructive
def test_header_is_displayed(base_url, selenium):
    page = ArticlePage(selenium, base_url).open()
    assert page.Header.is_displayed


@pytest.mark.smoke
@pytest.mark.nondestructive
def test_header_menu_is_displayed(base_url, selenium):
    page = ArticlePage(selenium, base_url).open()
    assert page.Header.menu_is_displayed


# footer tests
@pytest.mark.smoke
@pytest.mark.nondestructive
def test_footer_is_displayed(base_url, selenium):
    page = ArticlePage(selenium, base_url).open()
    assert page.Footer.is_displayed


@pytest.mark.smoke
@pytest.mark.nondestructive
def test_select_language_is_displayed(base_url, selenium):
    page = ArticlePage(selenium, base_url).open()
    assert page.Footer.select_language_is_displayed


@pytest.mark.smoke
@pytest.mark.nondestructive
def test_select_language_is_locale_match(base_url, selenium):
    page = ArticlePage(selenium, base_url).open()
    assert page.Footer.select_language_is_locale_match
