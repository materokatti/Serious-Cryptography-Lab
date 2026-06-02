"""
Caesar Cipher (Shift Cipher) implementation in Python.

Features:
- Encrypt / decrypt with a given shift (can be negative or > 26)
- Keeps case (A-Z, a-z) and leaves non-alphabet characters unchanged
- Simple CLI:
  python caesar_cipher.py --mode encrypt --shift 3 --text "ABC"
  echo "ABC" | python caesar_cipher.py --mode encrypt --shift 3
"""

from __future__ import annotations

import argparse
import sys
from typing import Literal


def _shift_char(ch: str, shift: int) -> str:
    """Shift a single ASCII letter, preserving its case."""
    if "a" <= ch <= "z":
        base = ord("a")
        return chr(((ord(ch) - base + shift) % 26) + base)
    if "A" <= ch <= "Z":
        base = ord("A")
        return chr(((ord(ch) - base + shift) % 26) + base)
    return ch


def caesar_cipher(text: str, shift: int) -> str:
    """
    Apply Caesar Cipher shift to `text`.

    Notes:
    - `shift` is normalized with modulo 26.
    - Non-alphabet characters are not changed.
    """
    shift_norm = shift % 26
    return "".join(_shift_char(ch, shift_norm) for ch in text)


def encrypt(text: str, shift: int) -> str:
    """Encrypt by shifting forward."""
    return caesar_cipher(text, shift)


def decrypt(text: str, shift: int) -> str:
    """Decrypt by shifting backward."""
    return caesar_cipher(text, -shift)


def _read_text(args: argparse.Namespace) -> str:
    if args.text is not None:
        return args.text
    # If no --text is provided, read from stdin (allows piping).
    return sys.stdin.read()


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Caesar Cipher (shift cipher)")
    parser.add_argument(
        "--mode",
        choices=["encrypt", "decrypt"],
        required=True,
        help="Whether to encrypt or decrypt",
    )
    parser.add_argument("--shift", type=int, required=True, help="Shift amount")
    parser.add_argument(
        "--text",
        type=str,
        default=None,
        help="Input text (if omitted, reads from stdin)",
    )
    args = parser.parse_args(argv)

    text = _read_text(args)
    if args.mode == "encrypt":
        out = encrypt(text, args.shift)
    else:
        out = decrypt(text, args.shift)
    sys.stdout.write(out)
    if out and not out.endswith("\n"):
        sys.stdout.write("\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

