class Validator:
    @staticmethod
    def raise_if_string_is_empty_or_whitespace(string: str, message: str):
        if string.strip() == '':
            raise ValueError(message)

    @staticmethod
    def raise_if_number_is_less_than_restriction(number: float, restriction, message):
        if number < restriction:
            raise ValueError(message)

    @staticmethod
    def raise_if_year_under_1888(year, message):
        if year < 1888:
            raise ValueError(message)

    @staticmethod
    def raise_if_owner_is_not_object(owner, message):
        if not type(owner).__name__ == 'User':
            raise ValueError(message)
