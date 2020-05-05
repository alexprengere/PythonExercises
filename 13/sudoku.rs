use std::env;
use std::fs::File;
use std::io;
use std::io::prelude::*;
use std::iter::FromIterator;
use std::path::Path;
use rustc_hash::FxHashMap;
use rustc_hash::FxHashSet;

struct Sudoku {
    data: [u8; 81],
}

// The output is wrapped in a Result to allow matching on errors
// Returns an Iterator to the Reader of the lines of the file.
fn read_lines<P>(filename: P) -> io::Result<io::Lines<io::BufReader<File>>>
where
    P: AsRef<Path>,
{
    let file = File::open(filename)?;
    Ok(io::BufReader::new(file).lines())
}

impl Sudoku {
    fn new(filename: &str) -> Sudoku {
        let mut data = [0u8; 81];

        if let Ok(lines) = read_lines(filename) {
            let mut i = 0;
            for (ln, line_) in lines.enumerate() {
                if let Ok(line) = line_ {
                    if ln == 3 || ln == 7 {
                        continue;
                    }
                    let mut j = 0;
                    for (cn, c) in line.chars().enumerate() {
                        if cn == 3 || cn == 7 {
                            continue;
                        }
                        if c != '.' {
                            data[i * 9 + j] = c.to_digit(10).unwrap() as u8;
                        }
                        j += 1;
                    }
                    i += 1;
                }
            }
        }
        Sudoku { data }
    }

    fn copy(&self) -> Sudoku {
        Sudoku { data: self.data.clone() }
    }

    fn show(&self) {
        for k in 0..81 {
            let i = k / 9;
            let j = k % 9;
            let n = self.data[k];
            if n == 0 {
                print!(".");
            } else {
                print!("{}", n);
            }
            if j == 2 || j == 5 {
                print!(" ");
            } else if j == 8 {
                println!();
                if i == 2 || i == 5 {
                    println!();
                }
            }
        }
    }

    fn get_neighbor_indices(k: u8) -> FxHashSet<u8> {
        let i = k / 9;
        let j = k % 9;
        let mut indices = FxHashSet::default();

        for dj in 0..9 {
            if dj != j {
                indices.insert(i * 9 + dj);
            }
        }

        for di in 0..9 {
            if di != i {
                indices.insert(di * 9 + j);
            }
        }

        let li = (i / 3) * 3;
        let lj = (j / 3) * 3;
        for di in li..li + 3 {
            for dj in lj..lj + 3 {
                if di != i && dj != j {
                    indices.insert(di * 9 + dj);
                }
            }
        }

        indices
    }

    fn solve(&mut self) {
        let mut possibilities = FxHashMap::default();
        for k in 0..81 {
            if self.data[k as usize] == 0 {
                let values: FxHashSet<u8> = FxHashSet::from_iter(1..10);
                possibilities.insert(k, values);
            }
        }
        let unknown: FxHashSet<u8> = possibilities.iter().map(|(&k, _)| k).collect();

        let mut neighbors: FxHashMap<u8, FxHashSet<u8>> = FxHashMap::default();
        for k in 0..81 {
            let indices = Sudoku::get_neighbor_indices(k);
            neighbors.insert(k, indices.intersection(&unknown).map(|&k| k).collect());
        }

        for k in 0..81 {
            let n = self.data[k as usize];
            if n != 0 {
                for &di_dj in &neighbors[&k] {
                    if possibilities[&di_dj].contains(&n) {
                        if let Some(set) = possibilities.get_mut(&di_dj) {
                            set.remove(&n);
                        }
                    }
                }
            }
        }

        let mut stack = vec![(self.copy(), possibilities)];
        while !stack.is_empty() {
            let (mut state, mut poss) = stack.pop().unwrap();

            loop {
                let mut updated = false;
                let poss_keys: Vec<u8> = poss.keys().map(|&u| u).collect();
                for &k in &poss_keys {
                    let set = poss.get(&k).unwrap();
                    if set.len() == 1 {
                        let n = *set.iter().next().unwrap();
                        state.data[k as usize] = n;
                        poss.remove(&k);
                        for &di_dj in &neighbors[&k] {
                            if poss.contains_key(&di_dj) && poss[&di_dj].contains(&n) {
                                if let Some(set) = poss.get_mut(&di_dj) {
                                    set.remove(&n);
                                    updated = true;
                                }
                            }
                        }
                    }
                }

                if !updated {
                    break;
                }
            }

            if poss.is_empty() {
                self.data = state.data;
                return;
            }

            let mut min_len = 10; // max cannot exceed 9
            let mut min_k = 0;

            for (&k, set) in &poss {
                let len = set.len();
                if len < min_len {
                    min_len = len;
                    min_k = k;
                }
            }

            let values: Vec<u8> = poss[&min_k].iter().map(|&u| u).collect();
            if values.is_empty() {
                continue;
            }

            for &n in &values[1..] {
                let mut new_state = state.copy();
                let mut new_poss = FxHashMap::default();
                for (&k, set) in &poss {
                    new_poss.insert(k, set.clone());
                }
                new_state.data[min_k as usize] = n;
                if let Some(set) = new_poss.get_mut(&min_k) {
                    set.remove(&n);
                }
                stack.push((new_state, new_poss));
            }

            state.data[min_k as usize] = values[0];
            if let Some(set) = poss.get_mut(&min_k) {
                set.remove(&values[0]);
            }
            stack.push((state, poss));
        }

        panic!("Not solvable");
    }

    fn get_lines(&self) -> Vec<Vec<u8>> {
        let mut lines = Vec::new();
        for i in 0..9 {
            let mut line = Vec::new();
            for j in 0..9 {
                line.push(self.data[i * 9 + j]);
            }
            lines.push(line);
        }
        lines
    }

    fn get_columns(&self) -> Vec<Vec<u8>> {
        let mut columns = Vec::new();
        for j in 0..9 {
            let mut column = Vec::new();
            for i in 0..9 {
                column.push(self.data[i * 9 + j]);
            }
            columns.push(column);
        }
        columns
    }

    fn get_squares(&self) -> Vec<Vec<u8>> {
        let mut squares = Vec::new();
        for li in [0, 3, 6].iter() {
            for lj in [0, 3, 6].iter() {
                let mut square = Vec::new();
                for i in *li..*li + 3 {
                    for j in *lj..*lj + 3 {
                        square.push(self.data[i * 9 + j]);
                    }
                }
                squares.push(square);
            }
        }
        squares
    }

    fn is_solved(&self) -> bool {
        let full: FxHashSet<u8> = FxHashSet::from_iter(1..10);

        let parts = [self.get_lines(), self.get_columns(), self.get_squares()];

        for numbers in parts.iter().flat_map(|it| it.clone()) {
            let h: FxHashSet<u8> = FxHashSet::from_iter(numbers);
            if h != full {
                return false;
            }
        }
        true
    }
}

fn main() {
    let args: Vec<String> = env::args().collect();
    let mut sudoku = Sudoku::new(&args[1]);
    sudoku.solve();
    sudoku.show();
    debug_assert!(sudoku.is_solved());
}
