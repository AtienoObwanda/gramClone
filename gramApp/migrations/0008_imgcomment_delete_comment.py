# Generated by Django 4.0.5 on 2022-06-05 17:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('gramApp', '0007_remove_comment_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='imgComment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField()),
                ('createDate', models.DateTimeField(default=django.utils.timezone.now)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('image', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gramApp.image')),
            ],
        ),
        migrations.DeleteModel(
            name='Comment',
        ),
    ]