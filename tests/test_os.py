"""os.chdirのsample
pytestのtmpdirとは違ってos.chdirは何も返さない。
最初のpathをgetcwdで取得しておくと元のディレクトリに戻ることができる。
"""
import os


def test_chdir():
    cwd = os.getcwd()
    p = os.chdir("tests")
    assert p is None
    assert os.getcwd().endswith("python-specs/tests")
    os.chdir(cwd)
    assert os.getcwd().endswith("python-specs")