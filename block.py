import json
import os
import hashlib

blockchaindir = os.curdir + '/blockchain/'

def get_hash(filename):
    f = open(blockchaindir + filename, 'rb').read()
    return hashlib.md5(f).hexdigest()

def get_files():
    files = os.listdir(blockchaindir)
    return sorted([int(i) for i in files])


def check_integrity():
    files = get_files()
    results = []

    for file in files[1:]:
        f = open(blockchaindir + str(file))
        h = json.load(f)['hash']
        prev_file = str(file - 1)
        actual_hash = get_hash(prev_file)

        if h == actual_hash:
            res = 'Ok'
        else:
            res = 'Corrapted'
        # print('Block {} is : {}'.format(prev_file, res))
        results.append({'Block':prev_file, 'result':res})
    return results


def writeblock(name, amount, to_whom, prev_hash=''):
    files = get_files()
    prev_file = files[-1]
    filename = str(prev_file + 1)
    prev_hash = get_hash(str(prev_file))

    data = {
        'name': name,
        'amount': amount,
        'to_whom': to_whom,
        'hash': prev_hash
    }
    with open(blockchaindir + filename, 'w') as file:
        json.dump(data, file)


def main():
    print(check_integrity())


if __name__ == '__main__':
     main()






# def check_integrity_my(block1, block2):
#     hash_new = get_hash(block1)
#     print(hash_new)
#     # next_filename = filename + '1'
#     # print(next_filename)
#     with open(blockchaindir + block2, 'r') as f:
#         data = json.load(f)
#     print(data)
#     hash_old = data['hash']
#     if hash_new == hash_old:
#         print('Ok')
#     else:
#         print('This block was changed')
