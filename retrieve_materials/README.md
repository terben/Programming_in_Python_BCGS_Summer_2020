# How to download course materials

Those familiar with `git` and `github` should doenload and
administrate the ocurse materials with `git`-commands. We will
introduce `git` and the concepts of *version control* at the end of
the term.

A way to obtain the materials easily without `git`-knowledge is:

1. Create a directory, where you want to store course materials. This
only needs to be done once for the whole course.

2. Go to that directory and execute:

   ```
   user$ bash get_current_course_materials.sh
   Cloning into 'Programming_in_Python_Bonn_Summer_2018'...
   .
   .
   user$ ls
   python_course_2018-04-10 ... # 2018-04-10 needs to be subtituted
                                # by the current date
   user$ cd python_course_2018-04-10
   user$ jupyter notebook       # to start working on the notebooks
   ```
