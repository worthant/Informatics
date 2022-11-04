import re

# myISU = 368090
# myvar = 222
test_test = input()
smile = 'X-{O'
test1 = smile * 6 + '---' + smile + 'XXXX' + 'X-{0' + smile
test2 = 'X--{O' + smile + 'Х--{O' + smile * 2
test3 = smile + 'X' + smile + 'JKRS' + smile
test4 = 'X_{O' + smile * 4
test5 = 'X-{o' + smile + 'hr' + smile
tests = [test1, test2, test3, test4, test5, test_test]

for test in tests:
    print(len(re.findall(smile, test)))

