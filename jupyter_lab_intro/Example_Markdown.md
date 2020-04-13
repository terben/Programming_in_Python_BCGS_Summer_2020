# Markdown examples

This file gives examples of Markdown typesetting.

## Emphasis of text

Here some normal text.

Here some *italic* text.

Here some **bold** text.

## Enumerations

Here some itemization:
- point 1
- point 2
- point 3

Here some enumeration:
1. point 1
2. point 2
3. point 3

## Mathematics with LaTeX

Here some math with $\LaTeX$:
\begin{equation}
\end{equation}

## Typesetting Code-blocks

Markdown can syntax-highlight and typeset code
from all well-known languages.

Short syntax phrases within the text are done like
`print("Hello World!")`. Language specific and larger
blocks are done like this for `C`:

```c
#include<stdio.h>

int main(void) {
  /* This is a simple C program */
  int a, b;

  a = 1;
  b = 2;
  
  printf("Hello World!\n");
  printf("%d %d\n", a, b);
}
```

or

```python
# This is a simple Python program

a = 1
b = 2
print("Hello World!")
print(a, b)
```

## Links
More Markdown can be found [here](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet).