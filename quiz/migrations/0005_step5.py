from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0004_step4'),
    ]

    operations = [
        migrations.AlterField(
            model_name='result',
            name='date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
