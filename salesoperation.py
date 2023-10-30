from products import *
from enum import Enum

class Brand(Enum):
    NIKE = "Nike"
    ADIDAS = "Adidas"
    REEBOK = "Reebok"
    COCA_COLA = "Coca-Cola"
    PEPSI = "Pepsi"
    NESTLE = "Nestlé"
    LINDT = "Lindt"

class Inventory():
    
    #Inicia uma lista vazia 
    def __init__(self):
        self.inv = []
    def add_item(self,barcode,amount):
        item = [barcode,amount]
        self.inv.append(item)
    
    # Mostra o que tem no inventário
    def summary(self):
        print(self.inv)
    
    # Vende um produto
    def sell_product(self, barcode):
       for product_array in self.inv:
           if barcode in product_array:
                self.inv.remove(product_array)
           else:
                raise ProductNotFoundError("Product not found in the inventory.")

    # Para devolver um produto    
    def return_product(self, barcode):
        self.inv.append(barcode)

    def restock_product(self, barcode, amount):
        # Supondo que a quantidade seja adicionada ao estoque
        item = [barcode,amount]
        self.inv.append(item)


class ProductNotFoundError(Exception):
    pass
#testando a estrutura de classes criada, exemplo

