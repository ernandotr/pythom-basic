import cv2

cap = cv2.VideoCapture(0)

# Verifica se a câmera foi aberta corretamente
if not cap.isOpened():
    print("Erro: Não foi possível acessar a câmera.")
    exit()

# Captura uma imagem da câmera
ret, frame = cap.read()

# Verifica se a captura foi bem-sucedida
if ret:
    # Exibe a imagem capturada
    cv2.imshow("Foto Capturada", frame)
    cv2.waitKey(0)  # Espera até que uma tecla seja pressionada
    cv2.destroyAllWindows()  # Fecha a janela de exibição
    # Salva a imagem capturada
    cv2.imwrite("foto_capturada.jpg", frame)  # Salva a imagem
    print("Foto salva como 'foto_capturada.jpg'")
else:
    print("Erro ao capturar imagem.")

# Libera a captura e fecha a janela
cap.release()
