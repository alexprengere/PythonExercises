import pytest
import sudoku as s

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
        sudoku = s.read(f)
    assert not s.is_solved(sudoku)

    with open("examples/solved.txt") as f:
        sudoku = s.read(f)
    assert s.is_solved(sudoku)


@pytest.mark.parametrize("string", SOLVABLE)
def test_solve_1(string):
    with open(string) as f:
        sudoku = s.read(f)
    s.solve(sudoku)
    assert s.is_solved(sudoku)


@pytest.mark.parametrize("string", NOT_SOLVABLE)
def test_solve_2(string):
    with open(string) as f:
        sudoku = s.read(f)
    with pytest.raises(ValueError):
        s.solve(sudoku)
