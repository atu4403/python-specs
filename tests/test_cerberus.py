from cerberus import Validator


def test_cerberus():
    li = [
        {"name": "alice", "age": 7},
        {"name": "bob", "age": "28"},
        {"name": "charlie"},
    ]
    schema = {
        "name": {"type": "string"},
        "age": {"type": "integer", "min": 10, "required": True},
    }
    v = Validator(schema)
    for d in li:
        v.validate(d)
        print("errors", d, v.errors)


# errors {'name': 'alice', 'age': 7} {'age': ['min value is 10']}
# errors {'name': 'bob', 'age': '28'} {'age': ['must be of integer type']}
# errors {'name': 'charlie'} {'age': ['required field']}