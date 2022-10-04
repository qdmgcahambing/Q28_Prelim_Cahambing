from flask import Flask, jsonify, request

app = Flask(__name__)

temperature=[
    {
        "temp_id" : "1",
        "date" : "10-01-2022",
        "temperature" : "36 degrees C"
    },

    {
        "temp_id" : "2",
        "date" : "10-02-2022",
        "temperature" : "37 degrees C"
    },

]

@app.route('/temperature', methods=['GET'])
def displayTemp():
    return jsonify(temperature)

@app.route('/temperature/<int:index>', methods=['GET'])
def displayTempId(index):
    return jsonify(temperature[index])

@app.route('/temperature', methods=['POST'])
def addTemp():
    temp = request.get_json()
    temperature.append(temp)
    return {'temp_id': len(temperature)},200

@app.route('/temperature/<int:index>', methods=['DELETE'])
def deleteTemp(index):
    temperature.pop(index)
    return 'Temperature record was successfully deleted', 200

if __name__ == '__main__':
    app.run()