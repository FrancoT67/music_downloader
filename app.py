from flask import Flask, request, jsonify 
import subprocess
import os

app = Flask(__name__)

# Carpeta donde se guardarán los archivos descargados
DOWNLOAD_FOLDER = "downloads"
# DOWNLOAD_FOLDER = "G:\\"
os.makedirs(DOWNLOAD_FOLDER, exist_ok=True)

@app.route('/download', methods=['POST'])
def download_playlist():
    data = request.get_json()
    playlist_url = data.get('url')

    if not playlist_url:
        return jsonify({"success": False, "error": "No URL provided."}), 400

    try:
        # Comando para descargar en formato MP3
        command = [
            "yt-dlp",
            "--extract-audio",
            "--audio-format", "mp3",
            "--output", f"{DOWNLOAD_FOLDER}/%(title)s.%(ext)s",
             "--cookies", "youtube_cookies.txt","--ignore-errors",
            playlist_url
        ]

        # Ejecutar el comando
        subprocess.run(command, check=True)

        return jsonify({"success": True})
    except subprocess.CalledProcessError as e:
        return jsonify({"success": False, "error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
