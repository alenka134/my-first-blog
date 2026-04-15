from django.conf import settings
from django.db import models
from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()

    # 🎬 NEW: video field
    video = models.FileField(upload_to='videos/', blank=True, null=True)
    
    # 📸 Images (up to four optional screenshots/photos)
    image = models.ImageField(upload_to='images/', blank=True, null=True)
    image2 = models.ImageField(upload_to='images/', blank=True, null=True)
    image3 = models.ImageField(upload_to='images/', blank=True, null=True)
    image4 = models.ImageField(upload_to='images/', blank=True, null=True)

    # 🎬 Second video field
    video2 = models.FileField(upload_to='videos/', blank=True, null=True)

    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    @property
    def gallery_images(self):
        """Non-empty image fields in display order (for templates)."""
        imgs = []
        for name in ('image', 'image2', 'image3', 'image4'):
            f = getattr(self, name)
            if f:
                imgs.append(f)
        return imgs

    def __str__(self):
        return self.title