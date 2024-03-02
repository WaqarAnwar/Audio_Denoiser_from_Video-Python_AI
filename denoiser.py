import moviepy.editor as mp
import os
import sys
from df.enhance import enhance, init_df, load_audio, save_audio
from df.utils import download_file
from scipy.io import wavfile
from pydub import AudioSegment

def removeNoise(video_file):
    #get video file
    clip = mp.VideoFileClip(video_file)
    
    #save audio from that video file
    clip.audio.write_audiofile('temp.wav')

    rate, data = wavfile.read('temp.wav')

    #resolve error related to data should be floating point number
    data = data / 1.0

    # Load audio
    audio = AudioSegment.from_file('temp.wav')

    # Resample the audio to the target bitrate (48 kHz) because DeepFilterNet uses only 48kHz audio
    new_rate = 48000
    resampled_audio = audio.set_frame_rate(new_rate)
    
    # Save the resampled data to a new WAV file
    resampled_audio.export('temp_resampled.wav', format="wav")

    # Load default model
    model, df_state, _ = init_df()

    #Load audio
    audio, _ = load_audio('temp_resampled.wav', sr=df_state.sr())

    # Denoise the audio
    enhanced = enhance(model, df_state, audio)

    #write denoised audio to temp file
    save_audio("temp_denoised.wav", enhanced, df_state.sr())

    #get audio from saved file
    audio = mp.AudioFileClip('temp_denoised.wav')

    #merge denoised audio and video
    final_video = clip.set_audio(audio)

    #get file name from filename and its extension
    filename, ext = os.path.splitext(video_file)

    #write the video file
    final_video.write_videofile(f"{filename} denoised.mp4")

    #remove recently generated unnecessary files
    os.remove('temp.wav')
    os.remove('temp_resampled.wav')
    os.remove('temp_denoised.wav')

if __name__ == "__main__":
    video_file = sys.argv[1]
    removeNoise(video_file)