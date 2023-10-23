from random import *
from statistics import *
import matplotlib.pyplot as plt

N = 100
R = 0.1
adj = [[] for i in range(N)]
s = [[i] for i in range(N)]
par = [i for i in range(N)]


def find(a):
	if par[a] != a:
		par[a] = find(par[a])
	return par[a]


def join(a, b):
	if len(s[a]) >= len(s[b]):
		s[a] = s[a] + s[b]
		s[b] = []
		par[b] = a
	else:
		s[b] = s[a] + s[b]
		s[a] = []
		par[a] = b


def run(sd):
	x = []
	y = []
	global adj, s, par
	adj = [[] for i in range(N)]
	s = [[i] for i in range(N)]
	par = [i for i in range(N)]
	seed(sd)
	for i in range(N):
		x.append(random())
		y.append(random())

	for i in range(N):
		for j in range(i+1, N):
			if (((x[j] - x[i])**2 + (y[j] - y[i])**2) ** 0.5) < R:
				adj[i].append(j)
				adj[j].append(i)

	for i in range(N):
		for j in adj[i]:
			a = find(i)
			b = find(j)
			if a != b:
				join(a, b)
	max_set = 0
	adj_lens = len(adj[0])
	for i in range(N):
		if len(s[i]) > max_set:
			max_set = len(s[i])
	return [adj_lens, max_set]
	#print(s)


sets = []
adjs = []
for i in range(3000):
	tmp = run(int(random()*10) + i)
	sets.append(tmp[1])
	adjs.append(tmp[0])

print("Mean of maximum set size: ", mean(sets))
print("Variance of maximum set size: ", variance(sets))
print("Mean of number of neighbors of vertex 0: ", mean(adjs))
print("Variance of number of neighbors of vertex 0: ", variance(adjs))

plt.figure(1)
nSet, binsSet, patchesSet = plt.hist(sets, 30, density=1, facecolor='g', alpha=1)
plt.savefig("1.png")

plt.figure(2)
nAdj, binsAdj, patchesAdj = plt.hist(adjs, 30, density=1, facecolor='g', alpha=1)
plt.savefig("2.png")
