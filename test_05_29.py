# --------------------------------------------------
# DEFINICE TABULKY
# --------------------------------------------------

people = Table(
    name="people",
    columns=[
        Column("id", ColumnType(DataType.INT, not_null=True, unique=True)),
        Column("name", ColumnType(DataType.TEXT)),
        Column("salary", ColumnType(DataType.DECIMAL)),
        Column("born",ColumnType(DataType.DATE)),],
    primary_key=["id"],
)

# --------------------------------------------------
# DATA
# --------------------------------------------------

people.insert(
    ["id", "name", "salary", "born"],
    (1, "Alice", Decimal("25000.50"), date(2000, 5, 1))
)

people.insert(
    ["id", "name", "salary", "born"],
    (2, "Bob", Decimal("18000.00"), date(1999, 8, 15))
)

people.insert(
    ["id", "name", "salary", "born"],
    (3, None, None, None)
)

people2 = Table(name="people2", columns=people.columns, 
                primary_key=people.primary_key)

people2.insert(
    ["id", "name", "salary", "born"],
    (2, "Bob", Decimal("18000.00"), date(1999, 8, 15))
)

people2.insert(
    ["id", "name", "salary", "born"],
    (4, "Eve", Decimal("50000.00"), date(1995, 1, 1))
)

