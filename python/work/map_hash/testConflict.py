print(hash('12234twrtrwetwertwervsdfvdfvs肺癌无法权威而无法全微分'))


def BKDRHash(inputStr):
    seed = 131 # 31 131 1313 13131 131313 etc..
    result = 0
    for c in inputStr:
        result = (result * seed + ord(c)) % 4294967295
    return result & 0x7FFFFFFF

'''
print(312354134543534558438572345)
print(type(312354134543534558438572345))
print(ord('.'))
'''

def test_conflict():
    count = 0;
    result_set = set();
    with open("resourcelist.txt", "r", encoding='utf-8') as file:
        for line in file.readlines():
            file_name = line.strip('\n')
            count = count + 1
            result_set.add(BKDRHash(file_name))
    print("result line = {0}".format(count))
    print("hash value count = {0}".format(len(result_set)))


if __name__ == '__main__':
    test_conflict()

print(BKDRHash('5h2lj345hk2j43h;of4u5tj4k5;'))