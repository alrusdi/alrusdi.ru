# Generated by Django 3.2.5 on 2021-07-29 11:22
import tinymce
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0002_page_is_private'),
    ]

    operations = [
        migrations.AlterField(
            model_name='page',
            name='content',
            field=tinymce.models.HTMLField(blank=True, null=True),
        ),
    ]



