from django.shortcuts import render
from django.http.response import (
    Http404,
    HttpResponseRedirect,
    JsonResponse,
    HttpResponse,
)


def testView(request):
    return JsonResponse({"message": "Test ok"}, status=200)
