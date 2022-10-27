import json
from . import *
from flask import jsonify, request
from flask.views import MethodView
from .database import *


@person.class_route("/persona", "persona_view", **{"pk": "identificacion"})
class PersonView(MethodView):
    def get(self, identificacion):
        if identificacion is None:
            sql = "SELECT * FROM PERSONA ORDER BY apellidos ASC"
        else:
            sql = "SELECT * FROM PERSONA WHERE identificacion = {} ORDER BY apellidos ASC".format(identificacion)
        data = query_r(sql)
        return jsonify(data)


    def post(self):
        # create a new invoice
        print("POST INFO ...")
        data = json.loads(request.data)
        response = {"code": "OK create", "method": "POST", "response": "Successfull!", "sale_id": None, "data": data}
        return jsonify(response)


    def put(self, invoice_id):
        # update a single invoice
        print("PUT INFO ...")
        data = json.loads(request.data)
        response = {"code": "OK update", "method": "PUT", "response": "Successfull!", "sale_id": invoice_id,
                    "data": data}
        return jsonify(response)


    def delete(self, invoice_id):
        # delete a single invoice
        print("DELETE INFO ...")
        response = {"code": "OK delete", "method": "DELETE", "response": "Successfull!", "sale_id": invoice_id,
                    "data": None}
        return jsonify(response)

