from enum import StrEnum, auto
from typing import Any

class TokenType(StrEnum):
    STRING = auto()
    NUMBER = auto()
    BOOLEAN = auto()
    NULL =auto()
    LEFT_BRACE = auto()
    RIGHT_BRUCE = auto()
    LEFT_BRACKET = auto()
    RIGHT_BRACKET = auto()
    COMMA = auto()
    COLON = auto()
    EOF = auto()


class Token:
    def __init__(self, token_type : TokenType, value: Any):
        self.tokentype = token_type
        self.value = value

class Scanner:
    tokens : list[Token]
    def __init__(self, source: str):
        self.source = source
        self.start = 0
        self.tokens = []
        self.current = 0
        self.line = 1

    def scan(self) -> list[Token]:
        while self.is_not_end():
            self.start = self.current
            self.scan_token()
        self.tokens.append(Token(TokenType.EOF, None))
        return self.tokens
    
    

