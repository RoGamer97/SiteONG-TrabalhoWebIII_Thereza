# Generated by Django 5.1.3 on 2025-05-08 22:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("myapp", "0009_relatorioanual"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="relatorioanual",
            name="arquivo_pdf",
        ),
        migrations.AddField(
            model_name="relatorioanual",
            name="link_relatorio",
            field=models.URLField(blank=True, max_length=500, null=True),
        ),
    ]
