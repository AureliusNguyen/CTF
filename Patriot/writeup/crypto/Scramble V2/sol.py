import random as r

base = [[(n,k) for k in range(210)] for n in range(11)]
del base[-1][-1]

key = "20240823084532"
r.seed(int(key))

r.shuffle(base)
for l in base:
  r.shuffle(l)

flat = sum(base, start=[])

image = []
work = []
for x in flat:
  work.append(x)
  n, k = x
  if k == 209:
    image.append(work)
    work = []

image.append(work)

base = [[(n,k) for k in range(210)] for n in range(11)]
del base[-1][-1]
flat = sum(base, start=[])

f = open("encryptedFlag.txt")
lines = f.readlines()

dec = {(n,209): '\n' for n in range(10)}
for l, xs in zip(lines, image):
  if len(l) != len(xs):
    continue
  for c, x in zip(l, xs):
    dec[x] = c

dec = {k: ' ' if v == '%' else v for k, v in dec.items()}
res = "".join(dec.get(x,'.') for x in flat)
print(res)