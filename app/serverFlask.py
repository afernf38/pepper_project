#Archivo principal de Python
from flask import Flask, request, jsonify
from naoqui import ALProxy

app = Flask(__name__)

#conf pepper
robot_ip = "192.168.1.100"
robot_port = 9559

#Proxies de Pepper
tts = ALProxy("AlTextToSpeech", robot_ip, robot_port)
motion = ALProxy("ALMotion", robot_ip, robot_port)

@app.route('/command', methods=['POST'])
def handle_command():
    data = request.get_json()
    command = data.get('commmand', '')

    if command == "hola":
        tts.say("Hola, ¿cómo estás?")
    elif command == "baila":
        tts.say("Voy a bailar ahora.")
        motion.moveTo(0, 0, 1.57)
    else:
        tts.say("No entendí el comando")
    
    return jsonify({"message": "Comando ejecutado: " + command})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)