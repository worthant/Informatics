import re

test_test = input()
test1 = 'idknoo@sldkfj.com.....'
test2 = 'adagio_sostenuto@sldkfjc'
test3 = 'videoswatch@something.'
test4 = 'growbro@asd;flkj;slkd;jf[].lol'
test5 = 'normal_email@site.com'
test_base0 = 'students.spam@yandex.ru'
test_base1 = 'example@example'
test_base2 = 'example@example.com'
tests = [test1, test2, test3, test4, test5, test_base0, test_base1, test_base2, test_test]

for test in tests:
    if test.count("@") == 1:
        address, server = test.split('@')
        print(server if re.findall(r'^\w+\.\w+$', server) and re.findall(r'\w+(([.,_])|(\w+))+$', address) else 'Fail!')
    elif test.count("@") == 0:
        print("Zero @ symbols")
    else:
        print("Too many @ symbols")