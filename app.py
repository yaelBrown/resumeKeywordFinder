from tabulate import tabulate
import os

desc = []
wordCount = dict()

def checkWords(s):
  _ = s.split(" ")
  for w in _:
    w.replace(".", "").replace(",", "").strip().lower()
    if w not in wordCount.keys():
      wordCount[w] = 1
    else: 
      wordCount[w] += 1

def printWordCount():
  table = []
  wCL = list(wordCount.items())
  tempL = list()
  cnt = 0
  for i in wCL:
    tempL.append((i[1], cnt))
    cnt += 1
  tempL = sorted(tempL)
  sortedWC = list()
  idx = len(wCL) - 1
  while not idx < 0:
    j = tempL[idx]
    sortedWC.append(wCL[j[1]]) 
    idx -= 1
  for i in sortedWC:
    if i[1] == 1:
      continue
    row = [i[0], i[1]]
    table.append(row)
  print(tabulate(table))

def populateWordCount(): 
  for ws in desc: 
    checkWords(ws)

def populateDesc():
  with os.scandir('jobs/') as entries: 
    for entry in entries:
      path = "jobs/" + entry.name
      with open(path, 'r') as f:
        desc.append(f.read())

def main():
  populateDesc()
  populateWordCount()
  printWordCount()


if __name__ == "__main__":
    main()

