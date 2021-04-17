#讀取亞馬遜的一百萬筆留言

data = []
count = 0
with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)
		count += 1
		if count % 1000 == 0: #求餘數
			print(len(data))
print('檔案讀取完了,總共有', len(data), '則留言') 

#計算平均留言長度
sum_len = 0
for d in data:
	sum_len += len(d)

print('平均的留言長度為', sum_len/len(data))

#計算少於100字的留言數量
new = []
for d in data:
	if len(d) < 100:
		new.append(d)
print('總共有', len(new), '筆留言長度小於100字')
print(new[0])
print(new[1])

#計算提到"good"的留言數量
good = []
for d in data:
	if 'good' in d:
		good.append(d)
print('一共有', len(good), '筆留言提到"good"')
print(good[0])