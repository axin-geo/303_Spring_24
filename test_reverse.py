# caution...mutable objects ahead
import pytest

def reverse_list(list: list):
  list.reverse()
  return list

     
@pytest.mark.parametrize("in_list, out_list",
                         [
                              ([1,2,3],[3,2,1]), ([1,2,3],[2,2,3])
                         ])
def test_reverse_list(in_list, out_list):
     assert reverse_list(in_list) == out_list