from project.table.inside_table import InsideTable
from project.table.outside_table import OutsideTable


class TableFactory:
    table_type = {
        'InsideTable': InsideTable,
        'OutsideTable': OutsideTable
    }

    @staticmethod
    def create_table(table_type, table_number, capacity):
        return TableFactory.table_type[table_type](table_number, capacity)