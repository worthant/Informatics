import time

schedule = open('Schedule.xml', 'r', encoding="utf-8")
timetable = open('timetable.md', 'w', encoding="utf-8")

start_time = time.perf_counter()
tab_counter = 0
grid_counter = 2
x = schedule.readlines()
schedule.close()

for i in range(len(x)):
    tag = x[i].strip().replace('<', '>').split('>')[1:-1]
    if len(tag) > 2:
        tag.pop()  # remove closing tag
    if len(tag) == 1:
        if tag[0][0] == '/':  # if it is closing tag
            tab_counter = 0  # we collapsed => move 1 tab left
            grid_counter -= 1
        else:
            timetable.write('#' * grid_counter + ' ' + tag[0] + ':\n')  # open, then <=> "object": {
            tab_counter = 1  # we expanded => move 1 tab right
            grid_counter += 1
    else:
        if grid_counter == 3:
            timetable.write('> ' + tag[0] + ':' + tag[1] + '\n')
        else:
            timetable.write('\t' * tab_counter + tag[0] + ':' + tag[1] + '\n')

timetable.close()
print(time.perf_counter() - start_time)
