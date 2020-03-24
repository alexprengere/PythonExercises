from __future__ import print_function
import itertools


def read(rows):
    """Reads the list of rows and returns the sudoku dict"""
    grid = []
    for row in rows:
        row = row.rstrip()
        if not row:
            continue
        grid.append([None if v == "." else int(v) for v in row if v != " "])

    # A single dict mapping an (i, j) index to a known value, or None
    # Indices go from 1 to 9
    sudoku = {}
    for i, line in enumerate(grid, start=1):
        for j, n in enumerate(line, start=1):
            sudoku[i, j] = n
    return sudoku


def show(sudoku):
    """Pretty print the content, kind of the opposite of read()"""
    for i, line in enumerate(get_lines(sudoku), start=1):
        if i in (4, 7):
            print()
        row = []
        for j, n in enumerate(line, start=1):
            if j in (4, 7):
                row.append(" ")
            row.append("." if n is None else str(n))
        print("".join(row))


def get_lines(sudoku):
    for i in range(1, 10):
        yield [sudoku[i, j] for j in range(1, 10)]


def get_columns(sudoku):
    for j in range(1, 10):
        yield [sudoku[i, j] for i in range(1, 10)]


def get_squares(sudoku):
    for li in (1, 4, 7):
        for lj in (1, 4, 7):
            yield [sudoku[i, j] for i in range(li, li + 3) for j in range(lj, lj + 3)]


def get_neighbor_indices(i, j):
    """Returns indices of cases on the same line/column/square as (i, j)"""
    # Same line indices
    for dj in range(1, 10):
        if dj != j:
            yield (i, dj)

    # Same column indices
    for di in range(1, 10):
        if di != i:
            yield (di, j)

    # Same square indices
    li = 1 + (i - 1) // 3 * 3
    lj = 1 + (j - 1) // 3 * 3
    for di in range(li, li + 3):
        for dj in range(lj, lj + 3):
            if (di, dj) != (i, j):
                yield (di, dj)


def is_solved(sudoku):
    return all(
        set(numbers) == set(range(1, 10))
        for numbers in itertools.chain(
            get_lines(sudoku), get_columns(sudoku), get_squares(sudoku)
        )
    )


def solve(sudoku):
    """Solves the Sudoku in place, or raises ValueError if not solvable."""

    while not is_solved(sudoku):
        # Used to check progress at the end of the loop
        prev_sudoku = sudoku.copy()

        # List of possibilities for an (i, j) index
        poss = {}
        for i_j, n in sudoku.items():
            if n is None:
                poss[i_j] = set(range(1, 10))
            else:
                poss[i_j] = {n}

        # First, we remove the possibilities in same line/column/square
        for i_j, n in sudoku.items():
            if n is None:
                continue
            for di_dj in get_neighbor_indices(*i_j):
                if n in poss[di_dj]:
                    poss[di_dj].remove(n)

        # When the possibilities are reduced to 1 single value, we write to sudoku
        for i_j in list(poss):
            if len(poss[i_j]) == 1:
                sudoku[i_j] = poss[i_j].pop()
                del poss[i_j]  # remove (i, j) from the possibilities

        # Do not go recursive if we made progress
        if prev_sudoku != sudoku:
            continue

        # Recursively split on the fewest possibilities
        i_j = min(poss, key=lambda k: len(poss[k]))
        for n in poss[i_j]:
            # Let's hypothesize that value at position i_j is n
            hyp_sudoku = sudoku.copy()
            hyp_sudoku[i_j] = n
            try:
                solve(hyp_sudoku)  # can go recursive
            except ValueError:
                # That possibility lead to a non solvable Sudoku.
                pass
            else:
                # That possibility lead to a resolution.
                # We store the result, the main loop will break
                # at the next iteration.
                sudoku.update(hyp_sudoku)
                break

        # No progress, no need no go further this is not solvable
        if prev_sudoku == sudoku:
            raise ValueError("Not solvable")


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("file")
    args = parser.parse_args()
    try:
        with open(args.file) as f:
            sudoku = read(f)
            solve(sudoku)
            show(sudoku)
    except Exception as e:
        print(e)
