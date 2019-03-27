# Generated by Django 2.0.10 on 2019-03-23 16:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('srcOptics', '0005_auto_20190321_2013'),
    ]

    operations = [
        migrations.AlterField(
            model_name='organization',
            name='name',
            field=models.TextField(max_length=32, unique=True),
        ),
        migrations.AddIndex(
            model_name='commit',
            index=models.Index(fields=['repo', 'commit_date'], name='srcOptics_c_repo_id_09963b_idx'),
        ),
        migrations.AddIndex(
            model_name='commit',
            index=models.Index(fields=['author', 'commit_date'], name='srcOptics_c_author__8a3d7d_idx'),
        ),
        migrations.AddIndex(
            model_name='statistic',
            index=models.Index(fields=['interval', 'author', 'repo', 'file', 'start_date'], name='srcOptics_s_interva_cb775a_idx'),
        ),
    ]