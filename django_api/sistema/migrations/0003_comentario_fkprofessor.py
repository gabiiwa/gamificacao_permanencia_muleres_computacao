# Generated by Django 4.0.5 on 2022-07-25 22:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sistema', '0002_alter_tarefa_unique_together'),
    ]

    operations = [
        migrations.AddField(
            model_name='comentario',
            name='fkprofessor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='sistema.professor'),
        ),
    ]
