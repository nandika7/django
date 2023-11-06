# Generated by Django 4.2.1 on 2023-07-15 16:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='HealthDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('age', models.IntegerField()),
                ('pregnancies', models.IntegerField()),
                ('glucose', models.IntegerField()),
                ('blood_sugar', models.IntegerField()),
                ('skin_thickness', models.IntegerField()),
                ('insulin', models.IntegerField()),
                ('bmi', models.IntegerField()),
                ('diabetes_pedigree_function', models.IntegerField()),
                ('is_diabetic', models.IntegerField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.user')),
            ],
        ),
    ]