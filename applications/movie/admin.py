from django.contrib import admin
from django.utils.safestring import mark_safe

from applications.movie.models import Movie, MovieImage
from applications.review.models import Like


class InlineMovieImage(admin.TabularInline):
    model = MovieImage
    extra = 1
    fields = ['image', ]

# class InlineReviewImage(admin.TabularInline):
#     model = Like
#     extra = 1
#     fields = ['like', ]

class MovieAdminDisplay(admin.ModelAdmin):
    inlines = [InlineMovieImage, ]
    list_display = ('title', 'image')
    # list_editable = ('in_stock', 'quantity')
    search_fields = ('title',)
    list_filter = ('category',)

    def image(self, obj):
        img = obj.image.first()
        if img:
            return mark_safe(f'<img src="{img.image.url}" width="80" height="80" style="object-fit: contain"/>')
        else:
            return ""


admin.site.register(Movie, MovieAdminDisplay)


