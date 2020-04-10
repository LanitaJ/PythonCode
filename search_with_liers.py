from sys import stdout

stdout.write("x < %d?\n" % 1)
ans = int(input())
lier = 0
if ans == 1:
	lier = 1
b = 100001
a = 1
mid = a +(b - a)//2
while (b - a > 1):
	stdout.write("x < %d?\n" % mid)
	ans = int(input())
	if ans + lier == 1:
		b = mid
	else:
		a = mid
	mid = a + (b - a)//2
stdout.write("Я угадал! %d" % mid)
stdout.flush()