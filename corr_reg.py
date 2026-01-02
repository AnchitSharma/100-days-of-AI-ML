import math

Physics_Scores = list(map(int,'15  12  8   8   7   7   7   6   5   3'.split()))
History_Scores = list(map(int,'10  25  17  11  13  17  20  13  9   15'.split()))

Physics_Scores_mean = sum(Physics_Scores)/len(Physics_Scores)
History_Scores_mean = sum(History_Scores)/len(History_Scores)

lst = [(Physics_Scores[i]-Physics_Scores_mean)*(History_Scores[i]-History_Scores_mean) for i in range(len(Physics_Scores))]
lst1 = [(i-Physics_Scores_mean)**2 for i in Physics_Scores]
lst2 = [(h-History_Scores_mean)**2 for h in History_Scores]

r = sum(lst)/math.sqrt(sum(lst1)+sum(lst2))
b = sum([(Physics_Scores[i]-Physics_Scores_mean)*(History_Scores[i]-History_Scores_mean) for i in range(len(Physics_Scores))])/(sum([(i-Physics_Scores_mean)**2 for i in Physics_Scores]))
a = History_Scores_mean-b*Physics_Scores_mean
y = a+b*10
print(round(y,1))