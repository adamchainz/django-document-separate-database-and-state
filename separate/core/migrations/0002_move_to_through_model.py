from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0001_initial"),
    ]

    operations = [
        migrations.SeparateDatabaseAndState(
            database_operations=[
                migrations.RunSQL(
                    sql="ALTER TABLE core_book_authors RENAME TO core_authorbook",
                    reverse_sql="ALTER TABLE core_authorbook RENAME TO core_book_authors",
                ),
            ],
            state_operations=[
                migrations.CreateModel(
                    name="AuthorBook",
                    fields=[
                        (
                            "id",
                            models.AutoField(
                                auto_created=True,
                                primary_key=True,
                                serialize=False,
                                verbose_name="ID",
                            ),
                        ),
                        (
                            "author",
                            models.ForeignKey(
                                on_delete=django.db.models.deletion.DO_NOTHING,
                                to="core.Author",
                            ),
                        ),
                        (
                            "book",
                            models.ForeignKey(
                                on_delete=django.db.models.deletion.DO_NOTHING,
                                to="core.Book",
                            ),
                        ),
                    ],
                ),
                migrations.AlterField(
                    model_name="book",
                    name="authors",
                    field=models.ManyToManyField(
                        through="core.AuthorBook", to="core.Author"
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name='authorbook',
            name='is_primary',
            field=models.BooleanField(default=False),
        ),
    ]
