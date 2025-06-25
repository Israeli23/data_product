from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to my API, hello guys"

@app.route('/api/data', methods=['GET'])
def get_data():
    #name = request.args.get('name')
    sample_data = {
            "name": "Israel",
            "occupation": "Data engineer",
            "favourite food": "Pizza"
        }
    return jsonify(sample_data)


if __name__ == '__main__':
    app.run(debug=True)