.. pent mini-language grammar

pent Mini-Language Grammar
==========================

*Intro text*

 * head/body/tail paradigm

 * Any of the three can be:

   * String (token pattern for a single line of text)
   * Ordered iterable of strings (token patterns for a
     specific sequence of lines of text)
   * A :class:`~pent.Parser` instance

 * String of tokens always corresponds to a single line of text

 * For head/tail, at each level, the pattern (whether one line,
   multiple lines, or a Parser) is matched ONCE

 * For body, the entire pattern is matched ONE OR MORE TIMES

 * A line-string can be empty, meaning a line containing nothing OR
   only whitespace

 * First token can be "?", marking the line as OPTIONAL in the pattern
   (DOESN'T ALWAYS WORK RIGHT!)

