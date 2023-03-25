from flask import Flask, request

app = Flask(__name__)

@app.route('/api')
def my_api():

    return "thank you for sending me: " + request.args.get('variable') + "!"

if __name__ == '__main__':
    app.run()