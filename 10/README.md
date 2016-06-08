## Exercise 10

### Problem

Sara is training for a Marathon. This is her last meal and she wants to optimize her food intake.
She has prepared a list of things she can eat, each one has two characteristics:
* the mass
* the carbohydrates level (a percentage)

For this meal, she cannot eat more than 600g, then she is full! But she wants to digest as much carbohydrates as possible.

The food list is stored in a file with this order: food, mass (gr), carbohydrates (%).
```bash
$ cat food.txt
Rice 200 15
Pasta 300 12
Cake 150 3
Icecream 50 5
```

One last thing: if she picks a food to eat, she will finish it (no waste!), so it is not possible to select half of something.

Please help her find the optimal meal! You can design a script working like this:
```bash
$ python find_food.py food.txt 600
Optimal meal for less than 600gr:
Rice
Icecream
...
```

### Help

This is actually a variant of the [Knapsack problem](https://en.wikipedia.org/wiki/Knapsack_problem).
