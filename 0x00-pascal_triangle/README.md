# Pascal's Triangle

## Description
> Solving the Pascal's tringle problem to prepare for job interviews.

### Problem Statement
- Create a function `def pascal_triangle(n):` that returns a list of lists of integers representing the Pascal’s triangle of `n`:
    * Returns an empty list if `n <= 0`.
    * Assume `n` is always positive.
<br>

### Example Test Environment

```
➜  0x00-pascal_triangle git:(master)$ cat 0-main.py
#!/usr/bin/python3
"""
0-main
"""
pascal_triangle = __import__('0-pascal_triangle').pascal_triangle

def print_triangle(triangle):
    """
    Print the triangle
    """
    for row in triangle:
        print("[{}]".format(",".join([str(x) for x in row])))


if __name__ == "__main__":
    print_triangle(pascal_triangle(5))

➜  0x00-pascal_triangle git:(master)$ 
➜  0x00-pascal_triangle git:(master)$ ./0-main.py
[1]
[1,1]
[1,2,1]
[1,3,3,1]
[1,4,6,4,1]
➜  0x00-pascal_triangle git:(master)$ 
```

## Author
- Siphamandla Matshiane, ![X (formerly Twitter) URL](https://img.shields.io/twitter/url?url=https%3A%2F%2Fx.com%2FSiphamandl76892)

## LICENSE
- [ALX Software Engineering Plus](https://tech.alxafrica.com/software-engineering-plus-programme-johannesburg)
