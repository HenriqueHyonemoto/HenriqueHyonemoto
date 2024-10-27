import os
from tkinter import PhotoImage

# Define o diretório atual e o diretório de destino
current_folder = '.'  # Diretório atual
destination_folder = '.'  # Diretório "image" no nível anterior

# Cria o diretório de destino, caso ele não exista
os.makedirs(destination_folder, exist_ok=True)

# Define a resolução desejada
new_size = (50, 50)

# Loop por cada arquivo no diretório atual
for filename in os.listdir(current_folder):
    if filename.endswith('.png'):
        # Constrói o caminho completo do arquivo original
        file_path = os.path.join(current_folder, filename)
        
        # Extrai o nome do arquivo sem extensão
        base_name = os.path.splitext(filename)[0]
        
        # Define o novo caminho do arquivo no diretório de destino, com o sufixo "_50"
        new_file_path = os.path.join(destination_folder, f"{base_name}_50.png")

        # Carrega a imagem usando PhotoImage do tkinter
        img = PhotoImage(file=file_path)
        
        # Redimensiona a imagem
        img = img.subsample(int(img.width() / new_size[0]), int(img.height() / new_size[1]))
        
        # Salva a imagem redimensionada
        img.write(new_file_path, format="png")

print("Todas as imagens PNG foram redimensionadas para 50x50 e salvas no diretório 'image'.")
