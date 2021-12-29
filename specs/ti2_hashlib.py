#%% [markdown]
# # hashlibの速度比較
# pythonのhashlibで生成できるhashの生成速度を比較
#%%
import hashlib
from timeit2 import ti2


def to_md5(s: str, count: int):
    for i in range(count):
        s = hashlib.md5(s.encode()).hexdigest()
    return s


def to_sha1(s: str, count: int):
    for i in range(count):
        s = hashlib.sha1(s.encode()).hexdigest()
    return s


def to_sha256(s: str, count: int):
    for i in range(count):
        s = hashlib.sha256(s.encode()).hexdigest()
    return s


def to_sha512(s: str, count: int):
    for i in range(count):
        s = hashlib.sha512(s.encode()).hexdigest()
    return s


def to_blake2b(s: str, count: int):
    for i in range(count):
        s = hashlib.blake2b(s.encode()).hexdigest()
    return s


def to_blake2s(s: str, count: int):
    for i in range(count):
        s = hashlib.blake2s(s.encode()).hexdigest()
    return s


#%% 40万文字の文字列を1回施行
s = "test" * 1000000
res = ti2(
    to_md5,
    to_sha1,
    to_sha256,
    to_sha512,
    to_blake2s,
    to_blake2b,
    args=[s, 1],
    relative=True,
)

# to_md5:
# 	0.006623 sec
# to_sha1:
# 	0.004902 sec
# to_sha256:
# 	0.010097 sec
# to_sha512:
# 	0.006934 sec
# to_blake2s:
# 	0.008271 sec
# to_blake2b:
# 	0.005663 sec
# relative:
# 	to_sha1:
# 		1
# 	to_blake2b:
# 		1.16
# 	to_md5:
# 		1.35
# 	to_sha512:
# 		1.41
# 	to_blake2s:
# 		1.69
# 	to_sha256:
# 		2.06
# %% 10文字の文字列を10000回施行
s = "password10"
res = ti2(
    to_md5,
    to_sha1,
    to_sha256,
    to_sha512,
    to_blake2s,
    to_blake2b,
    args=[s, 10000],
    relative=True,
)
# to_md5:
# 	0.010791 sec
# to_sha1:
# 	0.010968 sec
# to_sha256:
# 	0.014155 sec
# to_sha512:
# 	0.016704 sec
# to_blake2s:
# 	0.005646 sec
# to_blake2b:
# 	0.006353 sec
# relative:
# 	to_blake2s:
# 		1
# 	to_blake2b:
# 		1.13
# 	to_md5:
# 		1.91
# 	to_sha1:
# 		1.94
# 	to_sha256:
# 		2.51
# 	to_sha512:
# 		2.96
# %% 返り値の比較
s = "test"
print("md5    : ", to_md5(s, 1))
print("sha1   : ", to_sha1(s, 1))
print("sha256 : ", to_sha256(s, 1))
print("blake2s: ", to_blake2s(s, 1))
print("sha512 : ", to_sha512(s, 1))
print("blake2b: ", to_blake2b(s, 1))
# md5    :  098f6bcd4621d373cade4e832627b4f6
# sha1   :  a94a8fe5ccb19ba61c4c0873d391e987982fbbd3
# sha256 :  9f86d081884c7d659a2feaa0c55ad015a3bf4f1b2b0b822cd15d6c15b0f00a08
# blake2s:  f308fc02ce9172ad02a7d75800ecfc027109bc67987ea32aba9b8dcc7b10150e
# sha512 :  ee26b0dd4af7e749aa1a8ee3c10ae9923f618980772e473f8819a5d4940e0db27ac185f8a0e1d5f84f88bc887fd67b143732c304cc5fa9ad8e6f57f50028a8ff
# blake2b:  a71079d42853dea26e453004338670a53814b78137ffbed07603a41d76a483aa9bc33b582f77d30a65e6f29a896c0411f38312e1d66e0bf16386c86a89bea572