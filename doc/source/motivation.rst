Motivation
==========

Replicability---the ability for someone else to do exactly what you did at some
point in the past, on the same or an equivalent machine, using the same tooling
you used, and achieve the same results---is `a complex problem`_.  When someone
has a problem running a script, there's often a good deal of time wasted
iterating back and forth between the person having the problem and those who
might be able to help them solve it.  Questions such as the following arise:

.. _a complex problem: https://zenodo.org/record/7754004

* What kind of machine are you using?
* What's your environment look like?
* What did you run at the command line?
* Can you provide all the output?

And in our asynchronous work environment, there's often quite a bit of time
spent waiting for the person on the other end of the conversation to come back
to it, think about a response, and then move the conversation forward.
Frustration can build throughout, especially when you run into, "I just ran the
same thing you did, and it worked fine for me."

While tackling the issue of rock-solid replicability is far beyond the scope of
a single package, ``reverse_argparse`` aims to make life a little bit easier
when it comes to this last issue.

What Exactly Did You Run?
-------------------------

When your Python script requires input from the user, the go-to solution is the
:mod:`argparse` module in the standard library, which makes it easy to write
user-friendly command-line interfaces.  As scripts grow in complexity, it's
common for the number of command-line arguments to grow, but then, for
simplicity's sake, it's recommended to use default values wisely such that the
user isn't required to specify dozens of arguments each time they run the
script.

In such a scenario, asking someone what they ran in the terminal may be
insufficient, because

.. code-block:: bash

   python3 my_script.py --foo bar

for one person, in one environment, in one location, on one machine, may be
different from the same line executed by a different person, in a different
environment, in a different location, on a different machine.

What Might Go Wrong?
--------------------

The differences that may occur generally fall into three categories.

When default values change
^^^^^^^^^^^^^^^^^^^^^^^^^^

Say you're using one version of the script, and your collaborator is using a
different one (perhaps they're working on another branch).  In your version

.. code-block:: bash

   python3 my_script.py --foo bar

translates to

.. code-block:: bash

   python3 my_script.py --foo bar --baz

but in their version it translates to

.. code-block:: bash

   python3 my_script.py --foo bar --no-baz
   #                                ^^^

because someone updated a default value.  You'll probably spend a good deal of
time playing around with the debugger or print statements before you figure out
the switch.

When using relative references
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Changes in default values hopefully occur infrequently.  Perhaps a more common
occurrence is when using relative references.  Say a script requires some file
as input, so you run

.. code-block:: bash

   python3 my_script.py --foo bar.txt

and this translates to

.. code-block:: bash

   python3 my_script.py --foo /path/to/some-dir/bar.txt

However, your colleague, not having all the information needed to replicate
your error, runs the exact same thing, but it translates to

.. code-block:: bash

   python3 my_script.py --foo /path/to/some-other-dir/bar.txt
   #                                   ^^^^^^^^^^^^^^

There's no telling how long you two will go back and forth before realizing
that your relative references resolved to different files.

When arguments are post-processed
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

A final potential source of confusion is when arguments go through some amount
of post-processing after they're read in via
:meth:`argparse.ArgumentParser.parse_args`.  For instance, perhaps the input is
normalized in some way, as in the case where

.. code-block:: bash

   python3 my_script.py --start-time '30 minutes ago'

translates to

.. code-block:: bash

   python3 my_script.py --start-time '2023-07-01T12:34:56Z'

but when your colleague gets around to running your script a few days later,
the exact same line translates to

.. code-block:: bash

   python3 my_script.py --start-time '2023-07-05T05:43:21Z'

Who knows how long it'll take you two to figure out you're actually looking at
different data sets under the hood?

What's the Solution?
--------------------

The ``reverse_argparse`` module aims to solve these problems for you.  It takes
as input two things:

1. The :class:`argparse.Namespace` of parsed arguments, which already accounts
   for any default values applied, and any post-processing you might've done
   with them.
2. The :class:`argparse.ArgumentParser` that parsed the arguments.

These two are then used to undo the parsing such that you can generate a string
of the complete, effective command line invocation of the script.  When someone
asks what you ran in the terminal, you can give them this string and avoid a
good deal of wasted time, confusion, and frustration, which will hopefully help
you solve your problems more quickly.
