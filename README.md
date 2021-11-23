# flask-basic-01
Estructura básica de un proyecto en Flask


Después de clonar el proyecto se debe crear la carpeta para instalar el entorno virtual

$ cd flask-basic-01
$ mkdir vserver
$ virtualenv -p python3 vserver

Al crear el entorno virtual debemos activarlo

$ source vserver/bin/activate

Entramos a la carpeta del proyecto

$ cd app/

Instalamos las librerías para poder correr el servidor

$ pip3 install Flask flask_mysqldb

Ejecutamos el archivo app.py

$ python3 main.py