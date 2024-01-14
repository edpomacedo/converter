import os
from PIL import Image

def convert_jfif_to_png_folder(input_folder, output_folder):
    # Garante que a pasta de saída exista, se não existir, cria
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Lista todos os arquivos na pasta de entrada
    files = os.listdir(input_folder)

    for file in files:
        # Verifica se o arquivo tem extensão JFIF
        if file.lower().endswith(".jfif"):
            input_path = os.path.join(input_folder, file)
            # Gera o nome do arquivo de saída com a extensão PNG
            output_file = os.path.splitext(file)[0] + ".png"
            output_path = os.path.join(output_folder, output_file)

            # Converte o arquivo JFIF para PNG
            convert_jfif_to_png(input_path, output_path)

# Função para converter um arquivo JFIF para PNG
def convert_jfif_to_png(input_path, output_path):
    with Image.open(input_path) as img:
        img.save(output_path, 'PNG')

# Caminhos das pastas de entrada e saída
input_folder = 'input'
output_folder = 'output'

# Executa a conversão
convert_jfif_to_png_folder(input_folder, output_folder)
