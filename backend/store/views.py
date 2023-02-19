from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
from .stripe import stripe_checkout


def testView(request):
    return render(request, "store/test.html")


def success(request):
    return render(request, "store/success.html")


def cancel(request):
    return render(request, "store/cancel.html")


def checkout(request):
    if request.method == "GET":
        return render(request, "store/checkout.html")
    elif request.method == "POST":
        # TODO: get it from 
        price = 2.5
        name = "testWybierzVintage"
        description = (
            "Zamówienie Wybierz Vintage nr 1, zawierające złoty wisior unique vintage"
        )
        s_checkout = stripe_checkout(price, name, description)
        if s_checkout["ok"]:
            return redirect(s_checkout["redirect_url"], code=303)
        return HttpResponse(s_checkout["error_msg"])
