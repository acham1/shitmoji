from flask import Flask, jsonify, send_from_directory
from emojis import emojis
import random

app = Flask(__name__, static_url_path='')
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 300

@app.route('/')
def serve():
    return send_from_directory('static', 'index.html')

@app.route('/static/<path:path>')
def send_assets(path):
    return send_from_directory('static', path)

@app.route('/rand')
def rand():
    emoji = random.choice(emojis)
    if emoji == '🦙💩':
        return jsonify({ 'emoji': '''<a onclick="activateTrapCard()">🦙💩</a>'''})
    return jsonify({ 'emoji': emoji })

