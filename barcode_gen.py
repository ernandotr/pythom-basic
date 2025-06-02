import barcode
from barcode.writer import ImageWriter
import subprocess

# Dados para o código de barras
dados = "123456789102"  # precisa ser numérico em alguns formatos

# Escolhe o tipo de código de barras (ex: "code128", "ean13", etc.)
codigo = barcode.get('code128', dados, writer=ImageWriter())

# Salva como imagem PNG
nome_arquivo = codigo.save("codigo_de_barras")

print(f"Código de barras salvo como {nome_arquivo}.png")
# Exibe o código de barras
# Se você quiser abrir a imagem do código de barras
# import os
# os.startfile(f"{nome_arquivo}.png")  # Funciona no Windows
# Para outros sistemas operacionais, você pode usar:
# import subprocess
subprocess.run(["open", f"{nome_arquivo}"])  # macOS
