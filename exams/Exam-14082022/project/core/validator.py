class Validator:

    @staticmethod
    def raise_if_string_is_empty_or_whitespace(string, message):
        if string.strip() == "":
            raise ValueError(message)

    @staticmethod
    def raise_if_jockey_is_under_18(years, message):
        if years < 18:
            raise ValueError(message)

    @staticmethod
    def raise_if_string_is_less_than_min_numbers_of_chars(string, min_chars, message):
        if len(string.strip()) < min_chars:
            raise ValueError(message)

    @staticmethod
    def raise_if_race_type_is_not_valid(race_type, message):
        valid_race_types = ["Winter", "Spring", "Autumn", "Summer"]
        if race_type not in valid_race_types:
            raise ValueError(message)
