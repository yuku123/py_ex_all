import json
from flask import Flask, Response, request


def test1fromService():
    result = {'username': 'python', 'password': 'dsdsds'}
    return Response(json.dumps(result), mimetype='application/json')
