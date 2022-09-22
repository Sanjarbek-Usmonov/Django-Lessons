# Generated by Django 4.1.1 on 2022-09-20 12:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app1", "0003_alter_choice_question"),
    ]

    operations = [
        migrations.CreateModel(
            name="User",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("user", models.CharField(max_length=150)),
            ],
        ),
        migrations.AddField(
            model_name="question",
            name="user_id",
            field=models.ManyToManyField(to="app1.user"),
        ),
    ]