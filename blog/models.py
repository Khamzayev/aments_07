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


class Tags(models.Model):
    name = models.CharField(max_length=100, verbose_name=_("name"))

    def __str__(self) -> str:
        return self.name
    
    class Meta:
        verbose_name = _("Tag")
        verbose_name_plural = _("3.Tags")

class Comment(BaseModel):
    name = models.CharField(max_length=100, verbose_name=_("name"))
    email = models.EmailField(verbose_name=_("email"))
    comment = models.TextField(verbose_name=_("comment"))
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments', verbose_name=_("post"))

    def __str__(self) -> str:
        return f"{self.name}\n{self.email}\n{self.comment}"
    
    class Meta:
        verbose_name = _("Comment")
        verbose_name_plural = _("4.Comments")
        ordering = ['-created_at']        