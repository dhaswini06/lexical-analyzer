import re

TOKENS = [
    ("KEYWORD", r"\b(int|if|else|while|return)\b"),
    ("NUMBER", r"\b\d+\b"),
    ("IDENTIFIER", r"\b[a-zA-Z_][a-zA-Z0-9_]*\b"),
    ("OPERATOR", r"[+\-*/=]"),
    ("SEMICOLON", r";"),
    ("LPAREN", r"\("),
    ("RPAREN", r"\)"),
    ("WHITESPACE", r"\s+"),
]

def lexical_analyzer(code):
    position = 0
    tokens = []

    while position < len(code):
        match = None

        for token_type, pattern in TOKENS:
            regex = re.compile(pattern)
            match = regex.match(code, position)

            if match:
                text = match.group(0)
                if token_type != "WHITESPACE":
                    tokens.append((token_type, text))
                position = match.end()
                break

        if not match:
            print(f"Error: Invalid character '{code[position]}' at position {position}")
            return None

    return tokens


if __name__ == "__main__":
   
    source_code = input("Enter your code to analyze: ")
    
    result = lexical_analyzer(source_code)

    if result:
        print("\nTokens Found:")
        for token in result:
            print(token)
