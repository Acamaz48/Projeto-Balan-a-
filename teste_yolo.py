import torch

try:
    model = torch.hub.load('yolov5', 'yolov5s', source='local', pretrained=True)
    print("✅ Modelo YOLOv5 carregado com sucesso!")
except Exception as e:
    print(f"❌ Erro ao carregar o modelo: {e}")
