from hello import add

def test_add():
    assert add(2, 3) == 5
    assert add(5, 7) == 12
    assert add(10, 20) == 30
    assert add(100, 200) == 300