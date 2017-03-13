# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cal', '0033_auto_20160430_0642'),
    ]

    operations = [
        migrations.CreateModel(
            name='GRecurrence',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('start', models.DateTimeField()),
                ('end', models.DateTimeField()),
                ('recurring_event_id', models.CharField(help_text=b'For an instance of a recurring event, the id of the recurring event to which this instance belongs', max_length=1024, blank=True)),
                ('calendar', models.ForeignKey(related_name='recurrences', to='cal.GCalendar')),
            ],
        ),
    ]
