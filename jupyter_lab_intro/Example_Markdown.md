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
  \sum_{n=0}^{\infty} \frac{x^{n}}{n!} = \exp(x)
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

## Include images
Markdown supports the inclusion of images
<img src="../Wednesday_2020-04-08/images/NGVS_mask.jpg" width="400" height="200" />

Here an image from the WEB:
<img src="http://img.youtube.com/vi/Dvgn0Vt8WnA/0.jpg" width="400" height="200" />

### Coloured text boxes
<div class="alert alert-success">
<b>Green text box.</b>
<ul>
    <li> Item 1 </li>
    <li> Item 2 </li>
</ul>
</div>

- Blue text box: alert-success -> alert-info
- Yellow box: alert-success -> alert-warning
- Yellow box: alert-success -> alert-danger
