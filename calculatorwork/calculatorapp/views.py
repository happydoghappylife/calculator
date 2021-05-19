from django.shortcuts import render

def home(request):
    return render(request, "home.html")

def result(request):
    first = request.GET['num1']
    second = request.GET['num2']
    num1 = int(first)
    num2 = int(second)
    op = request.GET['operator']
    result = 0
    zeroerr = str("!division by zero!")

    if op == '+':
        result = num1+num2
    elif op == '-':
        result = num1-num2
    elif op == '*':
        result = num1*num2
    elif op == '/':
        if num2 == 0:
            result = zeroerr
        else:
            result = num1/num2

    return render(request, "result.html", {'num1' : num1, 'num2' : num2, 'op' : op, 'result' : result,})