# Generated by Django 4.2.4 on 2024-03-25 18:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0029_alter_sandwich_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sandwich',
            name='type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sandwichs', to='App.badge'),
        ),
    ]
