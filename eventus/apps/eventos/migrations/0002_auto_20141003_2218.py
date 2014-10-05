# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('eventos', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='inscritos',
            name='asistente',
            field=models.ForeignKey(blank=True, to=settings.AUTH_USER_MODEL, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='inscritos',
            name='evento',
            field=models.ForeignKey(blank=True, to='eventos.Evento', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='evento',
            name='organizador',
            field=models.ForeignKey(blank=True, to=settings.AUTH_USER_MODEL, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='comentario',
            name='evento',
            field=models.ForeignKey(to='eventos.Evento'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='comentario',
            name='usuario',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
    ]
