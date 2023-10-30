from products import *
from salesoperation import *


kop_bar = Chocolate(45.32,"A01392","Kopenhagen","Brasil","Tablete Clássico",42,100)

my_shoe = Shoe(450.99,"S01221",42,"Puma")

my_bottle = Bottle(99.99,"P03444","Termolar",1000)
    
my_prod1 = Chocolate(10.91,"SO0021",Brand.LINDT.value,'Suiça',"Ao leite",55,45)
print(my_prod1)

my_inv = Inventory()
my_inv.add_item(my_prod1.barcode,100)
my_inv.summary()
print("* Queima de Estoque *")
my_inv.sell_product(my_prod1.barcode)
my_inv.summary()
print("* Repondo o Estoque, em 999 unidades *")
my_inv.restock_product(my_prod1.barcode,999)
my_inv.summary()
