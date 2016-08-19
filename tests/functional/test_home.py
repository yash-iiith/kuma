import pytest

from pages.home import HomePage


# homepage tests
@pytest.mark.smoke
@pytest.mark.nondestructive
def test_masthead_is_displayed(base_url, selenium):
    page = HomePage(selenium, base_url).open()
    assert page.is_masthead_displayed


# header tests
@pytest.mark.smoke
@pytest.mark.nondestructive
def test_header_is_displayed(base_url, selenium):
    page = HomePage(selenium, base_url).open()
    assert page.Header.is_displayed


@pytest.mark.smoke
@pytest.mark.nondestructive
def test_header_menu_is_displayed(base_url, selenium):
    page = HomePage(selenium, base_url).open()
    assert page.Header.menu_is_displayed


# footer tests
@pytest.mark.smoke
@pytest.mark.nondestructive
def test_footer_is_displayed(base_url, selenium):
    page = HomePage(selenium, base_url).open()
    assert page.Footer.is_displayed


@pytest.mark.smoke
@pytest.mark.nondestructive
def test_select_language_is_displayed(base_url, selenium):
    page = HomePage(selenium, base_url).open()
    assert page.Footer.select_language_is_displayed


@pytest.mark.smoke
@pytest.mark.nondestructive
def test_select_language_is_locale_match(base_url, selenium):
    page = HomePage(selenium, base_url).open()
    assert page.Footer.select_language_is_locale_match
