from django.contrib import admin

from api.models import Category, Choice, HighScore, Player, Question, QuestionReport

# Register your models here.
admin.site.register(Category)
admin.site.register(Question)
admin.site.register(Choice)
admin.site.register(Player)
admin.site.register(QuestionReport)
admin.site.register(HighScore)