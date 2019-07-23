# Generated by Django 2.2.2 on 2019-07-23 13:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('source_optics', '0005_auto_20190722_2007'),
    ]

    operations = [
        migrations.AddField(
            model_name='organization',
            name='webhook_enabled',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='organization',
            name='webhook_token',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='repository',
            name='webhook_token',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='repository',
            name='name',
            field=models.TextField(db_index=True, max_length=32),
        ),
        migrations.AlterField(
            model_name='repository',
            name='url',
            field=models.TextField(help_text='use a git ssh url for private repos, else http/s are ok', max_length=255, unique=True),
        ),
        migrations.AlterUniqueTogether(
            name='repository',
            unique_together={('name', 'organization')},
        ),
    ]