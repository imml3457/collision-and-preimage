import random
import string
import hashlib
import json
#getting a random string of 100 characters
def get_random_string(length):
    letters = string.ascii_lowercase
    result_string = ''.join(random.choice(letters) for i in range(length))
    return result_string

#truncate the bits given number of bits desired
def truncate(val, numbits):
    return val & (2**numbits - 1)

#initial digest
def ininum(numbits):
    m = hashlib.sha1()
    m.update(get_random_string(100))
    d = m.hexdigest()
    sus = int(d, 16)
    bigsus = truncate(sus, numbits)
    return bigsus

#collision testing
def collision(numbits, d):
    i = 2
    flag = False

    while(flag is False):
        x = hashlib.sha1()
        x.update(get_random_string(100))
        t = x.hexdigest()
        sus1 = int(t, 16)
        temp = truncate(sus1, numbits)
        if(temp not in d.values()):
            d[i] = temp
            i += 1
        else:
            flag = True
    return i

#preimage testing
def preimage(numbits, val1):
    i = 2
    flag = False

    while(flag is False):
        x = hashlib.sha1()
        x.update(get_random_string(100))
        t = x.hexdigest()
        sus1 = int(t, 16)
        temp = truncate(sus1, numbits)
        if(temp == val1):
            flag = True
        else:
            i += 1
    return i   

cdict = {}
pdict = {}
#running it 50 times
for i in range(1, 51):
    vals = {}
    temp = ininum(8)
    vals[1] = temp
    cdict[i] = collision(8, vals)
    pdict[i] = preimage(8, temp)

#json dumps

with open('collision8.json', "w") as outfile:
    json.dump(cdict, outfile)

with open('preimage8.json', "w") as outfile:
    json.dump(pdict, outfile)