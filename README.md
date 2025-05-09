# 📦 Projeto Balança Inteligente

Sistema embarcado com visão computacional para identificar objetos, estimar peso e emitir notas fiscais, com integração via MQTT.

---

## 🛠 Tecnologias Usadas

- **Python 3**
- **YOLOv5** (modelo pré-treinado `yolov5s.pt`)
- **OpenCV** — reconhecimento por vídeo
- **MQTT** (via Mosquitto)
- **Pandas / CSV** — notas fiscais
- **Serial (pyserial)** — comunicação com hardware (ex: balança física)

---

## 📁 Estrutura do Projeto

```
Projeto-Balan-a--main/
└── Sistema Embarcados/
    ├── dados_objetos.json       # Tabela de pesos e nomes dos objetos
    ├── nota_fiscal.csv          # Histórico de notas fiscais
    ├── mosquitto.py             # Publicador MQTT
    ├── reconhecimentos.py       # Script principal de visão computacional
    └── yolov5s.pt               # Modelo YOLOv5 para detecção
```

---

## ⚙️ Como Rodar o Projeto

1. Clone o repositório:

```bash
git clone https://github.com/lukasdsouza/Zenith_App_v1
cd Projeto-Balan-a--main/Sistema\ Embarcados
```

2. Instale as dependências:

```bash
pip install -r requirements.txt
```

3. Execute o script de reconhecimento:

```bash
python reconhecimentos.py
```

> Isso abrirá a câmera, detectará objetos com o YOLO, identificará pesos via `dados_objetos.json` e publicará via MQTT usando `mosquitto.py`.

---

## 🔄 Comunicação MQTT

O `mosquitto.py` publica dados para um tópico MQTT (ajustável no script), ideal para dashboards IoT ou integração com outros sistemas.

---

## ✅ Requisitos de Hardware (opcional)

- Câmera USB
- Módulo de peso com comunicação serial (ex: HX711 com Arduino)
- Broker MQTT local ou via nuvem (ex: Mosquitto)

---

## 🧠 Personalização YOLO

Para treinar novos objetos:

1. Acesse o [repositório oficial do YOLOv5](https://github.com/ultralytics/yolov5)
2. Treine com suas imagens
3. Substitua `yolov5s.pt` pelo novo modelo no projeto
