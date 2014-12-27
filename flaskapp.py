from flask import Flask
app = Flask(__name__)
app.config.from_pyfile('flaskapp.cfg')


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route("/test")
def test():
    return "<strong>It's Alive!</strong>"

    if __name__ == '__main__':
        app.run()