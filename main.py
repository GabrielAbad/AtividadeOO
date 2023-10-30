from products import *
from salesoperation import *


# Chocolate de exemplo
choc_bar = Chocolate(45.32,"A01392",Brand.NESTLE.value,"Brasil",'crunch',42,100)
print(choc_bar,'\n')

# Sapato de exemplo
my_shoe = Shoe(450.99,"S01221",42,Brand.ADIDAS.value)
print(my_shoe,'\n')

# Garrafa de exemplo
my_bottle = Bottle(99.99,"P03444",Brand.TERMOLAR.value,1000)
print(my_bottle,'\n')

# Cria inventário vazio
my_inv = Inventory()

# Adiciona 100 barras de chocolate iguais e mostra o inventário
my_inv.add_item(choc_bar.barcode,100)
my_inv.summary()

print('\n',"* Queima de Estoque *")
my_inv.sell_product(choc_bar.barcode)
my_inv.summary()

print('\n',"* Repondo o Estoque, em 999 unidades *")
my_inv.restock_product(choc_bar.barcode,999)
my_inv.summary()