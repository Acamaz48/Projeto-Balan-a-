📦 Projeto Balança Inteligente
Sistema embarcado com visão computacional para identificar objetos, estimar peso e emitir notas fiscais, com integração via MQTT.

🛠 Tecnologias Usadas
Python 3

YOLOv5 (modelo pré-treinado yolov5s.pt)

OpenCV — reconhecimento por vídeo

MQTT (via Mosquitto)

Pandas / CSV — notas fiscais

Serial (pyserial) — comunicação com hardware (ex: balança física)

📁 Estrutura do Projeto
bash
Copiar
Editar
Projeto-Balan-a--main/
└── Sistema Embarcados/
    ├── dados_objetos.json       # Tabela de pesos e nomes dos objetos
    ├── nota_fiscal.csv          # Histórico de notas fiscais
    ├── mosquitto.py             # Publicador MQTT
    ├── reconhecimentos.py       # Script principal de visão computacional
    └── yolov5s.pt               # Modelo YOLOv5 para detecção
⚙️ Como Rodar o Projeto
Clone o repositório:

bash
Copiar
Editar
git clone https://github.com/lukasdsouza/Zenith_App_v1
cd Projeto-Balan-a--main/Sistema\ Embarcados
Instale as dependências:

bash
Copiar
Editar
pip install -r requirements.txt
Execute o script de reconhecimento:

bash
Copiar
Editar
python reconhecimentos.py
Isso abrirá a câmera, detectará objetos com o YOLO, identificará pesos via dados_objetos.json e publicará via MQTT usando mosquitto.py.

🔄 Comunicação MQTT
O mosquitto.py publica dados para um tópico MQTT (ajustável no script), ideal para dashboards IoT ou integração com outros sistemas.

✅ Requisitos de Hardware (opcional)
Câmera USB

Módulo de peso com comunicação serial (ex: HX711 com Arduino)

Broker MQTT local ou via nuvem (ex: Mosquitto)

🧠 Personalização YOLO
Para treinar novos objetos:

Acesse o repo oficial do YOLOv5

Treine com suas imagens

Substitua yolov5s.pt pelo novo modelo no projeto
