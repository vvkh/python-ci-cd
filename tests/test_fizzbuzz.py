import pytest
import fizzbuzz


@pytest.mark.parametrize('max_number,want_result', [
    (0, []),
    (1, []),
    (2, [1]),
    (4, [1, 2, 'fizz']),
    (6, [1, 2, 'fizz', 4, 'buzz']),
    (16, [1, 2, 'fizz', 4, 'buzz', 'fizz', 7, 8, 'fizz', 'buzz', 11, 'fizz', 13, 14, 'fizzbuzz']),
])
def test_fizzbuzz(max_number, want_result):
    assert fizzbuzz.generate(max_number) == want_result
