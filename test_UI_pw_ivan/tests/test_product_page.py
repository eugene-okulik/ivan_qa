def test_check_title(product_page):
    product_page.open_page()
    product_page.verify_title('Office Design Software | My Website')


def test_check_breadcrumbs(product_page):
    product_page.open_page()
    product_page.verify_breadcrumbs(
        'All Products\nMultimedia\nOffice Design Software'
    )


def test_check_name_of_product(product_page):
    product_page.open_page()
    product_page.verify_text_of_product('Office Design Software')


def test_check_price_of_product(product_page):
    product_page.open_page()
    product_page.verify_price_of_product('$ 280.00')


def test_adding_product_to_cart(product_page):
    product_page.open_page()
    product_page.add_product_to_cart()
    product_page.go_to_cart()
    product_page.verify_product_in_cart('Office Design Software', '$ 280.00')
