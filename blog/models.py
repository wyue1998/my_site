from django.db import models
from django.urls import reverse
from django.core.validators import MinLengthValidator


# Create your models here.


class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email_address = models.EmailField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
class Tag(models.Model):
    caption = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True)
    

    def __str__(self):
        return self.caption

class Post(models.Model):
    title = models.CharField(max_length=100)
    excerpt = models.CharField(max_length=200, null=True)
    # image = models.CharField(max_length=100, default="")
    date = models.DateField(auto_now=True)
    slug = models.SlugField(max_length=100, unique=True, null=True) #Both unique=True and SlugField db_index=True by default
    content = models.TextField(validators=[MinLengthValidator(10)])
    author = models.ForeignKey("Author", on_delete=models.SET_NULL, null=True, related_name="posts")
    tags = models.ManyToManyField(Tag, related_name="posts", blank=True)
    image = models.ImageField(upload_to="images/", null=True, blank=True)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("get_post", args=[self.slug])