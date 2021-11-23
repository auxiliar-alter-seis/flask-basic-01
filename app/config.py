import os

#### Quitar el DEBUG = True para el servidor en produccion

#### se debe configurar el DEBUG = False en config.py para que funcione SSLify

#### la longitud de la SECRET_KEY si es muy grande hace que el servidor sea mas lento

class Configuration(object):
      APPLICATION_DIR = os.path.dirname(os.path.realpath(__file__))
      ##DEBUG = True
      DEBUG = False
      SECRET_KEY = 'MiLlaveSecreta1234'
      
      STATIC_DIR = os.path.join(APPLICATION_DIR, 'static')
      IMAGES_DIR = os.path.join(STATIC_DIR, 'images')

      IMGS_USERS = os.path.join(STATIC_DIR, 'users') ##imagenes de usuarios
      ALLOWED_IMGS = set(['jpg', 'jpeg', 'png']) ##por seguridad solo estas extensiones