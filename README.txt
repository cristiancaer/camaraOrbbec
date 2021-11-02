# camaraOrbbec
Conexion camara orbbec
intallar requisitos/complementos de openni2
-GCC 4.x:
sudo apt-get install g++
-LibUSB 1.0.x:
sudo apt-get install libusb-1.0-0-dev
-FreeGLUT3
sudo apt-get install freeglut3-dev
-Doxygen
sudo apt-get install doxygen
-GraphViz
 sudo apt-get install graphviz
-se aconseja crear una carpeta en home. en esta carpeta se recomienda descargar e installar TODOS -los progrmas que se necesesiten
-Intallar astraSDK
https://orbbec3d.com/develop/
-abrir archivo descargado y buscar la carpeta install, dentro de la carpeta install abrir terminal y ejecutar los siguites comandos
sudo chmod a+x install.sh
sudo ./install
cuando se ejecuta la segunda linea parece un mensaje de recomendacion en nuestro caso fue:
NOTES:
We suggest adding the following lines to your .bash_profile or .bashrc

export ASTRA_SDK_INCLUDE=/home/estufab4/install/AstraSDK-v2.0.18-05cfa52534-20191108T074013Z-Linux/install/include
export ASTRA_SDK_LIB=/home/estufab4/install/AstraSDK-v2.0.18-05cfa52534-20191108T074013Z-Linux/install/lib

para abrir el archivo .bashrc
sudo nano $HOME/.bashrc
se debe colocar la linea despues del primer parrafo. ctr x para salir, pedirá confirmar, luego de confirmar se presiona enter para guardar.



-installar openni
Descarga drivers Orbbec astra.
se puede encontrar una copia en los siguientes enlaces
https://www.dropbox.com/sh/ou49febb83m476d/AADqCQuI3agPOdhyuihl0NHMa?dl=0
https://github.com/cristiancaer/camaraOrbbec/blob/main/OpenNI-Linux-x64-2.3.zip
Seleccionar el sistema operativo Linux, abrir la carpeta e instalar con las siguientes líneas de código
unzip archivo.zip
BUSCAR OpenNI-Linux-x64-2.3
descomprimir
abrir carpeta, y ejecutar
sudo chmod a+x install.sh
sudo ./install.sh
al ejecutar la segunda linea se creara el archivo OpenNIDevEnvironment, este archivo se debe ejecutar con el  siguientes lineas de comando
source OpenNIDevEnvironment
nota: para evitar tener que ejecutar OpenNIDevEnvironment,se abre el archivo OpenNIDevEnvironment y se copia las lineas de codigo en el achivo .bash_profile or .bashrc
Installar libreria en python
pip install openni
