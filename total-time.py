import json

# Request spotify data
# Once you have your data, open it and grab all files that follow the `StreamingHistory*.json` scheme to ./history
# Then change the historyFileNumber variable depending on how many history files you have

historyFileNumber = 3

totalMs = 0

for i in range(historyFileNumber):
  data = json.load(open(f'history/StreamingHistory{i}.json', 'r', encoding="utf8"))
  for i in data:
    totalMs += i['msPlayed']

seconds = (totalMs/1000)%60
seconds = int(seconds)
minutes = (totalMs/(1000*60))%60
minutes = int(minutes)
hours = (totalMs/(1000*60*60))%24
hours = int(hours)
days = (totalMs/(1000*60*60*24))
days = int(days)

print()
print(f'Your total listening time over the past year in miliseconds is: {totalMs}')
print()
print(f'days: {days}')
print(f'hours: {hours}')
print(f'minutes: {minutes}')
print(f'seconds: {seconds}')
print()
print(f'{days} days, {hours} hours, {minutes} minutes, and {seconds} seconds ({days}:{hours}:{minutes}:{seconds})')