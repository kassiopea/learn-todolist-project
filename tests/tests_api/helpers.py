def get_list_keys_from_response(list_dict: list) -> list:
    result = []
    for item in list_dict:
        for key in item.keys():
            result.append(key)
    return result

