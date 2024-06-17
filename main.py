from flask import Flask
app = Flask(__name__)                    # Create a new instance of the Flask class called "app"

@app.route('/')             #halaman utama web

def hello_world():
    return 'Hello sabih rizani'

if __name__ == '__main__':
    app.run(debug=True)