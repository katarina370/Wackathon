from flask import Flask, request, jsonify, render_template
import firebase_admin
from firebase_admin import credentials, firestore

app = Flask(__name__)

# Firebase 연결
cred = credentials.Certificate("firebase-key.json")
firebase_admin.initialize_app(cred)
db = firestore.client()

# 홈페이지
@app.route('/')
def index():
    return render_template('index.html')

# 카드 저장
@app.route('/save_card', methods=['POST'])
def save_card():
    data = request.get_json()
    card = {
        'title': data['title'],
        'description': data['description'],
        'userid': data['userid'],
        'lat': float(data['lat']),
        'lng': float(data['lng']),
        'createdAt': firestore.SERVER_TIMESTAMP
    }
    db.collection('cards').add(card)
    return jsonify({'status': 'success'})

# 카드 불러오기 
@app.route('/get_cards/<user_id>', methods=['GET'])
def get_cards(user_id):
    try:
        cards_ref = db.collection('cards').where('userid', '==', user_id)
        cards = [doc.to_dict() for doc in cards_ref.stream()]
        return jsonify(cards)
    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)
