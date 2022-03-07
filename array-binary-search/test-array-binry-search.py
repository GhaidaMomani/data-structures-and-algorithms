from array_binary_search import BinarySeach

# "Happy Path" cases

def test_simple():
  expected = 3
  actual = BinarySeach([1,2,3,4,5,6],4)
  assert actual == expected
