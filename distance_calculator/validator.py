def validate(cities: dict) -> dict:

    validation_res = {
        'flag': True,
        'message': '400. Invalid input data',
    }

    if 'from_city' not in cities or 'to_city' not in cities:
        validation_res['flag'] = False
        return validation_res
    elif not (0 <= cities['from_city'] < 50) or not (0 <= cities['to_city'] < 50):
        validation_res['flag'] = False
        return validation_res

    return validation_res
