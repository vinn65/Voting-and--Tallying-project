from django.contrib import admin
from .models import Questions , choice

admin.site.site_header = 'Pollster Admin'
admin.site.site_title = "Vincent`s Tallying centre"
admin.site.index_title = 'Welcome to the admin site'


class ChoiceInline(admin.TabularInline):
    model  = choice
    extra = 3

class QuestionsAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,{'fields':['question_text']}),
         ('Date information', 
         {'fields':['pub_date'],
         'classes':['collapse'] } ),
    ]

    inlines = [ChoiceInline]

admin.site.register(Questions, QuestionsAdmin)


# admin.site.register(models.questions)
# admin.site.register(models.choice)