from django.db import models
from blog.abstract import BaseModel, ActiveModel,OrderModel
from django.utils.translation import gettext_lazy as _


class Author(BaseModel):
    full_name = models.CharField(max_length=100, verbose_name=_("full_name"))
    image = models.ImageField(upload_to='media/blog/author/%Y/%m/%d', verbose_name=_("image"))

    def __str__(self) -> str:
        return self.full_name
    
    class Meta:
        verbose_name = _("Author")
        verbose_name_plural = _("1.Authors")

        
class Post(BaseModel):
    title = models.CharField(max_length=100, help_text=_("write title"), verbose_name=_("title"))
    author = models.CharField(max_length=30, help_text=_("write author name"), verbose_name=_("author"))
    description = models.TextField(verbose_name=_("description"))
    article = models.CharField(max_length=255, verbose_name=_("article"))
    tag = models.ManyToManyField("Tags", verbose_name=_("tag"), related_name="posts")
    image = models.ImageField(upload_to='media/', verbose_name=_("image"))

    def __str__(self) -> str:
        return f"{self.title[:15]}"
    
    class Meta:
        verbose_name = _("Post")
        verbose_name_plural = _("2.Posts")
