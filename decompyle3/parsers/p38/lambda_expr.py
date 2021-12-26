#  Copyright (c) 2020-2021 Rocky Bernstein
#
#  This program is free software: you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""
Differences over Python 3.7 for Python 3.8 in the Earley-algorithm lambda grammar
"""

from decompyle3.parsers.p37.lambda_expr import Python37LambdaParser
from decompyle3.parsers.parse_heads import (
    PythonParserLambda,
    PythonBaseParser,
)

from spark_parser import DEFAULT_DEBUG as PARSER_DEFAULT_DEBUG


class Python38LambdaParser(Python37LambdaParser, PythonParserLambda):
    def p_38walrus(self, args):
        """
        # named_expr is also known as the "walrus op" :=
        expr              ::= named_expr
        named_expr        ::= expr DUP_TOP store
        """

    def __init__(
        self,
        start_symbol: str = "lambda_start",
        debug_parser: dict = PARSER_DEFAULT_DEBUG,
    ):
        PythonParserLambda.__init__(
            self, debug_parser=debug_parser, start_symbol=start_symbol
        )
        PythonBaseParser.__init__(
            self, start_symbol=start_symbol, debug_parser=debug_parser
        )
        self.customized = {}


if __name__ == "__main__":
    # Check grammar
    from decompyle3.parsers.dump import dump_and_check

    p = Python38LambdaParser()
    modified_tokens = set(
        """JUMP_BACK CONTINUE RETURN_END_IF COME_FROM
           LOAD_GENEXPR LOAD_ASSERT LOAD_SETCOMP LOAD_DICTCOMP LOAD_CLASSNAME
           LAMBDA_MARKER RETURN_LAST
        """.split()
    )

    dump_and_check(p, (3, 8), modified_tokens)
