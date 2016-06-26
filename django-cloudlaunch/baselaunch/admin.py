from django.contrib import admin
import nested_admin

from baselaunch import forms
from baselaunch import models


class AppVersionCloudConfigInline(nested_admin.NestedTabularInline):
    model = models.ApplicationVersionCloudConfig
    extra = 1


class AppVersionInline(nested_admin.NestedStackedInline):
    model = models.ApplicationVersion
    extra = 0
    inlines = [AppVersionCloudConfigInline]


class AppAdmin(nested_admin.NestedModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
    inlines = [AppVersionInline]


class CloudImageInline(admin.StackedInline):
    model = models.CloudImage
    extra = 1


class CloudAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
    inlines = [CloudImageInline]


class EC2Admin(admin.ModelAdmin):
    # Hide this model from main app Admin page
    # http://stackoverflow.com/questions/2431727/django-admin-hide-a-model
    get_model_perms = lambda self, req: {}


class S3Admin(admin.ModelAdmin):
    # Hide this model from main app Admin page
    # http://stackoverflow.com/questions/2431727/django-admin-hide-a-model
    get_model_perms = lambda self, req: {}


class AWSCredsInline(admin.StackedInline):
    model = models.AWSCredentials
    form = forms.AWSCredentialsForm
    formset = forms.DefaultRequiredInlineFormSet
    extra = 1


class OSCredsInline(admin.StackedInline):
    model = models.OpenStackCredentials
    form = forms.OpenStackCredentialsForm
    formset = forms.DefaultRequiredInlineFormSet
    extra = 1


class UserProfileAdmin(admin.ModelAdmin):
    inlines = [AWSCredsInline, OSCredsInline]


### Public Services ###
class SponsorsAdmin(admin.ModelAdmin):
    models = models.Sponsor


class LocationAdmin(admin.ModelAdmin):
    models = models.Location

admin.site.register(models.Application, AppAdmin)
admin.site.register(models.AWS, CloudAdmin)
admin.site.register(models.EC2, EC2Admin)
admin.site.register(models.S3, S3Admin)
admin.site.register(models.OpenStack, CloudAdmin)
admin.site.register(models.UserProfile, UserProfileAdmin)

### Public Services Admin Registration ###
admin.site.register(models.Sponsor, SponsorsAdmin)
admin.site.register(models.Location, LocationAdmin)
