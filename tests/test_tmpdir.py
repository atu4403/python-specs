# https://py.readthedocs.io/en/latest/path.html
# https://ja.stackoverflow.com/questions/57956/macos-%E3%81%AE-tmpdir-%E3%81%AB%E4%BD%9C%E6%88%90%E3%81%97%E3%81%9F%E3%83%95%E3%82%A1%E3%82%A4%E3%83%AB-%E3%83%87%E3%82%A3%E3%83%AC%E3%82%AF%E3%83%88%E3%83%AA%E3%81%AF%E3%81%84%E3%81%A4%E5%89%8A%E9%99%A4%E3%81%95%E3%82%8C%E3%82%8B
import os
import pytest


@pytest.fixture
def d(tmpdir) -> str:
    p = tmpdir.chdir()
    yield
    p.chdir()


def test_tmpdir(d):
    a = os.getcwd()
    assert (
        a
        != "/private/var/folders/gc/1js4q5b53fjblxs9z0fsj17h0000gn/T/pytest-of-atu/pytest-7/test_tmpdir0"
    )
