import pytest
from sudoku import Sudoku

SOLVABLE = [
    "examples/solved.txt",
    "examples/simple.txt",
    "examples/expert.txt",
]
NOT_SOLVABLE = [
    "examples/error.txt",
]


def test_is_solved():
    with open("examples/simple.txt") as f:
        s = Sudoku(f)
    assert not s.is_solved()

    with open("examples/solved.txt") as f:
        s = Sudoku(f)
    assert s.is_solved()


@pytest.mark.parametrize("string", SOLVABLE)
def test_solve_1(string):
    with open(string) as f:
        s = Sudoku(f)
    s.solve()
    assert s.is_solved()


@pytest.mark.parametrize("string", NOT_SOLVABLE)
def test_solve_2(string):
    with open(string) as f:
        s = Sudoku(f)
    with pytest.raises(ValueError):
        s.solve()
