n = int(input())
score = list(map(int, input().split()))
maxScore = 0
newScoreArr = []

for i in range(n):
    maxScore = max(score)
    newScore = score[i] / maxScore * 100
    newScoreArr.append(newScore)

sumScore = sum(newScoreArr)
print(sumScore / len(newScoreArr))
