# Generated by Django 5.2.1 on 2025-06-20 04:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0006_attributedependency'),
    ]

    operations = [
        migrations.AddField(
            model_name='attributedependency',
            name='height',
            field=models.PositiveIntegerField(default=87, help_text='Player height in inches (e.g. 87 for 7\'3")'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='attributedependency',
            name='obs_dependent',
            field=models.IntegerField(help_text='Observed dependent value at this height'),
        ),
        migrations.AlterField(
            model_name='attributedependency',
            name='obs_source_value',
            field=models.IntegerField(help_text='Observed source value at this height'),
        ),
    ]
