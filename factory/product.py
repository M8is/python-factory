import factory

__DEFAULT_FACTORY_KEY__ = "__DEFAULT_FACTORY__"


class ProductWatcher(type):
    """
        Watches for newly registered products.
        Register products by subclassing Product.
    """
    __products = dict()

    def __init__(cls, name, bases, clsdict):
        if "__PRODUCT_KEY__" in clsdict and clsdict["__PRODUCT_KEY__"] is not None:
            factory_key = clsdict["__FACTORY_KEY__"] if "__FACTORY_KEY__" in clsdict else __DEFAULT_FACTORY_KEY__
            if factory_key not in ProductWatcher.__products:
                ProductWatcher.__products[factory_key] = dict()
            ProductWatcher.__products[factory_key][clsdict["__PRODUCT_KEY__"]] = cls
        super(ProductWatcher, cls).__init__(name, bases, clsdict)
    
    @staticmethod
    def __get_products__(factory_key = __DEFAULT_FACTORY_KEY__):
        return ProductWatcher.__products.get(factory_key, dict())

class Product(metaclass=ProductWatcher):
    """
        Subclass to register a new product to the factory.
        Please provide a key in the '__PRODUCT_KEY__' field, otherwise the product will not be registered.
        Optional: provide a factory key in '__FACTORY_KEY__' to enable multiple factories.
    """
    pass
