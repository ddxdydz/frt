def get_max_id(data_list: list[dict]):
    max_id = 0
    for item in data_list:
        if item['id'] > max_id:
            max_id = item['id']
    return max_id
