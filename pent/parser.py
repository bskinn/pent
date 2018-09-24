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

from .enums import ParserField
from .errors import SectionError
from .patterns import std_wordify_open, std_wordify_close
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
        # Relies on the convert_section default for 'capture_groups'
        # as False.
        rx_head = self.convert_section(self.head, capture_sections=False)
        rx_body = self.convert_section(self.body, capture_sections=False)
        rx_tail = self.convert_section(self.tail, capture_sections=False)
        #        rx_head, rx_body, rx_tail = map(
        #            self.convert_section, (self.head, self.body, self.tail)
        #        )

        rx = ""

        if rx_head:
            rx += (
                "(?P<{}>".format(ParserField.Head) + rx_head + ")\n"
                if capture_sections
                else rx_head + "\n"
            )

        try:
            # At least one line of the body, followed by however many more
            rx += (
                (
                    "(?P<{}>".format(ParserField.Body)
                    if capture_sections
                    else ""
                )
                + rx_body
                + "(\n"
                + rx_body
                + ")*"
                + (")" if capture_sections else "")
            )
        except TypeError as e:
            raise SectionError("'body' required to generate 'pattern'") from e

        if rx_tail:
            rx += (
                "\n(?P<{}>".format(ParserField.Tail) + rx_tail + ")"
                if capture_sections
                else "\n" + rx_tail
            )

        return rx

    def capture_head(self, text):
        """Capture all marked values from the pattern head."""
        m_entire = re.search(self.pattern(), text)
        head = m_entire.group(ParserField.Head)

        pat_capture = self.convert_section(self.head, capture_groups=True)
        m_head = re.search(pat_capture, head)

        return list(*map(str.split, self.generate_captures(m_head)))

    def capture_tail(self, text):
        """Capture all marked values from the pattern tail."""
        m_entire = re.search(self.pattern(), text)
        tail = m_entire.group(ParserField.Tail)

        pat_capture = self.convert_section(self.tail, capture_groups=True)
        m_tail = re.search(pat_capture, tail)

        return list(*map(str.split, self.generate_captures(m_tail)))

    def capture_body(self, text):
        """Capture all values from the pattern body, recursing if needed."""
        cap_blocks = []
        for m_entire in re.finditer(self.pattern(), text):
            block_text = m_entire.group(ParserField.Body)

            # If the 'body' pattern is a Parser
            if isinstance(self.body, self.__class__):
                data = []
                body_subpat = self.body.pattern(capture_sections=True)

                for m in re.finditer(body_subpat, block_text):
                    data.extend(self.body.capture_body(m.group(0)))

                cap_blocks.append(data)
                continue

            # If the 'body' pattern is a string or iterable of strings
            try:
                pat = self.convert_section(self.body, capture_groups=True)
            except AttributeError:
                raise SectionError("Invalid 'body' pattern for capture")
            else:
                data = []
                for m in re.finditer(pat, block_text):
                    line_caps = []
                    for c in self.generate_captures(m):
                        line_caps.extend(c.split())
                    data.append(line_caps)

                cap_blocks.append(data)
                continue

        return cap_blocks

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
            return cls.convert_line(sec, capture_groups=capture_groups)[0]
        except AttributeError:
            pass

        # If it's an iterable of lines
        def gen_converted_lines():
            id = 0
            for line in sec:
                pat, id = cls.convert_line(
                    line, capture_groups=capture_groups, group_id=id
                )
                yield pat

        try:
            return "\n".join(gen_converted_lines())
        except AttributeError:
            # Most likely is that the iterable members don't have
            # the .pattern attribute
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

        # Parse line into tokens, and then into Tokens
        tokens = shlex.split(line)
        tokens = list(Token(_, do_capture=capture_groups) for _ in tokens)

        # Zero-length start of line (or of entire string) match
        pattern = r"(^|(?<=\n))"

        # Always have optional starting whitespace
        pattern += r"[ \t]*"

        # Initialize flag for a preceding no-space-after num token
        prior_no_space_token = False

        for i, t in enumerate(tokens):
            tok_pattern = t.pattern

            if t.needs_group_id:
                tok_pattern = tok_pattern.format(str(group_id))
                group_id += 1

            if t.is_any:
                pattern += tok_pattern
                prior_no_space_token = False

            else:
                if not prior_no_space_token:
                    tok_pattern = std_wordify_open(tok_pattern)

                if t.space_after:
                    tok_pattern = std_wordify_close(tok_pattern)
                    prior_no_space_token = False
                else:
                    prior_no_space_token = True

                pattern += tok_pattern

            # Add required space or no space, depending on
            # what the token calls for, as long as it's not
            # the last token
            if i < len(tokens) - 1 and t.space_after:
                pattern += r"[ \t]+"

        # Always put possible whitespace to the end of the line
        pattern += r"[ \t]*($|(?=\n))"

        return pattern, group_id

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
