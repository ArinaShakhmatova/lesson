from django.contrib import admin
from .models import Adverisement



class AdvertisementAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'title', 'description', 'price', 'created_date', 'auction', 'updated_date',  "image_form"]
    list_filter = ['auction', 'created_ad']
    actions = ['make_auction_as_false', 'make_auction_as_true']

    fieldsets = (
        ('Общее', {
            "fields": ("title", "description", "user", "image")
        }),
        ("Финансы", {
            "fields": ("price", "auction"),
            "classes": ["collapse"]
        })
    )

    @admin.action(description='Убрать возможность торга')
    def make_auction_as_false(self, request, queryset):
        queryset.update(auction=False)

    @admin.action(description='Добавить возможность торга')
    def make_auction_as_true(self, request, queryset):
        queryset.update(auction=True)

admin.site.register(Adverisement, AdvertisementAdmin)