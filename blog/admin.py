from django.contrib import admin
from .models import Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "published_date")
    fieldsets = (
        (None, {"fields": ("author", "title", "text")}),
        (
            "Media",
            {
                "fields": (
                    "video",
                    "video2",
                    "image",
                    "image2",
                    "image3",
                    "image4",
                ),
            },
        ),
        ("Dates", {"fields": ("created_date", "published_date")}),
    )