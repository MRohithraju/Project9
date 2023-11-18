from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def input(request):
    return render(request,"input.html")
def calculate(request):
    i=int(request.POST["t1"])
    j=int(request.POST["t2"])
    optype=request.POST["op"]
    if optype=="add":
        z=i+j
        res="THE SUM IS:"+str(z)
    elif optype=="sub":
        z=i-j
        res="THE SUB IS:"+str(z)
    elif optype=="mul":
        z=i*j
        res="THE MUL IS:"+str(z)
    else:
        z=i/j
        res="THE DIV IS:"+str(z)

    response=HttpResponse(res)
    return response