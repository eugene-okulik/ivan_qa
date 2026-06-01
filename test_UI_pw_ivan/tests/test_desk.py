import pytest


def test_check_title(desk_page):
    desk_page.open_page()
    desk_page.verify_title('Shop | My Website')


def test_check_breadcrumbs(desk_page):
    desk_page.open_page()
    desk_page.verify_breadcrumbs('Products\nDesks')


def test_count_of_products(desk_page):
    desk_page.open_page()
    desk_page.count_of_products(9)


def test_attribute_of_product(desk_page):
    desk_page.open_page()
    desk_page.verify_attributes('Steel\nAluminium\nCustom')


def test_customezied_desk(desk_page):
    desk_page.open_page()
    desk_page.customize_desk('Customizable Desk\n750.00')


@pytest.mark.xfail(
        reason="Тест падает иногда из-за глючности сайта. Проходит 50 на 50."
)
def test_check_customization_desk(desk_page):
    desk_page.open_page()
    desk_page.customization_desk(
        '[FURN_0097] Customizable Desk (Steel, Black)'
    )
    desk_page.verify_customization_desk(
        '[FURN_0097] Customizable Desk (Steel, Black)'
    )
