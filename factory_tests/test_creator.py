import unittest 
import factory.product
import factory.creator


class TestCreator(unittest.TestCase):
    def test_creates_product(self):
        class TestProduct(factory.product.Product): 
            __PRODUCT_KEY__ = "-test-product-key-"

        instance = factory.creator.Creator().create("-test-product-key-")
        assert isinstance(instance, TestProduct), \
            f"Actual object is of instance {type(instance)}"

    def test_none_for_invalid_key(self):
        assert factory.creator.Creator().create("-invalid-key-") is None
    
    def test_passes_args(self):
        class TestProduct(factory.product.Product): 
            __PRODUCT_KEY__ = "-test-product-key-"

            def __init__(self, value1, value2=None, value3=None):
                super().__init__()
                self.value1 = value1
                self.value2 = value2
                self.value3 = value3
        
        instance = factory.creator.Creator().create("-test-product-key-", 1, value3=3)
        assert instance.value1 == 1, f"Actual value is {instance.value1}"
        assert instance.value2 is None, f"Actual value is {instance.value3}"
        assert instance.value3 == 3, f"Actual value is {instance.value4}"
    
    def test_supports_multiple_factories(self):
        class TestProduct(factory.product.Product): 
            __PRODUCT_KEY__ = "-test-product-key-"
            __FACTORY_KEY__ = "-test-factory-key-"

        instance = factory.creator.Creator(TestProduct.__FACTORY_KEY__).create(TestProduct.__PRODUCT_KEY__)
        assert isinstance(instance, TestProduct), \
            f"Actual object is of instance {type(instance)}"
    
    def test_adds_product_only_to_one_factory(self):
        class TestProduct(factory.product.Product): 
            __PRODUCT_KEY__ = "-test-product-key-"
            __FACTORY_KEY__ = "-test-factory-key-"

        class TestProduct2(factory.product.Product): 
            __PRODUCT_KEY__ = "-other-test-product-key-"
            __FACTORY_KEY__ = "-other-test-factory-key-"

        instance = factory.creator.Creator("-other-test-factory-key-").create(TestProduct.__PRODUCT_KEY__)
        assert instance is None, \
            f"Actual object is of instance {type(instance)}"
        

if __name__ == '__main__':
    unittest.main()
