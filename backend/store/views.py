from django.shortcuts import render
from django.http.response import (
    Http404,
    HttpResponseRedirect,
    JsonResponse,
    HttpResponse,
)
from django.shortcuts import render


def testView():
    return JsonResponse({"message": "Test ok"}, status=200)
