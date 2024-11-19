# pip install pytube
from pytube import YouTube

def download_youtube_video():
    try:
        # Solicita o link do vídeo
        video_url = input("Digite o link do vídeo do YouTube: ")
        yt = YouTube(video_url)
        
        # Exibe o título do vídeo
        print(f"Título do vídeo: {yt.title}")
        
        # Solicita o formato desejado
        print("\nEscolha o formato para download:")
        print("1. MP4 (Vídeo)")
        print("2. MP3 (Áudio)")
        choice = input("Digite o número da opção desejada (1 ou 2): ")
        
        if choice == "1":
            # Baixa o vídeo na melhor qualidade
            video_stream = yt.streams.get_highest_resolution()
            print("\nBaixando o vídeo na melhor qualidade disponível...")
            video_stream.download()
            print(f"Download concluído! O vídeo foi salvo como {video_stream.default_filename}.")
        
        elif choice == "2":
            # Baixa apenas o áudio em formato MP3
            audio_stream = yt.streams.filter(only_audio=True).first()
            print("\nBaixando o áudio...")
            downloaded_file = audio_stream.download()
            
            # Converte para MP3
            mp3_filename = downloaded_file.replace(".mp4", ".mp3")
            import os
            os.rename(downloaded_file, mp3_filename)
            print(f"Download concluído! O áudio foi salvo como {mp3_filename}.")
        
        else:
            print("Opção inválida. Tente novamente.")
    
    except Exception as e:
        print(f"Ocorreu um erro: {e}")

# Executa o programa
if __name__ == "__main__":
    download_youtube_video()
