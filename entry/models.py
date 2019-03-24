from django.db import models


class Entry(models.Model):

    ENTRY_IN = 'IN'
    ENTRY_OUT = 'OUT'

    ENTRY_TYPE_CHOICES = (
        (ENTRY_IN, 'In'),
        (ENTRY_OUT, 'Out'),
    )

    entry_type = models.CharField(max_length=3, choices=ENTRY_TYPE_CHOICES)
    value = models.DecimalField(max_digits=12, decimal_places=2)
    date = models.DateField()
    description = models.TextField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    tags = models.ManyToManyField('Tag')

    class Meta:
        verbose_name_plural = 'Entries'

    def __str__(self):
        return f'{self.entry_type}, {self.value}'


class Tag(models.Model):

    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name


class EntrySummary(models.Model):
    """
    Stores a CSV like file with a collection of entries
    """

    NEW = 'NEW'
    IN_PROGRESS = 'IN_PROGRESS'
    DONE = 'DONE'
    FAILED = 'FAILED'

    STATUS_CHOICES = (
        (NEW, 'New'),
        (IN_PROGRESS, 'In progress'),
        (DONE, 'Done'),
        (FAILED, 'Failed'),
    )

    name = models.CharField(max_length=128, null=True, blank=True)
    date_from = models.DateField(null=True, blank=True)
    date_to = models.DateField(null=True, blank=True)
    status = models.CharField(max_length=16, choices=STATUS_CHOICES, default=NEW)
    created = models.DateTimeField(auto_now_add=True)
    file = models.FileField()

    class Meta:
        verbose_name_plural = 'Entry Summaries'

    def __str__(self):
        return f'{self.name or "Unnamed"} {self.id}'
