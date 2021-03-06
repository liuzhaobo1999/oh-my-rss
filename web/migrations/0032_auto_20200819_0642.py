# Generated by Django 3.1 on 2020-08-18 22:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0031_auto_20200818_2234'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='status',
            field=models.IntegerField(choices=[(0, '待处理'), (1, '处理中'), (2, '处理成功'), (3, '超时'), (4, '解析异常'), (5, '交还次数超限'), (6, '内容违规或删除')], db_index=True, default=0, verbose_name='状态'),
        ),
    ]
