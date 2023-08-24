Examples
========

The following examples illustrate both the usage and the utility of
``reverse_argparse``.  They build on each other in complexity, so it will make
the most sense to start here at the top and work your way down through each in
turn.

The Basics
----------

When using a bare-bones :class:`argparse.ArgumentParser`, ``reverse_argparse``
doesn't really provide much benefit, but it's instructive to see how
straightforward it is to get up and running with it.

.. literalinclude:: ../../example/basic.py
   :language: python
   :linenos:
   :caption: ``example/basic.py``
   :emphasize-lines: 5,16-19

.. note::

   The only thing you're adding to your script to take advantage of
   ``reverse_argparse`` is lines 7 and 19--22.

Running the script, and passing an argument to it, yields the following:

.. command-output:: python3 ../../example/basic.py --foo bar

Default Values
--------------

Let's now take the prior example and add some complexity to it by adding more
arguments, but this time with default values.

.. literalinclude:: ../../example/default_values.py
   :language: python
   :linenos:
   :caption: ``example/default_values.py``
   :emphasize-lines: 10-11

Now running the script with the same command line arguments yields:

.. command-output:: python3 ../../example/default_values.py --foo bar

Relative References
-------------------

We can complicate things further by adding an argument representing a path.
Though the user is free to specify a relative path on the command line, this
will be translated to an absolute path behind the scenes.

.. literalinclude:: ../../example/relative_references.py
   :language: python
   :linenos:
   :caption: ``example/relative_references.py``
   :emphasize-lines: 3,13

Now running the script and pointing to a file in your current working directory
yields:

.. command-output:: python3 ../../example/relative_references.py --src bar.txt

Argument Post-Processing
------------------------

The example above is actually a special case of any general post-processing of
arguments that you might like to do after they are initially parsed.  Consider
an example of normalizing a date/time from whatever the user specifies to a
standard format.

.. literalinclude:: ../../example/post_processing.py
   :language: python
   :linenos:
   :caption: ``example/post_processing.py``
   :emphasize-lines: 6,16,20-21

Now running the script and specifying a relative date/time yields:

.. command-output:: python3 ../../example/post_processing.py --before '30 minutes ago'

Pretty-Printing the Effective Command
-------------------------------------

In all of the above, the effective command line invocation will be printed on a
single line.  Often this is what you want, as it facilitates easy copying and
pasting.  However, when your script grows in complexity, you may want to
pretty-print the output such that it's easier to see at a glance what all the
different flags and corresponding values are.

.. literalinclude:: ../../example/pretty_printing.py
   :language: python
   :linenos:
   :caption: ``example/pretty_printing.py``
   :emphasize-lines: 28

Now running the script and specifying a relative date/time yields:

.. command-output:: python3 ../../example/pretty_printing.py --foo eggs --src file.txt --before 'today'

Subparsers
----------

A special case you might be concerned with is that of an
:class:`argparse.ArgumentParser` with multiple `subparsers`_ or sub-commands,
each of which will have its own arguments, and even potentially nested
subparsers.  When using :meth:`get_effective_command_line_invocation`, you
won't notice anything different, but :meth:`get_pretty_command_line_invocation`
shows the subtle difference.

.. _subparsers: https://docs.python.org/3/library/argparse.html#sub-commands

.. literalinclude:: ../../example/subparsers.py
   :language: python
   :linenos:
   :caption: ``example/subparsers.py``
   :emphasize-lines: 11-18

Running this script and using the ``foo`` subcommand yields:

.. command-output:: python3 ../../example/subparsers.py foo --one eggs

.. note::

   The arguments associated with the subparser have been indented by an extra
   level.  If there are subparsers within subparsers, ``reverse_argparse``
   keeps track of the indentation level while unparsing, so the user can easily
   see which arguments correspond to which subparser.
