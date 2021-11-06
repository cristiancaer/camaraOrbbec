from ventana import ventana
from openni import openni2
from openni import _openni2 as c_api
import numpy as np
import cv2                                                                                                                                                                                                                                                                                                                                                                                          
import time 
from ttictoc import tic, toc 

# path to save images
path=" "


# variables
interface=ventana("presionar f: empezar/pausar de guardar. c: detener y salir")
#flag
save=False
idImagen=0
# img roi

# Initialize the depth device
openni2.initialize()
dev = openni2.Device.open_any()

# Start the depth stream
depth_stream = dev.create_depth_stream()
depth_stream.start()
depth_stream.set_video_mode(c_api.OniVideoMode(pixelFormat = c_api.OniPixelFormat.ONI_PIXEL_FORMAT_DEPTH_100_UM, resolutionX = 640, resolutionY = 480, fps = 30))
rgb_stream = dev.create_color_stream()
rgb_stream.set_video_mode(c_api.OniVideoMode(pixelFormat=c_api.OniPixelFormat.ONI_PIXEL_FORMAT_RGB888, resolutionX= 640, resolutionY = 480, fps = 30))
rgb_stream.start()

def get_rgb():                                                                  
    bgr   = np.frombuffer(rgb_stream.read_frame().get_buffer_as_uint16(),dtype=np.uint8).reshape(480,640,3)
    rgb   = cv2.cvtColor(bgr,cv2.COLOR_BGR2RGB)
    return rgb 
def get_depth():
    depth = np.frombuffer(depth_stream.read_frame().get_buffer_as_uint16(),dtype=np.uint16)
    depth.shape = (480, 640)
    # cv2.imshow("h",depth)
    depth = cv2.merge([depth,depth,depth])# por alguna razon, cuando no se une en 3 cales, se pierde información de la imagen.
    return depth
while True:
    tic()
    rgb = get_rgb()    
    depth=get_depth()
    #pseudo color
    depth_copy=cv2.cvtColor(depth, cv2.COLOR_BGR2GRAY)/100
    depth_copy=depth_copy.astype(np.uint8)    
    depth_color = cv2.applyColorMap(depth_copy, cv2.COLORMAP_JET)#COLORMAP_JET##COLORMAP_PINK
    key = cv2.waitKey(1) & 0xFF
    # If the 'c' key is pressed, break the while loopc
    if key == ord("c"):
                   break
    #save. 1 to save. o to idle
    if key == ord("f"):
        save=not save


    infodepth="Depth...."
    if save:
        infodepth+="saving"
        idImagen+=1
        hora=time.strftime("%m_%d_%Y_%H_%M_%S",time.localtime())
        rgb_paht="{}RGB_{}_{}.png".format(path,idImagen,hora)
        depth_path="{}depth_{}_{}.png".format(path,idImagen,hora)
        cv2.imwrite(format(depth_path),depth)
        cv2.imwrite(format(rgb_paht),rgb)
        
    interface.visualizar([rgb,depth_color],rgb.shape[0:2],1,2,["rgb;1/fps:{0:.3f}".format(toc()),infodepth])
    

openni2.unload()

cv2.destroyAllWindows()

