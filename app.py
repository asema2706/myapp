from flask import Flask, jsonify, request
import requests

app = Flask(__name__)

# Счётчик запросов (для мониторинга)
request_count = 0

@app.route('/')
def hello():
    global request_count
    request_count += 1
    return jsonify({"message": "Hello, DevOps!"})

@app.route('/health')
def health():
    """Endpoint для проверки работоспособности"""
    return jsonify({"status": "ok", "requests_served": request_count})

@app.route('/external')
def external():
    """Пример вызова внешнего API"""
    response = requests.get('https://jsonplaceholder.typicode.com/posts/1')
    return jsonify(response.json())

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)