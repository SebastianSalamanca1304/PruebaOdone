from collections import defaultdict
import logging

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)
### Punto numero 1
def group_products(products):
    gropus = defaultdict(lambda: defaultdict(lambda: defaultdict(list)))
    for product in products:
        manufacturer = product['manufacturer']
        category = product['Categoría']
        genre = product['Género']

        gropus[manufacturer][category][genre].append(product)
    return convert_to_dic(gropus)

def convert_to_dic(d):
    """Convierte todos los defaultdicts a dicts recursivamente."""
    if isinstance(d, defaultdict):
        d = {k: convert_to_dic(v) for k, v in d.items()}
    return d

products = [
    {'Nombre': 'Zapatos XYZ', 'Código de barras': '8569741233658', 'manufacturer': 'Deportes XYZ', 'Categoría': 'Zapatos', 'Género': 'Masculino'},
    {'Nombre': 'Zapatos ABC', 'Código de barras': '7452136985471', 'manufacturer': 'Deportes XYZ', 'Categoría': 'Zapatos', 'Género': 'Femenino'},
    {'Nombre': 'Camisa DEF', 'Código de barras': '5236412896324', 'manufacturer': 'Deportes XYZ', 'Categoría': 'Camisas', 'Género': 'Masculino'},
    {'Nombre': 'Bolso KLM', 'Código de barras': '5863219635478', 'manufacturer': 'Carteras Hi-Fashion', 'Categoría': 'Bolsos', 'Género': 'Femenino'}
]

result = group_products(products)
logging.info('Resultado: %s', result)