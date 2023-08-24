reverse_argparse
================

.. toctree::
   :hidden:
   :maxdepth: 2
   :caption: Contents

   motivation
   examples
   reference

The ``reverse_argparse`` module provides a means of undoing the argument
parsing provided by :mod:`argparse`.  That is, it can take a
:class:`argparse.Namespace` of parsed command line arguments, along with the
:class:`argparse.ArgumentParser` that generated it, and then unparse everything
into the exact list of command line arguments that was used when executing the
script.

"But wait, if I just ran a script on the command line, I can see what I just
typed in.  Why would the script need to figure that out again so it could tell
me something I can see right in front of me?"

Because ``reverse_argparse`` will take into consideration any default values,
along with any transformations that have been made after argument parsing
(e.g., path resolution, etc.).  For more details on why this matters, check out
the :doc:`motivation` page.

Installation
------------

To get up and running with ``reverse_argparse``, simply

.. code-block:: bash

   python3 -m pip install reverse-argparse

Usage
-----

Once the package is installed, you can simply

.. code-block:: python
   :emphasize-lines: 3,13-16

   from argparse import ArgumentParser

   from reverse_argparse import ReverseArgumentParser

   # Parse the command line arguments.
   parser = ArgumentParser()
   # Build out the parser however you like.
   args = parser.parse_args()
   # Optionally post-process any arguments, as needed.

   # Do whatever you need to in the script.

   # Wrap things up.
   print("This script executed the following:")
   unparser = ReverseArgumentParser(parser, args)
   print(unparser.get_pretty_command_line_invocation())

For more detailed usage information, see the :doc:`examples` page.  For
implementation details, see the :doc:`reference documentation <reference>`.

Contributing
------------

The source repository for this module is `on GitHub`_.  See the project's
README and contributing guidelines for details on how to interact with the
project.

.. _on GitHub:  https://github.com/sandialabs/reverse_argparse
