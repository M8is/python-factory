from factory import product


class Creator:
    def __init__(self, factory_key=product.__DEFAULT_FACTORY_KEY__):
        self.factory_key = factory_key

    def create(self, key, *args, **kwargs):
        """
            Create a product. Returns None if no product is registered for the given key.
        """
        products = product.ProductWatcher.__get_products__(self.factory_key)
        if key in products:
            return products[key](*args, **kwargs)
        else:
            return None
