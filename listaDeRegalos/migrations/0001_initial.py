# Generated by Django 4.0.4 on 2022-04-30 04:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ListaDeRegalos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('BO', 'Boda'), ('XV', 'XV Años'), ('BA', 'Bautizos'), ('IN', 'Infantiles'), ('PH', 'Para él'), ('PM', 'Para ella')], max_length=2)),
                ('description', models.TextField(max_length=130)),
                ('store', models.CharField(max_length=50)),
                ('price', models.PositiveIntegerField(default=0)),
                ('image', models.ImageField(blank=True, null=True, upload_to='products/images')),
            ],
        ),
    ]
