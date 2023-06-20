import csv
def updatehypothesis(x, h):
    if h == []:
        return x
    for i in range( 0, len(h)-1):
        if x[i].upper() != h[i].upper():
            h[i] == "?"
    return h

data = []
h = []
with open ('database.csv', 'r') as file:
    reader =csv.reader(file)
    print("Data:")
    for row in reader:
        data.append(row)
        print(row)
    if data:
        data=data[1::]
        for x in data:
            if x[-1].upper() == "YES":x.pop()
            h=updatehypothesis(x,h)
print("Hypothesis:", h)



output:
  PS C:\Users\user\Desktop> & C:/Python34/python.exe c:/Users/user/Desktop/find_s.py
Data:
['sky', 'humidity', 'air', 'wind', 'water', 'forecast', 'emjoy sports?']
['sunny', 'normal', 'warm', 'strong', 'warm', 'same', 'yes']
['sunny', 'high', 'warm', 'strong', 'warm', 'same', 'yes']
['rainy', 'high', 'cold', 'strong', 'warm', 'change', 'no']
['sunny', 'high', 'warm', 'strong', 'cool', 'change', 'yes']
Hypothesis: ['sunny', 'normal', 'warm', 'strong', 'warm', 'same']
