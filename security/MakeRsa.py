from cryptography.hazmat.primitives.asymmetric import padding #, rsa
from cryptography.hazmat.primitives import serialization, hashes
# from cryptography.hazmat.primitives import padding as sym_padding
# from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
import os
import argparse


# 加载公钥和私钥
def load_keys(public_key_path, private_key_path):
    with open(public_key_path, "rb") as f:
        public_key = serialization.load_pem_public_key(f.read())

    with open(private_key_path, "rb") as f:
        private_key = serialization.load_pem_private_key(f.read(), password=None)

    return public_key, private_key


# 加密文本内容
def encrypt_text(public_key, plaintext):
    # RSA加密只能加密较短的内容，因此需要分块加密
    max_length = public_key.key_size // 8 - 2 * hashes.SHA256().digest_size - 2
    plaintext = plaintext.encode()
    encrypted_text = b""

    for i in range(0, len(plaintext), max_length):
        chunk = plaintext[i:i + max_length]
        encrypted_chunk = public_key.encrypt(
            chunk,
            padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None
            )
        )
        encrypted_text += encrypted_chunk

    return encrypted_text


# 解密文本内容
def decrypt_text(private_key, encrypted_text):
    # RSA解密
    max_length = private_key.key_size // 8
    decrypted_text = b""

    for i in range(0, len(encrypted_text), max_length):
        chunk = encrypted_text[i:i + max_length]
        decrypted_chunk = private_key.decrypt(
            chunk,
            padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None
            )
        )
        decrypted_text += decrypted_chunk

    return decrypted_text.decode()

def parse_args():
    # 创建 ArgumentParser 对象
    parser = argparse.ArgumentParser(description="命令行参数")

    # 添加参数
    parser.add_argument("--file", type=str, default='Test.txt', help="源文件")
    parser.add_argument("--pkey", type=str, default='Temple.pkey', help="公钥")
    parser.add_argument("--skey", type=str, default='Temple.skey', help="私钥")
    #parser.add_argument("--name", type=str, required=True, help="你的名字")
    #parser.add_argument("--age", type=int, default=18, help="你的年龄")
    #parser.add_argument("--verbose", action="store_true", help="是否启用详细模式")

    # 解析命令行参数
    return parser.parse_args()


# 主程序
if __name__ == "__main__":
    args = parse_args()

    # 加载密钥
    public_key, private_key = load_keys(args.pkey, args.skey)

    # 读取要加密的文本文件
    with open(args.file, "r", encoding="utf-8") as f:
        plaintext = f.read()

    print("原文本内容：")
    print(plaintext)

    # 加密文本
    encrypted_text = encrypt_text(public_key, plaintext)
    print("\n加密后的文本（二进制）：")
    print(encrypted_text)

    # 解密文本
    decrypted_text = decrypt_text(private_key, encrypted_text)
    print("\n解密后的文本：")
    print(decrypted_text)