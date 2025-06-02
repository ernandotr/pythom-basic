import qrcode

# Dados que você quer codificar no QR Code
dados = "https://www.exemplo.com"

# Cria o QR Code
qr = qrcode.QRCode(
    version=1,  # controla o tamanho do QR Code (1 a 40); use 1 para automático
    error_correction=qrcode.constants.ERROR_CORRECT_L,  # nível de correção de erro (L, M, Q, H)
    box_size=10,  # tamanho de cada "quadrado" do QR Code
    border=4,  # margem em torno do QR Code
)

qr.add_data(dados)
qr.make(fit=True)

# Gera a imagem
img = qr.make_image(fill_color="black", back_color="orange")

# Salva a imagem em um arquivo
img.save("qrcode_exemplo.png")

print("QR Code gerado com sucesso!")
# Exibe o QR Code
img.show()  # Descomente esta linha se quiser abrir a imagem do QR Code


