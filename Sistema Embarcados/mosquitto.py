import paho.mqtt.client as mqtt

# Configurações do broker e tópico
MQTT_BROKER = "192.168.x.x"  # Substitua pelo IP do broker MQTT
MQTT_PORT = 1883  # Porta padrão
MQTT_TOPIC = "camera/data"

# Callback para conexão
def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Conectado ao broker MQTT com sucesso!")
    else:
        print(f"Falha na conexão. Código de retorno: {rc}")

# Publica uma mensagem no tópico
def publish_message():
    message = "Teste de dados da câmera"
    client.publish(MQTT_TOPIC, message)
    print(f"Mensagem publicada: {message}")

# Configuração do cliente MQTT
client = mqtt.Client()
client.on_connect = on_connect

# Conectando ao broker
client.connect(MQTT_BROKER, MQTT_PORT, 60)

# Inicia o loop MQTT
client.loop_start()

# Publica mensagens continuamente (simulação)
try:
    while True:
        publish_message()
        time.sleep(5)  # Publica a cada 5 segundos
except KeyboardInterrupt:
    print("Desconectando...")
    client.loop_stop()
    client.disconnect()
