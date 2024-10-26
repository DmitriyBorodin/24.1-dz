import stripe
from config.settings import STRIPE_API_KEY

stripe.api_key = STRIPE_API_KEY


def create_stripe_product(product):
    """Создаёт продукт в Stripe, возвращает его id"""
    stripe_product = stripe.Product.create(name=product.name)
    return stripe_product.id


def create_stripe_price(stripe_id, amount):
    """Создаёт цену в Stripe"""
    return stripe.Price.create(
        currency="rub",
        unit_amount=amount*100,
        product=stripe_id,
    )


def create_stripe_session(price):
    """Создаёт сессию на оплату в Stripe"""
    session = stripe.checkout.Session.create(
        success_url="https://127.0.0.1:8000/",
        line_items=[{"price": price.get("id"), "quantity": 1}],
        mode="payment",
    )
    return session.get("id"), session.get("url")
