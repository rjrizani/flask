from flask import Flask, request, render_template
app = Flask(__name__)

@app.route('/',methods=['GET','POST'])
def calculator():
    result = None
    if request.method == 'POST':
        num1 = request.form['num1']
        num2 = request.form['num2']
        operator = request.form['operator']
        if operator == 'add':
            result = float(num1) + float(num2)
        elif operator == 'subtract':
            result = float(num1) - float(num2)
        elif operator == 'multiply':
            result = float(num1) * float(num2)
        elif operator == 'divide':
            result = float(num1) / float(num2)
        else:
            result = 'Invalid operator'

        return render_template('callculator.html', result=result)

    return render_template('callculator.html', result=0)

if __name__ == '__main__':
    app.run(debug=True)