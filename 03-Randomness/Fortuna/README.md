# 02. Fortuna CSPRNG Simulation

A concise implementation of the Fortuna CSPRNG (Cryptographically Secure Pseudo-Random Number Generator) for security study purposes.

## 🔑 Key Features
* ***Entropy Collection***: Simulates gathering system noise.
* ***Reseed Mechanism***: Updates internal state for unpredictability.
* ***CSPRNG***: Generates 128-bit secure random data.

## 🚀 Quick Start
### 1. Setup Environment
```bash
python3 -m venv venv
source venv/bin/activate
pip install pycryptodome
```

### 2. Run Demo
```bash
python3 fortuna_demo.py
```
## 📝 Usage Note
This demo utilizes pycryptodome's secure interface to mimic Fortuna's behavior:

1. Gather raw entropy via system noise/timestamps.

2. Hash the entropy using SHA-256.

3. Generate secure bytes for cryptographic use.