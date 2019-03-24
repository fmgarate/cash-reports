from django.contrib import admin

from .models import Entry, Tag, EntrySummary


class EntryAdmin(admin.ModelAdmin):
    list_display = ('value', 'entry_type', 'description', 'date')


admin.site.register(Entry, EntryAdmin)
admin.site.register(Tag)
admin.site.register(EntrySummary)
