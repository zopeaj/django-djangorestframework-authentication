from products.models import Product
from product.repository.ProductRepository import ProductRepository

class ProductService:
    def __init__(self, productRepository):
        self.productRepository = productRepository

    def saveProduct(self, product):
        pass

    def updateProduct(self, product, product_id):
        pass

    def deleteProduct(self, product_id):
        pass


productService = ProductService(ProductRepository(Product()))
