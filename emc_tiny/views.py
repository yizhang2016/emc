from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def getFibonacciNums(request):
    threshold = 10000
    try:
        n = int(request.GET["n"])
        if n < 0:
            return HttpResponse("Failed: N is a negative integer")
        if n > threshold:
            return HttpResponse("Failed: sorry we don't accept too large number...")

        # base cases
        if n == 0:
            return HttpResponse("[]")
        elif n == 1:
            return HttpResponse("[0]")
        elif n == 2:
            return HttpResponse("[0, 1]")

        # normal cases
        res = [0] * n
        res[0], res[1] = 0, 1

        for i in xrange(2, n):
            res[i] = res[i-1] + res[i-2]

        return HttpResponse(str(res))
    except:
        return HttpResponse("Failed: input invalid (please enter an integer)!")

