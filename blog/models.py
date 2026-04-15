from django.conf import settings
from django.db import models
from django.utils import timezone


def _normalize_title_for_display(text):
    """Map Unicode Mathematical Bold Latin (common ‘fancy’ titles) to plain ASCII so webfonts apply."""
    if not text:
        return text
    out = []
    for ch in text:
        o = ord(ch)
        if 0x1D400 <= o <= 0x1D419:
            out.append(chr(ord('A') + (o - 0x1D400)))
        elif 0x1D41A <= o <= 0x1D433:
            out.append(chr(ord('a') + (o - 0x1D41A)))
        else:
            out.append(ch)
    return ''.join(out)


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

    def save(self, *args, **kwargs):
        self.title = _normalize_title_for_display(self.title)
        super().save(*args, **kwargs)

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