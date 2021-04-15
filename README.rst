.. This README is meant for consumption by humans and pypi. Pypi can render rst files so please do not use Sphinx features.
   If you want to learn more about writing documentation, please check out: http://docs.plone.org/about/documentation_styleguide.html
   This text does not appear on pypi or github. It is a comment.

==============================================================================
kitconcept.workingcopy
==============================================================================

.. image:: https://kitconcept.com/logo.svg
   :alt: kitconcept
   :target: https://kitconcept.com/


.. image:: https://github.com/kitconcept/kitconcept.workingcopy/actions/workflows/ci.yml/badge.svg
    :target: https://github.com/kitconcept/kitconcept.workingcopy/actions/workflows/ci.yml

Installation
------------

Install kitconcept.workingcopy by adding it to your buildout:

```
[buildout]

...

eggs =
    ...
    kitconcept.workingcopy
```

and then running bin/buildout


Contribute
----------

Issue Tracker: https://github.com/kitconcept/kitconcept.workingcopy/issues
Source Code: https://github.com/kitconcept/kitconcept.workingcopy


Development
-----------

Requirements:

- Python 3.8
- Plone 5.2
- Volto

Setup::

  make

Run Static Code Analysis::

  make code-Analysis

Run Unit / Integration Tests::

  make test

Run Robot Framework based acceptance tests::

  make test-acceptance
