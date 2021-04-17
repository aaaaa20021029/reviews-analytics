data = []
count = 0
with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)
		count += 1
		if count % 1000 == 0: #求餘數
			print(len(data))
print('檔案讀取完了,總共有', len(data), '則留言') 

sum_len = 0
for d in data:
	sum_len += len(d)

print('平均的留言長度為', sum_len/len(data))


new = []
for d in data:
	if len(d) < 100:
		new.append(d)
print('總共有', len(new), '比留言長度小於100字')
print('第一則留言 :', new[0])
print('第二則留言 :', new[1])