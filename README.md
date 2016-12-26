# PiLapse
Time Lapse for Raspberry : this is the Flask part code .. 


## Goal : 
Being able to take a timelapse from anywhere .

### Hardware : 
- raspberry pi3 
- a pi CAM
- any phone / cell / handy 
- a battery 

### Software :
1. Raspbian
2. a FTP

### Framework :
1. Flask
2. picam Python wrappers
3. OpenCV

## STEPS :
1. being able to take photo every 15 seconds ( done ) 
2. being able from a netork to watch the photos being taken , Flask... ( done) 
3. being able to expose the camera parameters : (20% done)
  - changing snapshot intervals
  - configuring time : ( time now, sundown ) 
  - configuring ISO / snapshot time lenght / and all the auto parameters of the webcam
4. using the raspberry as a hotspot and auto launch flask on start
5. Working on the battery : making the Pilapse self sufficient with a battery ( goal would be around 30 hours )
