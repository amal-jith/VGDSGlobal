from django.contrib import admin

from django.utils.safestring import mark_safe

from .models import FAQ, Testimonials, Order, Work, TeamMember, Rating, Blog, HeroImageSwiperOne, HeroImageSwiperTwo, HeroImageMobile


# Register your models here.


@admin.register(FAQ)
class FAQadmin(admin.ModelAdmin):
    list_display = ('question', 'created_at')
    ordering = ('-created_at',)

@admin.register(Testimonials)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ('name', 'date', 'trustpilot_url')
    list_filter = ('date',)
    search_fields = ('name', 'content')

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ("full_name", "email", "delivery_date", "created_at")
    readonly_fields = ("created_at",)


@admin.register(Work)
class WorkAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'image_preview', 'created_at')
    list_filter = ('category', 'is_important')
    search_fields = ('title',)

    def image_preview(self, obj):
        if obj.image:
            return mark_safe(f'<img src="{obj.image.url}" width="80" style="object-fit:contain;" />')
        return "-"
    image_preview.short_description = 'Preview'



@admin.register(TeamMember)
class TeamMemberAdmin(admin.ModelAdmin):
    list_display = ('name', 'designation', 'role', 'priority')
    ordering = ('priority',)

@admin.register(Rating)
class RatingAdmin(admin.ModelAdmin):
    list_display = ['value', 'updated_at']


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'date')



@admin.register(HeroImageSwiperOne)
class HeroImageSwiperOneAdmin(admin.ModelAdmin):
    list_display = ('id', 'image_preview', 'alt_text')
    readonly_fields = ('image_preview',)

    def image_preview(self, obj):
        if obj.image:
            return mark_safe(f'<img src="{obj.image.url}" style="max-height: 100px;" />')
        return "-"
    image_preview.short_description = 'Preview'


@admin.register(HeroImageSwiperTwo)
class HeroImageSwiperTwoAdmin(admin.ModelAdmin):
    list_display = ('id', 'image_preview', 'alt_text')
    readonly_fields = ('image_preview',)

    def image_preview(self, obj):
        if obj.image:
            return mark_safe(f'<img src="{obj.image.url}" style="max-height: 100px;" />')
        return "-"
    image_preview.short_description = 'Preview'


@admin.register(HeroImageMobile)
class HeroImageMobileAdmin(admin.ModelAdmin):
    list_display = ('id', 'image_preview', 'alt_text')
    readonly_fields = ('image_preview',)

    def image_preview(self, obj):
        if obj.image:
            return mark_safe(f'<img src="{obj.image.url}" style="max-height: 100px;" />')
        return "-"
    image_preview.short_description = 'Preview'