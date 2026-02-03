# lexical-analyzer
“Implementation of a lexical analyzer in Python for compiler design coursework.”
# Lexical Analyzer (Lexer) in Python

A simple, rule-based **Lexical Analyzer** built for Compiler Design. This program takes raw source code as input and breaks it down into a stream of meaningful **tokens** using Regular Expressions (Regex).

## 🚀 Features
* **Tokenization:** Identifies Keywords, Numbers, Identifiers, Operators, and Symbols.
* **Error Handling:** Detects invalid characters that don't match any rules.
* **Whitespace Management:** Automatically skips spaces and tabs.

## 🛠️ Token Specifications
The lexer recognizes the following categories:
| Token Type  | Examples |
| ------------- | ------------- |
| **Keywords** | `int`, `if`, `else`, `while`, `return` |
| **Identifiers**| `x`, `y`, `my_var` |
| **Numbers** | `10`, `500` |
| **Operators** | `+`, `-`, `*`, `/`, `=` |
| **Symbols** | `;`, `(`, `)` |

## 💻 How to Run

### Option 1: Using GitHub Codespaces (Recommended)
1. Click the green **Code** button in this repo.
2. Select the **Codespaces** tab and click **Create codespace on main**.
3. Once the terminal opens at the bottom, type:
   ```bash
   python lexer.py
