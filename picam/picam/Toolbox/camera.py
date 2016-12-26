import picamera
import os,os.path
import threading
from picam.DataModel import TimeModel



""" Camera Data model """
class CameraModel(object):
    """Parameters used for the camera """

    def __init__(self):
        """ initialize this camera model """
        self.Now = TimeModel.Date()
        self.SunDown = TimeModel.Date()
        self.SleepDuration = 15
        self.ImageDirectory = "picam/static/timelapse/"

""" Camera ToolBox """
class CameraToolbox(object) :
    """ interface for using the camera """

    def __init__(self):
        self.parameters = CameraModel()
        self.do = picameraInterface(self.parameters)

    def Start_Capture(self) :
         self.do.SnapShot()



""" Pi camera interface """
class picameraInterface(object) :
    """interface for the picamera """

    def __init__(self, parameters):
        self.parameters = parameters
        self.picam = picamera.PiCamera()
        self.picam.resolution = (1024,768)


    #FUNCTIONS


    def GetLastImage(self):
        
         count = len([f for f in os.listdir(self.parameters.ImageDirectory) if os.path.isfile(os.path.join(self.parameters.ImageDirectory, f))])
         countString = str(count-1)

         #check if we laready launch the timelapse
         if count == 0 :
             return 'images/SadSmiley.jpeg'
         else :
            return 'timelapse/image_'+countString+'.jpg'



    def SnapShot(self) :
         t = threading.Timer(self.parameters.SleepDuration,self.SnapShot)
         t.start()
         count = len([f for f in os.listdir(self.parameters.ImageDirectory) if os.path.isfile(os.path.join(self.parameters.ImageDirectory, f))])
         countString = str(count)
         self.picam.capture(self.parameters.ImageDirectory+'image_'+countString+'.jpg')


