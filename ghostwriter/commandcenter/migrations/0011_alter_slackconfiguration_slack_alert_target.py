# Generated by Django 3.2.11 on 2022-08-30 16:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('commandcenter', '0010_auto_20220205_0026'),
    ]

    operations = [
        migrations.AlterField(
            model_name='slackconfiguration',
            name='slack_alert_target',
            field=models.CharField(blank=True, default='<!here>', help_text='Alert target for the notifications (e.g., <!here>) – blank for no target', max_length=255),
        ),
    ]