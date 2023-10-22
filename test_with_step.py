import allure
from allure_commons.types import Severity
from selene.support import by
from selene.support.conditions import be
from selene.support.shared import browser
from selene.support.shared.jquery_style import s


@allure.tag("web")
@allure.severity(Severity.MINOR)
@allure.label("owner", "Антон Фомин")
@allure.feature("Search issue on github")
@allure.description("Тест селена через лямбда шаги через with allure.step")
@allure.link("https://github.com", name="Testing")
def test_github_with_steps():
    with allure.step("Open main page"):
        browser.open("https://github.com")

    with allure.step("Find repository"):
        s(".header-search-button").click()
        s("#query-builder-test").send_keys("programmist11A/qa_quru_python_8_2")
        s("#query-builder-test").submit()

    with allure.step("Go to repository"):
        s(by.link_text("programmist11A/qa_quru_python_8_2")).click()

    with allure.step("Go to Issues tab"):
        s("#issues-tab").click()

    with allure.step("Check issue Issue for task"):
        s(by.partial_text("Issue for task")).should(be.visible)

    browser.quit()
