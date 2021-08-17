# Generated by Django 3.2.6 on 2021-08-13 14:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_alter_performancepredict_pstatus'),
    ]

    operations = [
        migrations.AlterField(
            model_name='performancepredict',
            name='failures',
            field=models.CharField(choices=[('0', 'No Fail'), ('1', 'Failed once'), ('2', 'Failed Twice'), ('3', 'Failed Trice')], max_length=4, null=True),
        ),
        migrations.AlterField(
            model_name='performancepredict',
            name='reason',
            field=models.CharField(choices=[('course', 'Course preference'), ('other', 'Other'), ('home', 'Close to home'), ('reputation', 'School reputation')], max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='performancepredict',
            name='studytime',
            field=models.CharField(choices=[('1', '2 hours'), ('2', 'From 2 to 5 hours'), ('3', 'From 5 to 10 hours'), ('4', 'More than 10 hours')], max_length=20, null=True),
        ),
    ]
