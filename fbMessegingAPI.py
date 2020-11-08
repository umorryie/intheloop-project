from flask import Flask, request, jsonify
app = Flask(__name__)

@app.route('/webhook', methods = ['POST', 'GET'])
def hello_world():
    if request.method == 'POST':
        params = request.json
        return params

    if request.method == 'GET':
        return 'KAKO SMO KAJ'

        """token = 'nekaj'
        postBody = {
            "messaging_type": "<MESSAGING_TYPE>",
            "recipient": {
                "id": "<PSID>"
            },
            "message": {
                "text": "Pa sem le uspel ti pisat iz te aplikacije haha"
            }
        }
        requests.post(url='https://graph.facebook.com/v8.0/me/messages?access_token={0}'.format(token),data=postBody)"""




if __name__ == "__main__":
    app.run()