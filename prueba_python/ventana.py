import numpy as np
import cv2
# la clase es utilizada para mostrar imagenes como un subplo
# todas las imagenes deben tener la misma dimension
# en el contructor solo se inicializa una ventana sin ningun elemento
# la función visualizar permite cargar una lista de imagenes y mostrarlas como un subplot.
# el subplot se visualizara hasta que se presione una tecla
# nota: cerrarla  con el simbolo de cerrar de la ventana puede generar inconvenientes, si se desea cerrar solo pulsar una tecla hasta llega al fianal de la visualización
class ventana():
    def __init__(self,nombre):
        #Constantes de instancia
        self.nombre=nombre
        cv2.namedWindow(nombre,flags=cv2.WINDOW_NORMAL)# establecer nombre de la ventana, y la opción de cambiar el tanaño manualmente.
        # margenes de cada imagen
        self.margen_superior=50
        self.margen_inferior=20
        self.margen_izquierdo=20
        self.margen_derecho=20 
        self.font = cv2.FONT_HERSHEY_SIMPLEX 
        # escala de la fuente
        self.fontScale = 1
        # color blanco
        self.color = (255, 255, 255) 
        # distancia entre letra
        self.thickness = 2
        # posiciion del titulo
        self.org = (self.margen_izquierdo,int(self.margen_superior/2))
        #variables de clase
        # dimensiones de la imagen    
        self.alto=0
        self.ancho=0
        
        
    #list_img: una lista con las imagenes a graficar, las imagenes deben tener la misma dimensión
    def visualizar(self,list_img,shape,nf,nc,titulos=[]):
        #dimensiones de las imagenes de entrada. deben ser la mismas para todas
        self.alto,self.ancho=shape# 
        #dimesiones de las imagenes luego de agregarles el margen
        self.ancho=self.ancho+self.margen_izquierdo+self.margen_derecho
        self.alto=self.alto+self.margen_superior+self.margen_inferior
        #numero de imagenes entregadas en la lista
        n=len(list_img)
       
        #
        for i in range(n):
            #agregar marco
            list_img[i] = cv2.copyMakeBorder(list_img[i], self.margen_superior, self.margen_inferior, self.margen_izquierdo, self.margen_derecho, cv2.BORDER_CONSTANT) 
            
            #añadir titulo
            if len(titulos)==n:
                list_img[i]=cv2.putText(list_img[i],titulos[i], self.org, self.font,self.fontScale, self.color, self.thickness, cv2.LINE_AA)
        # completar plot con imagenes negras
        for i in range(nf*nc-n):
            list_img.append(np.zeros((self.alto,self.ancho,3),dtype=np.uint8))
        # comvertir lista en array para poder estructurarla en la forma del plot, todas las imagenes deben tener la misma dimensión  
        list_img=np.array(list_img)
        
        list_img=list_img.reshape(nf,nc,self.alto,self.ancho,3)
        #unir imagenes por fila
        filas=[]
        for i in range(nf):
            img=np.hstack(list_img[i])
            filas.append(img)
        #unir filas    
        filas=np.array(filas)
        plot=np.vstack(filas)
        # mostrar imagen final  
        cv2.imshow(self.nombre, plot,)
 
