import random
import string

def pd_general_szamokkal(hossz=12):

    return ''.join(random.choices(string.digits, k=hossz))

def pd_general_karakterekkel(hossz=12):

    karakters = string.ascii_letters
    return ''.join(random.choices(karakters, k=hossz))

def pd_general_komplex(hossz=12):

    spec_karakterek = string.punctuation
    karakterek = string.ascii_letters + string.digits + spec_karakterek
    return ''.join(random.choices(karakterek, k=hossz))
