import stripe
from django.conf import settings


def stripe_checkout(price, name, description):
    DOMAIN_ROOT = settings.DOMAIN_ROOT
    try:
        stripe.api_key = settings.STRIPE_API_KEY
        checkout_session = stripe.checkout.Session.create(
            line_items=[
                {
                    "price_data": {
                        "currency": "PLN",
                        "unit_amount": f"{int(price*100)}",
                        "product_data": {"name": name, "description": description},
                    },
                    "quantity": 1,
                },
            ],
            mode="payment",
            success_url=DOMAIN_ROOT + "/success",
            cancel_url=DOMAIN_ROOT + "/cancel",
        )
        return {"ok": True, "redirect_url": checkout_session.url}
    except Exception as e:
        return {"ok": False, "error_msg": str(e)}
