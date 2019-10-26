## CHANGELOG: pent - Pent Extracts Numerical Text

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](http://keepachangelog.com/en/1.0.0/)
and this project adheres to [Semantic Versioning](http://semver.org/spec/v2.0.0.html).

### [Unreleased]

#### Fixed

- Optional-line flag behavior now fixed and ~thoroughly tested.
  Required a change to the accepted behavior, such that an optional pattern
  matches (1) the line specified, (2) a blank line, or (3) no line.

#### Changed

- The semantics of the 'decimal' and 'float' number tokens have been swapped.
  'Decimal' tokens will only match non-scientific-notation decimal values, while
  'float' values match either 'decimal' or 'scinot' formatted values.

### v0.2.0rc1 [2018-10-28]

#### Added

- "Misc" token type, '&', matching arbitrary non-whitespace content
- Optional whitespace can now be specified after number, literal, and misc
  tokens, in addition to 'required whitespace after' and
  'no whitespace after'
- New helper function `column_stack_2d`
  - Needs performance improvements for large arrays
- New 'optional line' token type
  - Works irregularly, perhaps due to quirks in managing optional
    groups/capture groups within the Python regex engine?
- New property flags on `Token` to indicate the new features added
  ('misc' token type, optional-whitespace-after, etc.)

#### Changed

- Switched certain lists within the `Parser.capture_struct` return
  dict structure to a type that automatically passes through a dict key to the
  single element of those lists, if they are length-one. This
  simplifies the syntax of a number of use cases by eliminating explicit `[0]`
  indexing.
- `Parser` instances now syntax-check their `head`/`body`/`tail` patterns
   at instantiation, instead of at the first capture attempt.


### v0.1.0 [2018-09-23]

#### Features

- Three token types implemented to date: numeric, string-literal, "any"
- Parsing of multiple levels of recursive nested data; tested only
  to two leves of nesting to date.
- Each nested level of structure can have head/body/tail
- Captured tokens can be easily retrieved from head/tail at the top level
  parser; no good head or tail capture yet from within nested structures

