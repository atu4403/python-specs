import pathlib
import json
import pytest

# `json.dump`はファイルオブジェクト
# `json.dumps`は文字列
def json_write(d: dict, file_path: str, overwrite: bool = False):
    file_path = pathlib.Path(file_path)
    if not overwrite and file_path.exists():
        return 0
    file_path.write_text(json.dumps(d))
    return 1


# `json.load`はファイルオブジェクト
# `json.loads`は文字列
def json_read(file_path: str):
    file_path = pathlib.Path(file_path)
    return json.loads(file_path.read_text())


@pytest.fixture()
def path():
    _p = "sample.json"
    yield _p
    pathlib.Path(_p).unlink()


@pytest.fixture()
def ppath():
    _p = pathlib.Path("sample.json")
    yield _p
    pathlib.Path(_p).unlink()


def test_json(path):
    assert json_write({"a": 1}, path) == 1
    assert json_write({"a": 1}, path, overwrite=True) == 1
    assert json_read(path) == {"a": 1}
    assert json_write({"a": 1}, path) == 0


def test_json_pathlib(ppath):
    assert json_write({"a": 1}, ppath) == 1
    assert json_write({"a": 1}, ppath, overwrite=True) == 1
    assert json_read(ppath) == {"a": 1}
    assert json_write({"a": 1}, ppath) == 0
