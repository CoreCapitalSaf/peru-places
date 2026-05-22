from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0009_auto_20210216_2312'),
    ]

    operations = [
        migrations.AddField(
            model_name='county',
            name='is_state',
            field=models.BooleanField(default=False),
        ),
    ]
