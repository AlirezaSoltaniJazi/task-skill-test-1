from pytest import mark

from pages import LoginPage, ProductsPage, ProductDetailsPage, CartPage, CheckoutPage


@mark.purchase
def test_purchase_a_product(android_driver_factory):
    with android_driver_factory() as driver:
        # Arrange
        url = 'https://www.saucedemo.com'
        login_page = LoginPage(driver)
        products_page = ProductsPage(driver)
        product_details_page = ProductDetailsPage(driver)
        cart_page = CartPage(driver)
        checkout_page = CheckoutPage(driver)

        # Login
        login_page.open_login_page(url)
        login_page.enter_username('standard_user')
        login_page.enter_password('secret_sauce')
        login_page.click_login_button()
        login_page.verify_successful_login()

        # Products
        products_page.select_first_product()

        # Product Details
        product_details_page.add_product_to_cart()
        product_details_page.return_to_products()

        # Products
        products_page.add_second_item_to_cart()
        products_page.open_cart()

        # Cart
        cart_page.verify_items_count(2)
        cart_page.open_checkout()

        # Checkout
        checkout_page.enter_first_name('Alireza')
        checkout_page.enter_last_name('SoltaniJazi')
        checkout_page.enter_zip('123456')
        checkout_page.continue_payment()
        checkout_page.verify_total_amount('Total: $43.18')
        checkout_page.confirm_purchase()
        checkout_page.verify_successful_purchase('Thank you for your order!')
