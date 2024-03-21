from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader


def handler404(request, exception):
    template = loader.get_template("404.html")
    return HttpResponse(template.render({}, request), status=404)
