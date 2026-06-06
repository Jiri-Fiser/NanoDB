from datetime import datetime

from nanodb import Column, ColumnType, DataType, Table


def test_table_schema_is_not_mutated_by_source_columns() -> None:
    columns = [
        Column("id", ColumnType(DataType.INT, not_null=True, unique=True)),
    ]
    table = Table("person", columns, ["id"])

    columns.append(Column("name", ColumnType(DataType.TEXT)))
    columns[0].name = "changed"
    table.columns[0].name = "changed_again"

    table.insert(["id"], (1,))

    assert [column.name for column in table.columns] == ["id"]
    assert list(table) == [(1,)]


def test_int_columns_reject_bool_values() -> None:
    table = Table(
        "person",
        [Column("id", ColumnType(DataType.INT, not_null=True, unique=True))],
        ["id"],
    )

    try:
        table.insert(["id"], (True,))
    except TypeError as exc:
        assert "expects int" in str(exc)
    else:
        raise AssertionError("INT columns must reject bool values")


def test_date_columns_reject_datetime_values() -> None:
    table = Table(
        "event",
        [
            Column("id", ColumnType(DataType.INT, not_null=True, unique=True)),
            Column("created", ColumnType(DataType.DATE, not_null=True)),
        ],
        ["id"],
    )

    try:
        table.insert(["id", "created"], (1, datetime(2026, 1, 1, 12, 30)))
    except TypeError as exc:
        assert "expects date" in str(exc)
    else:
        raise AssertionError("DATE columns must reject datetime values")


def test_select_to_inserts_projected_rows_into_target() -> None:
    source = Table(
        "source",
        [
            Column("id", ColumnType(DataType.INT, not_null=True, unique=True)),
            Column("name", ColumnType(DataType.TEXT, not_null=True)),
        ],
        ["id"],
    )
    target = Table(
        "target",
        [
            Column("id", ColumnType(DataType.INT, not_null=True, unique=True)),
            Column("label", ColumnType(DataType.TEXT, not_null=True)),
        ],
        ["id"],
    )
    source.insert(["id", "name"], (1, "Alice"))

    returned = source.select_to(
        lambda row: {"id": row["id"], "label": row["name"]},
        target,
    )

    assert returned is target
    assert list(target) == [(1, "Alice")]


def test_select_to_uses_target_constraints() -> None:
    source = Table(
        "source",
        [
            Column("id", ColumnType(DataType.INT, not_null=True, unique=True)),
            Column("name", ColumnType(DataType.TEXT)),
        ],
        ["id"],
    )
    target = Table(
        "target",
        [
            Column("id", ColumnType(DataType.INT, not_null=True, unique=True)),
            Column("label", ColumnType(DataType.TEXT, not_null=True)),
        ],
        ["id"],
    )
    source.insert(["id", "name"], (1, None))

    try:
        source.select_to(
            lambda row: {"id": row["id"], "label": row["name"]},
            target,
        )
    except ValueError as exc:
        assert "cannot be NULL" in str(exc)
    else:
        raise AssertionError("select_to must validate rows through target.insert")
