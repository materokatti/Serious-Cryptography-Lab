# Caesar Cipher (Shift Cipher)

`caesar_cipher.py` is a simple Python implementation of the **Caesar Cipher (Shift Cipher)**.
It encrypts and decrypts text by shifting letters by a given amount (`shift`).

## File Structure

- `caesar_cipher.py`
  - `encrypt(text, shift)`: shifts letters **forward** by `shift` to encrypt
  - `decrypt(text, shift)`: shifts letters **backward** by `shift` to decrypt
  - `caesar_cipher(text, shift)`: shared core logic that transforms the text
  - `_shift_char(ch, shift)`: helper that shifts a single character while preserving case
  - `main()`: CLI entry point (parses arguments and prints the result)
- `test_caesar_cipher.py`
  - `unittest`-based tests covering representative cases

## How It Works (Key Points)

- `shift` can be **negative** and can be larger than `26`.
  - The implementation normalizes it with `shift % 26`.
- Uppercase (`A-Z`) and lowercase (`a-z`) **case is preserved**.
  - Example: `A` encrypts to `D` (still uppercase).
  - Example: `a` encrypts to `d` (still lowercase).
- Non-alphabet characters (spaces, commas, exclamation marks, etc.) are **left unchanged**.

## Usage (CLI)

### 1) Pass text directly with `--text`

```sh
python3 caesar_cipher.py --mode encrypt --shift 3 --text "ABC"
```

Decrypt:

```sh
python3 caesar_cipher.py --mode decrypt --shift 3 --text "DEF"
```

### 2) Use stdin (pipe input)

```sh
echo "Hello, World!" | python3 caesar_cipher.py --mode encrypt --shift 3
```

## Use from Python (Import)

```python
from caesar_cipher import encrypt, decrypt

cipher = encrypt("ABC", 3)   # "DEF"
plain = decrypt(cipher, 3)   # "ABC"
```

## Examples

- `encrypt("Hello, World!", 3)` -> `Khoor, Zruog!`
- `decrypt("Khoor, Zruog!", 3)` -> `Hello, World!`

