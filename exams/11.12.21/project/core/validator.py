class Validator:
    @staticmethod
    def raise_if_len_is_less_than(obj, min_len, message):
        if len(obj) < min_len:
            raise ValueError(message)

    @staticmethod
    def raise_if_num_is_not_in_range(value, min_speed_limit, max_speed_limit, message):
        if value < min_speed_limit or value > max_speed_limit:
            raise ValueError(message)

    @staticmethod
    def raise_if_name_is_empty_str_or_white_space(value, message):
        if value.strip() == "":
            raise ValueError(message)
