import heapq


class minWater(object):  # 直接贪心算法就可以了
    def xiaolaji(self, startwater, stations):

        q = []
        res = pre = 0
        tank = startwater
        for loction, water in stations:
            tank -= loction - pre
            while tank < 0:
                if not q:
                    return -1
                tank += -heapq.heappop(q)
                res += 1
            heapq.heappush(q, -water)
            pre = loction
        return res


d, w = map(int, input().split())
l1 = list(map(int, input().split()))
l2 = list(map(int, input().split()))


station = []
for i in range(len(l1)):
    station.append([l1[i], l2[i]])
station.append([d, 0])

laji = minWater()
print(laji.xiaolaji(w, station))

