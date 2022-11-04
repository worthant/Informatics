import re

test1 = 'ВТ ВТ ВТ ВТ ВТ ИТМО ВТ ИТМО ИТМО ИТМО ВТ ВТ ВТ ИТМО ИТМО ИТМО ВТ ИТМО ИТМО'
test2 = 'ВТ      думать                понимать ИТОО ИООО ВТВТВТ ИТМОИТМОИТМО ВТ думать ИТМО'
test3 = 'ВТ         ИТВТ ИТВТ ИТМО'
test4 = 'ВТ -       -   -ИТМО'
test5 = 'ВТ ИТМО'
tests = [test1, test2, test3, test4, test5]
patterns = [re.compile(r'ВТ\s+ИТМО'), re.compile(r'ВТ\s+\w+\s+ИТМО'), re.compile(r'ВТ\s+\w+\s+\w+\s+ИТМО'),
            re.compile(r'ВТ\s+\w+\s+\w+\s+\w+\s+ИТМО'), re.compile(r'ВТ\s+\w+\s+\w+\s+\w+\s+\w+\s+ИТМО')]

for i, test in enumerate(tests, start=1):
    print("test{}:".format(i))
    if len(test.split()) < 6:
        ans_ = []
        for pattern in patterns:
            ans_ += re.findall(pattern, test)
        if ans_:
            for i, x in enumerate(ans_, start=1):
                print('{}) {}'.format(i, x))
        else:
            print('This test is incorrect')
    else:
        ans = set()
        test_ = test.split()
        for x in range(6, len(test_) + 1):
            search = test_[x - 6:x]
            for pattern in patterns:
                m = re.findall(pattern, ' '.join(search))
                if m:
                    for item in m:
                        ans.add(item)
        if ans:
            for i, x in enumerate(list(ans), start=1):
                print('{}) {}'.format(i, x))
        else:
            print('This test is incorrect')
    print('-' * 50)
