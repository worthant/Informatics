import time

schedule = open('Schedule.xml', 'r', encoding="utf-8")
timetable = open('timetable.json', 'w', encoding="utf-8")

start_time = time.perf_counter()
tab_counter = 1
timetable.write('{\n')
x = schedule.readlines()
schedule.close()

for i in range(len(x)):
    tag = x[i].strip().replace('<', '>').split('>')[1:-1]
    if i == len(x) - 1 or x[i + 1].strip()[:2] == '</':
        q = ''
    else:
        q = ','  # comma if quotes aren't closing
    if len(tag) > 2:
        tag.pop()  # remove closing tag
    if len(tag) == 1:
        if tag[0][0] == '/':  # if it is closing tag
            timetable.write('\t' * tab_counter + '}' + q + '\n')  # close, then <=> }, or }
            tab_counter -= 1  # we collapsed => move 1 tab left
        else:
            timetable.write('\t' * tab_counter + '"' + tag[0] + '": {\n')  # open, then <=> "object": {
            tab_counter += 1  # we expanded => move 1 tab right
    else:
        timetable.write('\t' * tab_counter + '"' + tag[0] + '" : "' + tag[1] + '" ' + q + '\n')

timetable.write('}\n')
timetable.close()
print(time.perf_counter() - start_time)
