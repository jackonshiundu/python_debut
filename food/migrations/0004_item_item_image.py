# Generated by Django 4.2 on 2024-08-14 19:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0003_rename_items_price_item_item_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='item_image',
            field=models.CharField(default='https://i0.wp.com/www.drdavidludwig.com/wp-content/uploads/2017/01/1-RIS_6IbCLYv1X3bzYW1lmA.jpeg?resize=705%2C486&ssl=1', max_length=500),
        ),
    ]
