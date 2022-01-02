import pathlib


def test_01():
    # pathlibのインスタンスをPathに渡して問題ないのかtest
    p = pathlib.Path("test")
    p2 = pathlib.Path(p)
    assert p == p2