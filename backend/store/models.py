from django.db import models


class myAbstractModel(models.Model):
    # auto fields:
    created = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Category(myAbstractModel):
    name = models.CharField(
        blank=False, max_length=64, help_text="Name for this category"
    )

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name_plural = "Categories"


class Item(myAbstractModel):
    name = models.CharField(blank=False, max_length=64, help_text="Name for the item")
    price = models.PositiveSmallIntegerField(help_text="Price in PLN")
    category = models.ForeignKey(
        Category, related_name="items", on_delete=models.PROTECT
    )
    main_image = models.ImageField()

    def __str__(self) -> str:
        return self.name


class Picture(myAbstractModel):
    picture = models.ImageField()
    item = models.ForeignKey(Item, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.picture.url
