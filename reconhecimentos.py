import cv2
import torch
import serial
import time
import pandas as pd

# Configuração da comunicação serial com o Arduino
PORTA_SERIAL = 'COM3'  # Atualize com a porta correta (agora entre aspas)
BAUD_RATE = 115200

# Tentativa de conectar ao Arduino
try:
    arduino = serial.Serial(PORTA_SERIAL, BAUD_RATE, timeout=1)
    print("Conectado ao Arduino com sucesso.")
except serial.SerialException as e:
    print(f"Erro na comunicação serial: {e}")
    exit(1)

# Configuração do YOLOv5
model = torch.hub.load('yolov5', 'yolov5s', source='local', pretrained=True)

# Classes de objetos de interesse
CLASSES_INTERESSADAS = ['bottle', 'keyboard', 'mouse', 'cup', 'plate', 'notebook', 'book', 'clock']
itens_para_nota = []

def obter_peso_arduino():
    """Lê o peso da balança conectada via serial (Arduino)."""
    try:
        linha = arduino.readline().decode('utf-8').strip()
        return float(linha) if linha else None
    except ValueError:
        return None

def reconhecer_objeto(frame):
    """Reconhece objetos no frame usando o modelo YOLOv5."""
    results = model(frame)
    print(results.pandas())  # Exibe o conteúdo retornado para depuração
    objetos = results.pandas().xyxy[0]
    return objetos

# Captura de vídeo
camera = cv2.VideoCapture(0)

if not camera.isOpened():
    print("Erro ao acessar a câmera.")
    exit()

while True:
    ret, frame = camera.read()
    if not ret:
        print("Erro ao capturar o frame. Encerrando...")
        break

    objetos_detectados = reconhecer_objeto(frame)
    peso_atual = obter_peso_arduino()

    if peso_atual is not None:
        print(f"Peso detectado: {peso_atual} g")

        for _, row in objetos_detectados.iterrows():
            if row['name'] not in CLASSES_INTERESSADAS:
                continue

            label = f"{row['name']} ({row['confidence']:.2f})"
            x1, y1, x2, y2 = int(row['xmin']), int(row['ymin']), int(row['xmax']), int(row['ymax'])

            # Desenhando o retângulo verde ao redor do objeto detectado
            cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)

            # Colocando o nome do objeto acima do retângulo
            cv2.putText(frame, label, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

            # Adiciona o item à nota fiscal com base no peso
            preco_unitario = 5.0  # Exemplo: preço unitário para cada objeto
            peso_kg = peso_atual / 1000  # Converte para kg
            total = peso_kg * preco_unitario

            # Adiciona o item à lista de itens para a nota fiscal
            itens_para_nota.append([row['name'], peso_kg, preco_unitario, total])

    # Exibe o vídeo com objetos reconhecidos e desenhados
    cv2.imshow("Reconhecimento de Objetos", frame)

    # Se pressionar ESC (27), encerra o loop
    if cv2.waitKey(1) & 0xFF == 27:
        break

camera.release()
cv2.destroyAllWindows()

# Gera a nota fiscal, se houver itens reconhecidos
if itens_para_nota:
    nota_fiscal = pd.DataFrame(itens_para_nota, columns=["Objeto", "Peso (kg)", "Preço Unitário (R$)", "Total (R$)"])
    nota_fiscal.to_csv("nota_fiscal.csv", index=False)
    print("Nota fiscal gerada com sucesso: nota_fiscal.csv")
    print(nota_fiscal)
else:
    print("Nenhum item reconhecido para a nota fiscal.")
