r"""*Mini-language parser for* ``pent``.

``pent`` Extracts Numerical Text.

**Author**
    Brian Skinn (bskinn@alum.mit.edu)

**File Created**
    8 Sep 2018

**Copyright**
    \(c) Brian Skinn 2018

**Source Repository**
    http://www.github.com/bskinn/pent

**Documentation**
    http://pent.readthedocs.io

**License**
    The MIT License; see |license_txt|_ for full license terms

**Members**

"""

import itertools as itt
import re

import attr

from .enums import SpaceAfter, ParserField
from .errors import SectionError
from .patterns import std_wordify_open, std_wordify_close
from .thrulist import ThruList
from .token import Token


@attr.s(slots=True)
class Parser:
    """Mini-language parser for structured numerical data."""

    head = attr.ib(default=None)
    body = attr.ib(default=None)
    tail = attr.ib(default=None)

    def pattern(self, capture_sections=True):
        """Return the regex pattern for the entire parser.

        The individual capture groups are NEVER inserted when
        regex is generated this way.

        Instead, head/body/tail capture groups are inserted,
        in order to subdivide matched text by these subsets.
        These 'section' capture groups are ONLY inserted for the
        top-level Parser, though -- they are suppressed for inner
        nested Parsers.

        """
        res_head = self.convert_section(self.head, capture_sections=False)
        res_body = self.convert_section(self.body, capture_sections=False)
        res_tail = self.convert_section(self.tail, capture_sections=False)

        rx = ""

        if res_head:
            head_pat, head_opt = res_head
            rx += (
                "(?P<{}>".format(ParserField.Head) + head_pat + ")\n?"
                if capture_sections
                else head_pat + "\n?"
            )

        if res_body:
            body_pat, body_opt = res_body
            
            return_opt = body_opt
            
            # At least one line of the body, followed by however many more
            rx += (
                (
                    "(?P<{}>".format(ParserField.Body)
                    if capture_sections
                    else ""
                )
                + body_pat
                + "(\n?"
                + body_pat
                + ")*"
                + (")" if capture_sections else "")
            )
        else:
            raise SectionError("'body' required to generate 'pattern'")

        if res_tail:
            tail_pat, tail_opt = res_tail
            
            return_opt = tail_opt
            
            rx += (
                "\n?"
                + ( "(?P<{}>".format(ParserField.Tail) + tail_pat + ")"
                    if capture_sections
                    else tail_pat
                  )
            )

        return rx, return_opt

    def capture_body(self, text):
        """Capture all values from the pattern body, recursing if needed."""
        cap_blocks = []
        for m_entire in re.finditer(self.pattern()[0], text):
            block_text = m_entire.group(ParserField.Body)

            # If the 'body' pattern is a Parser
            if isinstance(self.body, self.__class__):
                data = []
                body_subpat = self.body.pattern(capture_sections=True)[0]

                for m in re.finditer(body_subpat, block_text):
                    data.extend(self.body.capture_body(m.group(0)))

                cap_blocks.append(data)
                continue

            # If the 'body' pattern is a string or iterable of strings
            cap_blocks.append(self.capture_str_pattern(self.body, block_text))

        return cap_blocks

    def capture_struct(self, text):
        """Perform capture of marked groups to nested dict(s)."""
        return self.capture_parser(self, text)

    @classmethod
    def capture_section(cls, sec, text):
        """Perform capture of a str, iterable, or Parser section."""
        if isinstance(sec, cls):
            return cls.capture_parser(sec, text)
        else:
            return cls.capture_str_pattern(sec, text)

    @classmethod
    def capture_str_pattern(cls, pat_str, text):
        """Perform capture of string/iterable-of-str pattern."""
        try:
            pat_re = cls.convert_section(pat_str, capture_groups=True)[0]
        except AttributeError:
            raise SectionError("Invalid pattern string for capture")

        data = []
        for m in re.finditer(pat_re, text):
            chunk_caps = []
            for c in cls.generate_captures(m):
                if c is None:
                    chunk_caps.append(None)
                else:
                    chunk_caps.extend(c.split())
            data.append(chunk_caps)

        return data

    @classmethod
    def capture_parser(cls, prs, text):
        """Perform capture of a Parser pattern."""
        data = ThruList()

        prs_pat_re = prs.pattern(capture_sections=True)[0]

        for m in re.finditer(prs_pat_re, text):
            sec_dict = {}

            for sec in ParserField:
                try:
                    sec_dict.update(
                        {
                            sec: cls.capture_section(
                                getattr(prs, sec), m.group(sec)
                            )
                        }
                    )
                except IndexError:
                    sec_dict.update({sec: None})

            data.append(sec_dict)

        return data

    @classmethod
    def convert_section(cls, sec, capture_groups=False, capture_sections=True):
        """Convert the head, body or tail to regex."""
        # Could be None
        if sec is None:
            return None

        # If it's a Parser
        try:
            return sec.pattern(capture_sections=capture_sections)
        except AttributeError:
            pass

        # If it's a single line
        try:
            return cls.convert_line(sec, capture_groups=capture_groups)[0::2]
        except AttributeError:
            pass

        # If it's an iterable of lines
        def gen_converted_lines():
            id = 0
            for line in sec:
                pat, id, opt = cls.convert_line(
                    line, capture_groups=capture_groups, group_id=id
                )
                yield pat  # , opt

        try:
            return "\n?".join(gen_converted_lines()), True
            #pattern = ""
            #for line, opt in gen_converted_lines():
            #    pattern += line + r"\n"
            #    if opt:
            #        pattern += "?"
            
            # Have to strip the last newline
            #pattern = pattern[:(-3 if opt else -2)]
            
            return pattern, True  # opt
                
        except AttributeError:
            # Happens to be the exception that the internals
            # throw when the wrong type is passed.
            raise SectionError("Unrecognized format")

    @classmethod
    def convert_line(cls, line, *, capture_groups=True, group_id=0):
        """Convert line of tokens to regex.

        The constructed regex is required to match the entirety of a
        line of text, using lookbehind and lookahead at the
        start and end of the pattern, respectively.

        `group_id` indicates the starting value of the index for any
        capture groups added.

        """
        import shlex
        
        from .errors import LineError

        # Parse line into tokens, and then into Tokens
        tokens = shlex.split(line)
        tokens = list(Token(_, do_capture=capture_groups) for _ in tokens)

        # Zero-length start of line (or of entire string) match
        pattern = r"(^|(?<=\n))"
        
        # Replace target for the opening paren if the line is optional
        pattern += "{opline_open}"

        # Always have optional starting whitespace
        pattern += r"[ \t]*"

        # Initialize flag for a preceding no-space-after num token
        prior_no_space_token = False
        
        # Initialize flag for whether the line is optional
        optional_line = False

        for i, t in enumerate(tokens):
            tok_pattern = t.pattern

            if t.is_optional_line:
                if i == 0:
                    optional_line = True
                    continue
                else:
                    raise LineError(line)

            if t.needs_group_id:
                tok_pattern = tok_pattern.format(str(group_id))
                group_id += 1

            if t.is_any:
                pattern += tok_pattern
                prior_no_space_token = False

            else:
                if not prior_no_space_token:
                    tok_pattern = std_wordify_open(tok_pattern)

                if t.space_after is SpaceAfter.Required:
                    tok_pattern = std_wordify_close(tok_pattern)
                    prior_no_space_token = False
                else:
                    prior_no_space_token = True

                pattern += tok_pattern

            # Add required space, optional space, or no space, depending
            # on what the token calls for, as long as it's not
            # the last token
            if i < len(tokens) - 1:
                if t.space_after is SpaceAfter.Required:
                    pattern += r"[ \t]+"
                elif t.space_after is SpaceAfter.Optional:
                    pattern += r"[ \t]*"

        # Always put possible whitespace to the end of the line.
        # Also include a format tag for closing optional-line grouping
        pattern += r"[ \t]*{opline_close}($|(?=\n))"

        # Wrap pattern with parens and '?' if it's optional
        # Otherwise just drop the formatting tags
        pattern = pattern.format(
            opline_open=("(" if optional_line else ""),
            opline_close=(")?" if optional_line else "")
            )

        return pattern, group_id, optional_line

    @staticmethod
    def generate_captures(m):
        """Generate captures from a regex match."""
        for i in itt.count(0):
            try:
                yield m.group(Token.group_prefix + str(i))
            except IndexError:
                break


if __name__ == "__main__":  # pragma: no cover
    print("Module not executable.")
