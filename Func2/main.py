import requests
from flask import Flask, request, jsonify
import azure.functions as func 
from flask_cors import CORS

app_flask = func.Blueprint()  
#Initialise Flask
app_flask = Flask(__name__)
CORS(app_flask)
 
#@app_flask.route(route='/api/v1/bank/BNPL', methods=['POST'])
@app_flask.post('/api/v1/bank/BNPL')
def BNPL():
    data = request.get_json()
   
    # Extract parameters from the request
    number = data.get('number')
    text = data.get('text')
 
    # Check if number is an 11-digit number and text is a non-empty string
    if not (number.isdigit() and len(number) == 11 and text.strip()):
        return jsonify({'error': 'Invalid parameters. Number should be 11 digits and text should be non-empty.'}), 400
   
    # Call another API with the validated parameters
    api_url = 'https://jsonplaceholder.typicode.com/posts'
    payload = {'number': number, 'text': text}
    response = requests.post(api_url, json=payload)
 
    # Return the response from the other API to the original entity
    return jsonify(response.json()), response.status_code
 
if __name__=='__main__':
   
    app_flask.run(debug=False)
