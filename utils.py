def check_type(value, types):
    if type(value) not in types:
        raise TypeError(
            f'Unexpected argument type - '
            f'type: `{type(value)}` value: `{value}`'
        )
