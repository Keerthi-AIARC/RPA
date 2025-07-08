from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello Keerthi WELCOME to Community!!"

if __name__ == '__main__':
    app.run(debug=True)