from chalice import Chalice
import boto3
import json

app = Chalice(app_name='GOTOams Bot')
app.debug = True
lex = boto3.client('lex-runtime', region_name='us-east-1')


@app.route('/', methods=['POST'])
def index():
    body = app.current_request.json_body
    response = lex.post_text(botName='GOTOams Bot', botAlias='GOTOams Bot', userId='sampleuserid',
                             inputText=body['usertext'])
    return response


@app.route('/hello/{name}')
def hello_name(name):
    # '/hello/james' -> {"hello": "james"}
    return {'hello': name}


# @app.route('/users', methods=['POST'])
# def create_user():
#     # This is the JSON body the user sent in their POST request.
#     user_as_json = app.json_body
#     # Suppose we had some 'db' object that we used to
#     # read/write from our database.
#     # user_id = db.create_user(user_as_json)
#     return {'user_id': user_id}
