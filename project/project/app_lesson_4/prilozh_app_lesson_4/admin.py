from django.contrib import admin
from .models import Advertisement

# Register your models here.

from django.contrib import admin
from .models import Advertisement

# Register your models here.

class AdvertisementAdmin(admin.ModelAdmin):
    list_display = ['id','title','description',
                    'price','created_date','updated_date','get_html_image','image','auction','user']
    list_filter = ['auction','created_at']
    actions = ['make_auction_false','make_auction_true']
    fieldsets = (
        ('Общее',{
            'fields':('title','description','image','user')
        }),
        ('Финансы',{
            'fields':('price','auction'),
            'classes':['collapse','wide']

        })
    )
    @admin.action(description='Убрать возможность торга')
    def make_auction_false(self, request, queryset):
        queryset.update(auction=False)

    @admin.action(description='Добавить возможность торга')
    def make_auction_false(self, request, queryset):
        queryset.update(auction=True)


admin.site.register(Advertisement,AdvertisementAdmin)