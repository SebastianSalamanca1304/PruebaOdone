import logging

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)
### Punto numero 3
def calculate_discount(solds):
    if solds > 500:
        return 10
    elif 100 <= solds <= 500:
        return 5
    else:
        return 0

solds = [50, 150, 550]

for sold in solds:
    discount = calculate_discount(sold)
    logging.info('Para una venta de $%s, el descuento aplicable es del %s%%.', sold, discount)