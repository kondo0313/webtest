from flask import Flask, request, jsonify
from time import time

app = Flask(__name__)

print("//////////////////////////////START//////////////////////////////", flush=True)

@app.route('/message', methods=['POST'])
def receive_message():
    start_time = time()
    message = request.json.get('message')
    print(f"Received message: {message}", flush=True)
    end_time = time()
    print(f"Processing time: {end_time - start_time:.4f} seconds", flush=True)
    return jsonify({'status': 'Message received'}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
