


@app.get('/calculate', response_class=HTMLResponse)
async def calculator(request: Request):
    return templates.TemplateResponse('calculator.html', {'request': request})


@app.post('/calculate')
async def calculate(numbers: Numbers):
    result = numbers.num1 + numbers.num2
    data = {'result': result}
    return JSONResponse(content=data)