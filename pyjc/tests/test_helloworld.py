import pyjc


def test_helloworld():
    assert isinstance(pyjc.helloworld(), str)
    assert pyjc.helloworld() == "Hello World!"
