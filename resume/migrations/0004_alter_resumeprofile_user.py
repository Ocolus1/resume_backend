# Generated by Django 4.1.3 on 2022-12-15 18:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('resume', '0003_alter_resumeprofile_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resumeprofile',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='to_user', to=settings.AUTH_USER_MODEL, verbose_name='user'),
        ),
    ]
