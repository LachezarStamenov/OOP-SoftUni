class Validator:
    @staticmethod
    def raise_if_value_is_empty_string_or_white_space(string, message):
        if string.strip() == '':
            raise ValueError(message)

    @staticmethod
    def raise_if_value_is_less_than_or_equal_to_zero(value, message):
        if value <= 0:
            raise ValueError(message)

    @staticmethod
    def raise_if_inside_table_number_is_out_of_range(table_num, message):
        if not 1 <= table_num <= 50:
            raise ValueError(message)

    @staticmethod
    def rase_if_outside_table_num_is_out_of_range(table_num, message):
        if not 51 <= table_num <= 100:
            raise ValueError(message)

    @staticmethod
    def raise_if_food_exist_in_menu(name, food_menu, message):
        for food in food_menu:
            if food.name == name:
                raise Exception(message)

    @staticmethod
    def raise_if_drink_exist_in_menu(name, drink_menu, message):
        for drink in drink_menu:
            if drink.name == name:
                raise Exception(message)

    @staticmethod
    def raise_if_table_exist(table_number, table_repository, message):
        for table in table_repository:
            if table.table_number == table_number:
                raise Exception(message)

