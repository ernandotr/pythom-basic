import cv2

# Script para gravar vídeo usando OpenCV
# Certifique-se de ter o OpenCV instalado: pip install opencv-python
cap = cv2.VideoCapture(0)

# Verifica se a câmera foi aberta corretamente
if not cap.isOpened():
    print("Erro: Não foi possível acessar a câmera.")
    exit()

# Define o codec e cria o objeto VideoWriter
fourcc = cv2.VideoWriter_fourcc(*'MJPG')  # Codec (pode ser 'MJPG' ou 'mp4v' para .mp4)

# Cria o objeto VideoWriter, especificando o nome do arquivo, codec, FPS e tamanho do vídeo
out = cv2.VideoWriter('video_saida.mp4', fourcc, 20.0, (640, 480))

print("Gravando... Pressione 'q' para parar.")

# Loop para capturar frames da câmera
while True:
    ret, frame = cap.read()
    if not ret:
        break

    out.write(frame)               # Grava o frame no arquivo
    cv2.imshow('Gravando', frame) # Mostra o vídeo ao vivo

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Libera os recursos
cap.release()
out.release()
cv2.destroyAllWindows()
