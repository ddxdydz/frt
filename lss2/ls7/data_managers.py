def get_max_id(data_list: list[dict]):
    max_id = 0
    for item in data_list:
        if item['id'] > max_id:
            max_id = item['id']
    return max_id


def add_to_data_list(data_list: list[dict], params: dict):
    elem = params.copy()
    elem['id'] = get_max_id(data_list)
    data_list.append(params)


def get_from_data_list(data_list: list[dict], id: int) -> dict:
    results = []
    for elem in data_list:
        if elem["id"] == id:
            results.append["id"]
            return results
        


def remove_from_data_list(data_list: list[dict], list, id: int):
    pass


def edit_elem_from_data_list(data_list: list[dict], id: int, params: dict):
    pass
