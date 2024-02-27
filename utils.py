import subprocess

def convert_to_pcm_wav(input_file):
    output_file = input_file.replace('.mp3', '_pcm.wav')  # Adjust output file extension as needed
    try:
        subprocess.run(['ffmpeg', '-i', input_file, '-acodec', 'pcm_s16le', '-ar', '44100', output_file], check=True)
        print("Conversion to PCM WAV successful!")
        return output_file
    except subprocess.CalledProcessError as e:
        print("Conversion to PCM WAV failed:", e)
        return None