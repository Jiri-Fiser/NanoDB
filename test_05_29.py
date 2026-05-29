# --------------------------------------------------
# DEFINICE TABULKY
# --------------------------------------------------

people = Table(
    name="people",
    columns=[
        Column("id", ColumnType(DataType.INT, not_null=True, unique=True)),
        Column("name", ColumnType(DataType.TEXT)),
        Column("city", ColumnType(DataType.TEXT)),
        Column("age", ColumnType(DataType.INT)),
       ], primary_key=["id"],
)

# --------------------------------------------------
# DATA
# --------------------------------------------------

people.insert(["id", "name", "city", "age"], (1, "Alice", "Praha", 20))
people.insert(["id", "name", "city", "age"], (2, "Bob", None, 22))
people.insert(["id", "name", "city", "age"], (3, "Anna", "Brno", None))
people.insert(["id", "name", "city", "age"], (4, None, None, None))

print(people.to_text())


more_people = Table(
    name="more_people",
    columns=[
        Column("id", ColumnType(DataType.INT, not_null=True, unique=True)),
        Column("name", ColumnType(DataType.TEXT)),
        Column("city", ColumnType(DataType.TEXT)),
        Column("age", ColumnType(DataType.INT)),
        Column("prefix_ok", ColumnType(DataType.INT, not_null=True)),
    ],
    primary_key=["id"],
)

bad_people = Table(
    name="bad_people",
    columns=[
        Column("id", ColumnType(DataType.INT, not_null=True, unique=True)),
        Column("name", ColumnType(DataType.TEXT)),
        Column("city", ColumnType(DataType.TEXT)),
        Column("age", ColumnType(DataType.INT)),
        Column("prefix_ok", ColumnType(DataType.INT, not_null=True)),
    ],
    primary_key=["id"],
)

