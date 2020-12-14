import json
from flask import Flask, Response, request

from case.web.service import test1fromService

app = Flask(__name__)


@app.route("/health")
def health():
    result = {'status': 'UP'}
    return Response(json.dumps(result), mimetype='application/json')


@app.route("/getUser")
def getUser():
    result = {'username': 'python', 'password': 'python'}
    return Response(json.dumps(result), mimetype='application/json')

'''
get的多参数测试
'''


@app.route("/a")
def test1():
    return test1fromService()
    if request.args.get('b') is not None:
        print(request.args.get('a') + "\n")
    if request.args.get('b') is not None:
        print(request.args.get('b') + "\n")

    result = {'username': 'python', 'password': 'python'}
    return Response(json.dumps(result), mimetype='application/json')


'''
post的json传参测试
'''
@app.route("/b", methods=['GET', 'POST'])
def aa():
    if request.method == 'POST':
        data = request.get_data()
        print(data)
        json_data = json.loads(data.decode("utf-8"))
        print(json_data)
    result = {'name': 'python', 'ps': 'python'}
    return Response(json.dumps(result), mimetype='application/json')

app.run(port=3000, host='0.0.0.0')
