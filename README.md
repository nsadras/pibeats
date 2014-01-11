Pi Beats
========
+ An LED Music visualizer, based on Juliana Pena's [arduino soundlight project](https://gist.github.com/limitedmage/2628477)

Instructions
-----------
+ Run `visualize_client.py` on the computer playing music, and `visualize_server.py` on the raspberry pi
+ In pulse audio volume control, in the recording tab, set the input of the client to the internal audio monitor

Client
------
+ takes raw audio data from the system recording device
    - make sure you set this recording device as the monitor of your internal audio
+ performs fft using `numpy`, calculates intensity for the specified number of frequency bins
+ sends frequency domain data to the server using python's `socket` library

Server
------
+ use `RPi.GPIO` to make LED's respond to fft data
