import logging

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)
### Punto numero 2
dictionary = {'nombre': 'Juan', 'edad': 30}
try:
    address = dictionary['direccion']
except KeyError:
    logging.info('La clave "direccion" no existe en el diccionario.')
    address = 'No disponible'
logging.info(address)