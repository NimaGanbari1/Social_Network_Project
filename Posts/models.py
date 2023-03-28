from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth import get_user_model
User = get_user_model()


        
    


class Post(models.Model):
    title = models.CharField(verbose_name=_('title'), max_length=50)
    avatar = models.ImageField(verbose_name=_('avatar'),blank=True)
    user = models.ForeignKey(User, on_delete= models.CASCADE)
    caption = models.TextField(verbose_name=_('caption'),blank=True)
    is_active = models.BooleanField(default=True)
    is_public = models.BooleanField(default=True)
    create_time = models.DateTimeField(
        verbose_name=_("create time"), auto_now_add=True)
    update_time = models.DateTimeField(
        verbose_name=_("update time"), auto_now=True)
    
    class Meta:
        db_table = 'Posts'
        verbose_name = _('Post')
        verbose_name_plural = _('Posts')
          
class Post_File(models.Model):
    FILE_AUDIO = 1
    FILE_VIDEO = 2
    FILE_IMG = 3
    FILE_TYPES = (
        (FILE_AUDIO,_('audio')),
        (FILE_VIDEO,_('video')),
        (FILE_IMG,_('image'))
    )
    title = models.CharField(_("title"),max_length=50)
    file_type =models.PositiveSmallIntegerField(_("file type"), choices=FILE_TYPES)
    fil = models.FileField(_("file"),upload_to="files/%Y/%m/%d/")
    post = models.ForeignKey('Post',verbose_name=_("Post"), on_delete=models.CASCADE)
    is_enable = models.BooleanField(_("is enable"),default=True)
    create_time = models.DateTimeField(_("create time"),auto_now_add=True)
    update_time = models.DateTimeField(_("update time"),auto_now=True)
    
    class Meta:
        db_table = "files"
        verbose_name = _("file")
        verbose_name_plural = _("files")
        
    def __str__(self):
        return self.title    