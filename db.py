import json


def write_to_file(user_data):
    json_string = json.dumps(user_data, ensure_ascii=False)
    print(json_string)
    with open('db.json', 'w', encoding='utf-8') as file:
        file.write(json_string)
    print('done!')


def read_from_db():
    try:
        with open('db.json', encoding='utf-8') as file:
            json_string = file.read()
        db_data = json.loads(json_string)
    except FileNotFoundError:
        db_data = {}
    return db_data


a = {'1': 1}
write_to_file(a)

s = read_from_db()
print(s)
