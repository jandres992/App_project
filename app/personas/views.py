from . import *
from flask import jsonify, request
from flask.views import MethodView
from .database import *


@person.class_route("/persona", "persona_view", **{"pk": "persona_id"})
class PersonView(MethodView):
    def get(self, persona_id):
        if persona_id is None:
            sql = "SELECT * FROM PERSONA ORDER BY apellidos ASC"
        else:
            if type(persona_id) == dict:
                sql = "SELECT * FROM PERSONA WHERE identificacion={} ORDER BY apellidos ASC".format(persona_id['identificacion'])
            else:
                sql = "SELECT * FROM PERSONA WHERE id={} ORDER BY apellidos ASC".format(persona_id)
        data = query_r(sql)
        return jsonify(data)


    def post(self):
        if 'identificacion' and 'nombre' and 'apellidos' and 'edad' in request.form:
            data = self.get({'identificacion': request.form['identificacion']})
            if data.json[0]:
                if not data.json[1]:
                    identificacion = request.form['identificacion']
                    nombre = request.form['nombre']
                    apellidos = request.form['apellidos']
                    edad = request.form['edad']

                    sql = "INSERT INTO PERSONA(id, identificacion, nombre, apellidos, edad) VALUES (0, '{0}', '{1}', '{2}', {3})".format(identificacion, nombre, apellidos, edad)
                    resp = query_l(sql)
                    if resp:
                        response = {"mesaje": "El registro ha sido agregado correctamente", 'status_code': 200}
                    else:
                        response = {"mesaje": "El registro no pudo ser almacenado", 'status_code': 500}
                else:
                    response = {'mensaje': "La persona ya se encuentra creada", 'status_code': 200}
            else:
                response = {"mensaje": "No se obtuvo acceso a la base de datos", 'status_code': 500}
        else:
            response = {"error": "Faltan suministrar información", "status_code": 404}
        return jsonify(response)


    def put(self, persona_id):
        if 'identificacion' and 'nombre' and 'apellidos' and 'edad' in request.json:
            data = self.get(persona_id)
            if data.json[0]:
                if data.json[1]:
                    identificacion = request.json['identificacion']
                    nombre = request.json['nombre']
                    apellidos = request.json['apellidos']
                    edad = request.json['edad']

                    sql = "UPDATE PERSONA SET identificacion='{0}',nombre='{1}',apellidos='{2}', edad={3} WHERE id={4}".format(identificacion, nombre, apellidos, edad, persona_id)

                    resp = query_l(sql)
                    if resp:
                        response = {"mesaje": "El registro ha sido actualizado correctamente", 'status_code': 200}
                    else:
                        response = {"mesaje": "El registro no pudo ser almacenado", 'status_code': 500}
                else:
                    response = {'mensaje': "La persona no se encuentra creada", 'status_code': 404}
            else:
                response = {"mensaje": "No se obtuvo acceso a la base de datos", 'status_code': 500}
        else:
            response = {"error": "Faltan suministrar información", "status_code": 404}
        return jsonify(response)


    def delete(self, persona_id):
        data = self.get(persona_id)
        if data.json[0]:
            sql = "DELETE FROM `PERSONA` WHERE id={0}".format(persona_id)
            resp = query_l(sql)
            if resp:
                response = {"mesaje": "El registro ha sido eliminado", 'status_code': 200}
            else:
                response = {"mesaje": "El registro no pudo ser eliminado", 'status_code': 500}
        else:
            response = {"mensaje": "No se encontraron registros para eliminar", 'status_code': 500}

        return jsonify(response)

