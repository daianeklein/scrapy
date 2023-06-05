from flask import Flask, render_template
import requests
import json

app = Flask(__name__)

@app.route('/')
def index():
    resp = requests.get(
        url = 'http://127.0.0.1:9080/crawl.json?start_requests=true&spider_name=best_selling'
    ).json()

    items = json.dumps(resp.get('items'))
    return items

@app.route('/show')
def show_template():
    users_list = [
        'User 1',
        'User 2',
        'User 3'
    ]
    return render_template('index.html', users_list = users_list)


if __name__ == "__main__":
    app.run(port=8000, debug=True)