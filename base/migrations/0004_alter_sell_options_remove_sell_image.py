# Generated by Django 4.1 on 2023-06-14 06:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_alter_sell_image'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='sell',
            options={'ordering': ['-updated', '-created']},
        ),
        migrations.RemoveField(
            model_name='sell',
            name='image',
        ),
    ]