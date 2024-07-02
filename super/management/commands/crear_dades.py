# crear_dades.py

from django.core.management.base import BaseCommand
from django.utils import timezone
from faker import Faker
from random import randint, choice
from super.models import Product, Customer, Order, OrderItem
from django.db import transaction

faker = Faker(["es_CA", "es_ES"])

# Lista de nombres comunes de productos de supermercado
PRODUCT_NAMES = [
    "Leche",
    "Pan",
    "Arroz",
    "Fideos",
    "Aceite de oliva",
    "Café",
    "Azúcar",
    "Harina",
    "Sal",
    "Atún en lata",
    "Jabón de lavandería",
    "Papel higiénico",
    "Pañales",
    "Pasta dental",
    "Champú",
    "Cereal",
    "Galletas",
    "Salsa de tomate",
    "Sopa instantánea",
    "Detergente",
    "Agua embotellada",
    "Refresco",
    "Queso",
    "Yogur",
    "Huevos",
    "Cerveza",
    "Vino",
    "Chocolate",
    "Helado",
    "Cereal",
    "Mermelada",
    "Aceitunas",
    "Conservas",
    "Vinagre",
    "Salsa de soya",
    "Caramelos",
    "Pipas",
    "Frutos secos",
    "Cerveza artesanal",
    "Pimientos en conserva"
]

# Lista de nombres de marcas asociadas a productos
BRAND_NAMES = [
    "Nestlé",
    "Kellogg's",
    "Coca-Cola",
    "Pepsi",
    "Knorr",
    "Danone",
    "L'Oréal",
    "Colgate",
    "Nike",
    "Adidas",
    "Sony",
    "Samsung",
    "Apple",
    "Microsoft",
    "Lenovo",
    "HP",
    "Dell",
    "Canon",
    "Toyota",
    "Honda",
    "Volkswagen",
    "Mercedes-Benz",
    "BMW",
    "Audi"
]

def generate_product():
    product_code = faker.unique.uuid4()
    name = choice(PRODUCT_NAMES) 
    if faker.boolean(chance_of_getting_true=50):  
        brand = choice(BRAND_NAMES)
        name = f"{brand} {name}"
    description = faker.text()
    price = faker.random_number(digits=3)
    stock = randint(1, 100)
    product = Product(product_code=product_code, name=name, description=description, price=price, stock=stock)
    return product

def generate_customer():
    first_name = faker.first_name()
    last_name = faker.last_name()
    email = faker.unique.email()
    phone_number = faker.phone_number()
    customer = Customer(first_name=first_name, last_name=last_name, email=email, phone_number=phone_number)
    return customer

def generate_order(customer):
    order = Order(customer=customer, date_ordered=timezone.now(), complete=False)
    return order

def generate_order_item(order):
    product = generate_product()
    product.save()
    quantity = randint(1, 10)
    order_item = OrderItem(product=product, order=order, quantity=quantity)
    return order_item

class Command(BaseCommand):
    help = 'Genera datos ficticios de ventas'

    def handle(self, *args, **options):
        # Generar y guardar productos
        for _ in range(20):  # Generar más productos
            product = generate_product()
            product.save()
            self.stdout.write(self.style.SUCCESS(f"Producto creado: {product.name}"))

        # Generar y guardar clientes
        for _ in range(10):  # Generar más clientes
            customer = generate_customer()
            customer.save()
            self.stdout.write(self.style.SUCCESS(f"Cliente creado: {customer.first_name} {customer.last_name}"))

        # Generar y guardar órdenes con elementos de órdenes
        for _ in range(100):  # Generar más órdenes
            customer = generate_customer()
            customer.save()
            order = generate_order(customer)
            order.save()
            self.stdout.write(self.style.SUCCESS(f"Orden creada: {order.id}"))
            for _ in range(2):
                order_item = generate_order_item(order)
                order_item.save()
                self.stdout.write(self.style.SUCCESS(f"  Elemento de orden creado: {order_item.product.name}"))

