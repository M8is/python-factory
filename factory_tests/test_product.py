import unittest 
import factory.product


class TestProductWatcher(unittest.TestCase):
    def test_does_not_register_without_key(self):
        class TestProduct(factory.product.Product): 
            pass

        assert TestProduct not in factory.product.ProductWatcher.__get_products__().values(), \
            "Registered products: {}".format(factory.product.ProductWatcher.__get_products__())

    def test_registers_to_default_factory(self):
        key = "-test-product-key-"
        class TestProduct(factory.product.Product): 
            __PRODUCT_KEY__ = key

        assert (key, TestProduct) in factory.product.ProductWatcher.__get_products__().items(), \
            "Registered products: {}".format(factory.product.ProductWatcher.__get_products__())
    
    def test_does_not_register_with_none_key(self):
        class TestProduct(factory.product.Product): 
            __PRODUCT_KEY__ = None

        assert TestProduct not in factory.product.ProductWatcher.__get_products__().values(), \
            "Registered products: {}".format(factory.product.ProductWatcher.__get_products__())

    def test_registers_to_custom_factory(self):
        factory_key = "-test-factory-key-"
        product_key = "-test-product-key-"
        class TestProduct(factory.product.Product): 
            __FACTORY_KEY__ = factory_key
            __PRODUCT_KEY__ = product_key

        assert (product_key, TestProduct) in factory.product.ProductWatcher.__get_products__(factory_key).items(), \
            "Registered products: {}".format(factory.product.ProductWatcher.__get_products__(factory_key))
    
        


if __name__ == '__main__':
    unittest.main()
