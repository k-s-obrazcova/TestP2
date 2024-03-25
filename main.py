from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello_world():
    return ('Hello, World! Test text,'
            ' para P50-5-20, 25.05.2024. Test Check Style Project')


app.run()
