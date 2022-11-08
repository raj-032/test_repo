def generate_sql_in_cond_string(column_name, values, col_type='varchar'):
    """
    :param column_name:
    :param values:
    :param col_type:
    :return: where clause
    """
    try:
        if col_type == 'int':
            values_array = ','.join(str(value) for value in values)
        else:
            if len(values) != 1:
                values_array = str(tuple(values))
                values_array = str(values_array).replace("(", "").replace(")", "")
            else:
                values_array = str(values).replace("[", "").replace("]", "")
        values_array = f"""{values_array}"""
        in_clause = f"{column_name} in ({values_array})"

        return in_clause
    except Exception as e:
        raise Exception(e)


def upper_keys(x):
    try:
        if isinstance(x, list):
            return [upper_keys(v) for v in x]
        elif isinstance(x, dict):
            return dict((k.upper(), upper_keys(v)) for k, v in x.items())
        else:
            return x
    except Exception as e:
        raise Exception(e)