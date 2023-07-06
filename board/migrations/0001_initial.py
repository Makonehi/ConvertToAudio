from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ads',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Заголовок')),
                ('anons', models.CharField(max_length=250, verbose_name='Описание')),
                ('full_text', models.TextField(verbose_name='Текст')),
                ('date', models.DateTimeField(verbose_name='Дата публикации')),
            ],
        ),
    ]
