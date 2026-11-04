import os
from flask import Flask, jsonify
app = Flask(__name__)
@app.route('/', methods=['GET'])
def inicio():
return jsonify({
'estado': 'Exitoso, prueba realizada con exito',
'mensaje': '¡API desplegada con éxito en la Nube!',
'materia': 'Servicios en la Nube',
'version': '2.0.0',
})
if __name__ == '__main__':
port = int(os.environ.get('PORT', 5000))
app.run(host='0.0.0.0', port=port)