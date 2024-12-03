from flask import Flask, request, jsonify

app = Flask(__name__)

leaderboard = []

@app.route('/submit', methods=['POST'])
def submit_score():
    data = request.get_json()
    name = data.get('name')
    score = data.get('score')

    if name and score is not None:
        leaderboard.append({'name': name, 'score': score})
        leaderboard.sort(key=lambda x: x['score'], reverse=True)  # Sort by score
        return jsonify({'message': 'Score added successfully!'}), 200
    return jsonify({'error': 'Invalid data!'}), 400

@app.route('/leaderboard', methods=['GET'])
def get_leaderboard():
    return jsonify(leaderboard[:10])  # Return top 10 scores

if __name__ == '__main__':
    app.run(debug=True)
