from django.contrib import admin

from applications.review.models import Review, Like

admin.site.register(Review)





# class ProductAdminDisplay(admin.ModelAdmin):
#     inlines = [InlineReviewImage, ]
#     list_display = ('like', )
    # list_editable = ('in_stock', 'quantity')
    # search_fields = ('title',)
    # list_filter = ('category',)

    # def image(self, obj):
    #     img = obj.image.first()
    #     if img:
    #         return mark_safe(f'<img src="{img.image.url}" width="80" height="80" style="object-fit: contain"/>')
    #     else:
    #         return ""