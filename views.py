import os

from django import get_version
from django.conf import settings
from django.shortcuts import render


def home(request):
    Obj1 = eCommerce
    Obj2 = eCommerce2
    context = {
        "debug": settings.DEBUG,
        "django_ver": get_version() + "PROBANDO" + Obj1.eCommerce_test,
        "python_ver": os.environ["PYTHON_VERSION"] + "MAS CAMBIOS" + Obj2.greetings 
    }

    return render(request, "pages/home.html", context)

class eCommerce:
  stock = {}
  cart = {}
  bill = 0
  eCommerce_test = "Se creo una instancia de la clase 1"

  def add_to_cart(self,product, qt):
    result = self.check_stock(product) #Funcion1 anidada
    if result == 0:
      res_update = self.update_stock(product,qt) #Funcion2 anidada
      if res_update == 1:
        if product in self.cart.keys():
          self.cart[product] += qt
        else:
          self.cart[product] = qt
        print(f"{qt} Producto {product} agregado\n")
      else: print(f"No hay inventario suficiente de {product} disponible\n")
    else: print(f"No hay {product} en stock\n")

  def check_stock(self,product):
    if product in self.stock.keys(): return 0
    else: return 1

  def update_stock(self,product,qt):
    if (self.stock[product] - qt) < 0: return 0
    else:
      self.stock[product] -= qt
      return 1

  def add_stock(self,product,qt):
    self.stock[product] = qt

################################################################################

class eCommerce2(eCommerce):
  greetings = "Bienvenido a la Tienda de Mario"

  def __init__(self):
    print(self.greetings)

  def status_order(self):
    print(f"Tu carrito tiene: \n")
    [print(f"{q} {p}s") for p,q in zip(self.cart.keys(),self.cart.values())]