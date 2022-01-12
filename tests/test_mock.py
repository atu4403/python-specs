from pytest_mock import mocker


def fn(n):
    print(n ** 2)


def test_mock(mocker):
    mocker.patch("builtins.print")
    print.assert_not_called()  # この時点でprintは呼ばれていない
    fn(3)
    print.assert_any_call(9)  # print(9)で呼ばれた
    print.assert_called()  # mockが呼ばれた
    print.assert_called_once()  # mockが１回呼ばれた
    print.assert_called_once_with(9)  # mockが１回print(9)で呼ばれた
    print.assert_has_calls([mocker.call(9)])
    print.assert_called_with(9)
    assert print.called == True
    assert print.call_args == mocker.call(9)
    assert print.call_args_list == [mocker.call(9)]
    assert print.call_count == 1
    assert print.called == True

    fn(8)
    print.assert_any_call(9)
    print.assert_any_call(64)
    print.assert_has_calls([mocker.call(9)])
    print.assert_has_calls([mocker.call(9), mocker.call(64)])
    assert print.call_args == mocker.call(64)
    assert print.call_args_list == [mocker.call(9), mocker.call(64)]
    assert print.call_count == 2


class AAA:
    def __init__(self, name) -> None:
        self.name = name

    def bbb(self, age):
        return f"{self.name} is age {age}"


def test_class_instance(mocker):
    mock = mocker.patch.object(AAA, "__init__", return_value=None)
    ins = AAA("alice")
    mock.assert_called_with("alice")


def test_class_method(mocker):
    mock = mocker.patch.object(AAA, "bbb")
    ins = AAA("alice")
    ins.bbb(3)
    mock.assert_called_with(3)
    print(mock, AAA, ins.name, mock.call_args_list)
