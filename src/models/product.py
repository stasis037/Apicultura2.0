
from tortoise import fields, models

class ProductCategory(models.Model):
    id = fields.IntField(pk=True)
    name = fields.CharField(max_length=255, unique=True)
    description = fields.TextField(null=True)
    products: fields.ReverseRelation["Product"]

    class Meta:
        table = "product_categories"

class ProductType(models.Model):
    id = fields.IntField(pk=True)
    name = fields.CharField(max_length=255, unique=True)
    description = fields.TextField(null=True)
    products: fields.ReverseRelation["Product"]

    class Meta:
        table = "product_types"

class Product(models.Model):
    id = fields.IntField(pk=True)
    name = fields.CharField(max_length=255, index=True)
    description = fields.TextField(null=True)
    price = fields.FloatField()
    stock = fields.IntField(default=0)
    image_url = fields.CharField(max_length=255, null=True)
    category = fields.ForeignKeyField("models.ProductCategory", related_name="products")
    type = fields.ForeignKeyField("models.ProductType", related_name="products")

    class Meta:
        table = "products"
