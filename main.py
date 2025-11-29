from flask import Flask, request, jsonify
from agent import invoke_agent
from contact import send_email as contact_me
from flask_cors import CORS

app = Flask(__name__)
CORS(app) 

@app.route('/chatbot', methods=['POST'])
def chatbot():
    data = request.get_json()
    if not data or 'message' not in data:
        return jsonify({'error': 'No message provided'}), 400
    
    user_message = data.get('message')
    
    return jsonify(invoke_agent(user_message)), 200

@app.route('/contact', methods=['POST'])
def contact():
    data = request.get_json()
    
    name = data.get('name')
    email = data.get('email')
    message = data.get('message')

    response = contact_me(name, email, message)

    if "error" in response:
        return jsonify({"error": "An Error Occured, Pls contact me directly via email"}), 500
    else:
        return jsonify({"success": "message sent"}),200

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
