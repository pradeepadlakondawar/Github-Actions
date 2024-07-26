# app.py
# test_commit_1
# test_commit_2
def add(a, b):
    return a + b

def test_add():
    assert add(1, 2) == 3
    assert add(1, -1) == 0
