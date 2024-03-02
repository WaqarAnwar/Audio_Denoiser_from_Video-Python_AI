# Audio_Denoiser_from_Video-Python_AI

Hello! This is a basic noise removing script that uses Python and AI technology DeepFilterNet to remove audio noise from a video. 
Furthermore it uses moviepy library to merge audio and video.

### Pros:

Normally it takes 4 to 5 hours to remove noise from a video as first you have to split audio and video, 
then remove noise from the audio then merge audio and video back. All of it has to be done manually. 
But this method is faster and it lowers the time from 4-8 hours to 1-2 hours per video
(for a video that is around 2 hours long). And it does all of it in one go. Just input a video and it will output a denoised video.
The time to generate the video is much shorter as compared to some conventional video editors these days. Plus it uses AI technology to denoise 
and produce an enhanced speech video.

### Cons: 

Sometimes it might give unexpected results based on audio input. This is due to the DeepFilterNet library.
Also sometimes the audio and video go out of sync after 45 minutes if the video
is more than 45 minutes long. This is due to moviepy library not syncing the audio and video correctly.


### Noisy Audio Plot:

### Denoised Audio Plot:

## Usage

Make virtual environment and then activate that virtual environment.

Then run:
```bash
  pip install -r requirements.txt
```
Then copy your video to the current directory where these files are located.

Then to remove noise from a video "video.mp4", run:
```bash
  python denoiser.py "video.mp4"
```
And it will successfully remove noise from the provided video and generate a new denoised video.

## Contributing

Pull requests are welcome. Please try to open an issue first to discuss what you would like to change.

