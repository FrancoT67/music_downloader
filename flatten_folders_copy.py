import os
import shutil

def flatten_folders(base_path):
    """
    Recorre todas las carpetas en un directorio base, mueve los archivos contenidos al nivel superior,
    y elimina las carpetas vacías.
    
    :param base_path: Ruta del directorio base.
    """
    for root, dirs, files in os.walk(base_path, topdown=False):
        for file in files:
            # Mueve cada archivo al directorio base
            source_path = os.path.join(root, file)
            destination_path = os.path.join(base_path, file)

            # Renombra el archivo si ya existe en el destino
            if os.path.exists(destination_path):
                base_name, extension = os.path.splitext(file)
                destination_path = os.path.join(
                    base_path, f"{base_name}_copy{extension}"
                )

            shutil.move(source_path, destination_path)

        # Elimina carpetas vacías
        for dir in dirs:
            dir_path = os.path.join(root, dir)
            if not os.listdir(dir_path):
                os.rmdir(dir_path)

if __name__ == "__main__":
    # Cambia esta ruta por la ruta de tu pendrive o carpeta objetivo
    base_directory = input("Introduce la ruta de la carpeta principal: ").strip()
    
    if os.path.exists(base_directory):
        flatten_folders(base_directory)
        print("Archivos movidos y carpetas eliminadas correctamente.")
    else:
        print(f"La ruta '{base_directory}' no existe. Verifica e intenta de nuevo.")
