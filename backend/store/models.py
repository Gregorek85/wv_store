from django.db import models
from django.core.validators import FileExtensionValidator

# from accounts.models import CustomUser


class Currency(models.Model):
    short_name = models.CharField(
        blank=False, max_length=64, help_text="Abbr for this currency (i.e. EUR)"
    )
    long_name = models.CharField(
        blank=False, max_length=64, help_text="Long name for this currency (i.e. Euro)"
    )
    relation_to_PLN = models.PositiveSmallIntegerField(
        help_text="Price in PLN for 1 in this currency"
    )

    def __str__(self) -> str:
        return f"{self.long_name} ({self.short_name})"


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


class HashTag(myAbstractModel):
    name = models.CharField(
        blank=False, max_length=64, help_text="Name for this category"
    )

    def __str__(self) -> str:
        return f"#{self.name}"


class Cart(myAbstractModel):
    paid = models.BooleanField(default=False)
    sent = models.BooleanField(default=False)
    # user = models.ForeignKey(
    #     CustomUser, on_delete=models.CASCADE, default=None, null=True
    # )

    def total_amount(self, currency):
        amount = 0
        for item in self.items:
            amount += item.price(currency)
        return amount


class Item(myAbstractModel):
    name = models.CharField(blank=False, max_length=64, help_text="Name for the item")
    description = models.TextField(
        default="Ten wspaniały..", help_text="Description of the item"
    )
    _price = models.PositiveSmallIntegerField(help_text="Price in PLN")
    category = models.ForeignKey(
        Category, related_name="items", on_delete=models.PROTECT
    )
    main_image = models.ImageField()
    video = models.FileField(
        null=True,
        blank=True,
        validators=[
            FileExtensionValidator(
                allowed_extensions=["MOV", "avi", "mp4", "webm", "mkv"]
            )
        ],
    )
    hashtags = models.ManyToManyField(HashTag, related_name="items")
    # Since this is vintage shop we always have only 1 quantity of the item.
    cart = models.ForeignKey(
        Cart,
        on_delete=models.SET_NULL,
        null=True,
        default=None,
        blank=True,
        related_name="items",
    )

    @property
    def price(self):
        user = self.cart.user
        if not user:
            return self._price
        currency = self.cart.user.currency
        if not currency:
            return self._price
        relation = currency.relation_to_PLN
        return round(self.price / relation, 2)

    def __str__(self) -> str:
        return self.name


class Picture(myAbstractModel):
    picture = models.ImageField()
    item = models.ForeignKey(Item, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.picture.url
