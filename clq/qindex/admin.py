from django.contrib import admin
from.models import topic,Contact,btopic,bspl,spl



class TopicAdmin(admin.ModelAdmin):
    list_display=('pk','suraname','surano','verseno','verse','tname','t_id')
admin.site.register(topic,TopicAdmin)

class BtopicAdmin(admin.ModelAdmin):
    list_display=('pk','bsuraname','bsurano','bverseno','bverse','btname','bt_id')
admin.site.register(btopic,BtopicAdmin)

#=========================
class BsplAdmin(admin.ModelAdmin):
    list_display=('pk','bav','bu','bv','bq')
admin.site.register(bspl,BsplAdmin)

class SplAdmin(admin.ModelAdmin):
    list_display=('pk','av','eu','v','q')
admin.site.register(spl,SplAdmin)

class ServiceAdmin(admin.ModelAdmin):
    list_display=('pk','name','email','desc',)
admin.site.register(Contact,ServiceAdmin)



# Register your models here.

