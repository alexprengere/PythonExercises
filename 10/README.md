## Exercise 10

### Problem

Sara is training for a Marathon. This is her last meal and she wants to optimize her food intake.
She has prepared a list of dishes she can eat, each one has two characteristics:
* weight
* carbohydrates level (a percentage)

For this meal, she cannot eat more than 600g, then she is full! But she wants to digest as much carbohydrates as possible.
One last thing: if she picks a dish to eat, she will finish it (no waste!), so it is not possible to select half a dish.

The list of dishes is stored in a file with this format: dish name, mass (g), carbohydrates (%).
```bash
$ cat dishes.txt
Rice 200 15
Pasta 300 12
Cake 150 3
Icecream 50 5
```

Please help her find the optimal meal! You can make a script working like this:
```bash
$ python optimize_meal.py dishes.txt 600
Optimal meal <= 600g:
Rice
Icecream
...
```

### Help

This is actually a variant of the [Knapsack problem](https://en.wikipedia.org/wiki/Knapsack_problem).
