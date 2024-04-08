# Generated by Django 5.0.3 on 2024-04-01 02:59

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0015_alter_user_managers"),
        ("auth", "0012_alter_user_first_name_max_length"),
        ("course", "0007_delete_courseoffer"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="student",
            name="department",
        ),
        migrations.RemoveField(
            model_name="student",
            name="level",
        ),
        migrations.AlterField(
            model_name="parent",
            name="user",
            field=models.OneToOneField(
                on_delete=django.db.models.deletion.CASCADE, to="accounts.user"
            ),
        ),
        migrations.AlterField(
            model_name="student",
            name="student",
            field=models.OneToOneField(
                on_delete=django.db.models.deletion.CASCADE, to="accounts.user"
            ),
        ),
        migrations.AlterField(
            model_name="user",
            name="groups",
            field=models.ManyToManyField(
                blank=True,
                related_name="custom_user_set",
                related_query_name="custom_user",
                to="auth.group",
                verbose_name="groups",
            ),
        ),
        migrations.AlterField(
            model_name="user",
            name="user_permissions",
            field=models.ManyToManyField(
                blank=True,
                help_text="Specific permissions for this user.",
                related_name="custom_user_set",
                related_query_name="custom_user",
                to="auth.permission",
                verbose_name="user permissions",
            ),
        ),
        migrations.DeleteModel(
            name="DepartmentHead",
        ),
    ]
