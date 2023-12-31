# Generated by Django 4.2.2 on 2023-07-06 13:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('dashboard', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stock',
            name='edit_date',
            field=models.DateField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='stock',
            name='edited_by',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='stock',
            name='item_code',
            field=models.ForeignKey(default=101, on_delete=django.db.models.deletion.CASCADE, to='dashboard.items'),
        ),
    ]
