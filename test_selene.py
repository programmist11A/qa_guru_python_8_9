import allure
from allure_commons.types import Severity
from selene.support import by
from selene.support.conditions import be
from selene.support.shared import browser
from selene.support.shared.jquery_style import s


@allure.tag("web")
@allure.severity(Severity.NORMAL)
@allure.label("owner", "Антон Фомин")
@allure.feature("Search issue on github")
@allure.description("Тест селена")
@allure.link("https://github.com", name="Testing")
def test_github():
    browser.open("https://github.com")

    s(".header-search-button").click()
    s("#query-builder-test").send_keys("eroshenkoam/allure-example")
    s("#query-builder-test").press_enter()

    s(by.link_text("eroshenkoam/allure-example")).click()

    s("#issues-tab").click()

    s(by.partial_text("#76")).should(be.visible)

    browser.quit()
