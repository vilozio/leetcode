from dataclasses import dataclass, field
from typing import List, Dict, Tuple


@dataclass
class Bracket:
    stack: List[int] = field(default_factory=list)
    counter: int = 0
    threshold: int = 0


class Solution:
    def isValid(self, s: str) -> bool:
        brackets: Dict[Tuple, Bracket] = {
            ('{', '}'): Bracket(),
            ('[', ']'): Bracket(),
            ('(', ')'): Bracket(),
        }
        for c in s:
            for bracket_key in brackets.keys():  # search for a bracket type
                if c in bracket_key:
                    bracket = brackets[bracket_key]
                    rest_brackets = [b for k, b in brackets.items() if k != bracket_key]
                    if c == bracket_key[0]:
                        bracket.counter += 1
                        for other_bracket in rest_brackets:
                            other_bracket.stack.append(other_bracket.threshold)
                            other_bracket.threshold = other_bracket.counter
                    if c == bracket_key[1]:
                        bracket.counter -= 1
                        if bracket.counter < bracket.threshold:
                            return False
                        for other_bracket in rest_brackets:
                            if other_bracket.counter != other_bracket.threshold:
                                return False
                            if other_bracket.stack:
                                other_bracket.threshold = other_bracket.stack.pop()
                    break  # found the bracket type, stop search
        if any(b.counter != 0 for b in brackets.values()):
            return False
        return True


def call(string):
    s = Solution()
    return s.isValid(string)


def test():
    assert call('') is True
    assert call('()') is True
    assert call('()[]{}') is True
    assert call('(]') is False
    assert call(')(') is False
    assert call(')))') is False
    assert call('(((') is False
    assert call('[(])') is False
    assert call('[)]') is False
    assert call('([{({[(({(())}))]})}])') is True
    assert call('([{({[(({(())})]})}])') is False
    assert call('([{({[(({(()}))]})}])') is False
    assert call('([{({[((({(()}))]})}])') is False
    assert call('((())))') is False
    assert call('((())))') is False
    assert call('({})[(({}))]({)}') is False
    assert call('({})[(({}))](){}') is True
    assert call('({})[(({}))]()}') is False
