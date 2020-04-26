# ImageNoiseGenerator
Python noise images/videos generator.

# Configuration
## config.py
* You can set resolution of images by changing the **image_resolution** variable.
* Destination folder where the program will save images can be changed by setting **dest** variable with your own path.
* To define amount of images you can change **images_amount** variable.
* To set the output format of image change **img_format**.
* **video_name** variable defines an output video name.
* To change the framerate of generated video change **framerate** variable

# Requirements
You need to install opencv for python to use this project.

To install opencv library run ```pip install opencv-python```
# How to use
Run ```py noise_generator.py``` to generate images with noise.

After the images are created you can generate a video from them.

Run ```py video_generator.py``` to generate .avi video with your images as frames.
