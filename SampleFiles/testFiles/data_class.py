from dataclasses import dataclass

@dataclass # @dataclass Decoration(same as java->Annotation)
class Product:
    weight: int = None
    price: float = None

apple = Product()
apple.price = 10

