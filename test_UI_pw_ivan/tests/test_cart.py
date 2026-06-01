def test_check_title(cart_page):
    cart_page.open_page()
    cart_page.verify_title('Shopping Cart | My Website')


def test_empty_cart(cart_page):
    cart_page.open_page()
    cart_page.verify_empty_cart('Your cart is empty!')


def test_check_breadcrumbs(cart_page):
    cart_page.open_page()
    cart_page.verify_breadcrumbs('Review Order\nShipping\nPayment')
