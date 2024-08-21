from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.urls import reverse
from django.utils.text import slugify
# Create your models here.


class Tag(models.Model):
    caption = models.CharField(max_length=20)

    # class Meta:
    #     verbose_name_plural = "Tags"


class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email_adddress = models.EmailField()

    # def full_name(self):
    #     return f"{self.first_name} {self.last_name}"

    # class Meta:
    #     verbose_name_plural = "Authors"


class Post(models.Model):
    title = models.CharField(max_length=150)
    excerpt = models.CharField(max_length=200)
    image = models.CharField(max_length=100)
    date = models.DateField(auto_now=True)
    slug = models.SlugField(unique=True, db_index=True)
    content = models.TextField(validators=[MinValueValidator(10)])
    author = models.ForeignKey(
        Author, on_delete=models.SET_NULL, related_name="posts")
    tags = models.ManyToManyField(Tag)

    # def get_absolute_url(self):
    #     return reverse("book_detail", args=[self.slug])

    # def __str__(self):
    #     return f"{self.title} ({self.author})"

    # class Meta:
    #     verbose_name_plural = "Posts"
