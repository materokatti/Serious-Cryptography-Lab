#!/bin/zsh
openssl genrsa 4096 > private.pem

# Encrypt the private key with a symmetric key
openssl genrsa -aes128 4096 > key.bin