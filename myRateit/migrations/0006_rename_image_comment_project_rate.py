# Generated by Django 4.0.3 on 2022-04-12 16:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myRateit', '0005_alter_project_description'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='image',
            new_name='project',
        ),
        migrations.CreateModel(
            name='Rate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('design', models.IntegerField(default=0)),
                ('usability', models.IntegerField(default=0)),
                ('content', models.IntegerField(default=0)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rating', to='myRateit.project')),
            ],
        ),
    ]
