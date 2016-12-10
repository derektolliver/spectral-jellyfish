import sys

n,m = input().strip().split(' ')
n,m = [int(n),int(m)]
topic = []
for topic_i in range(n):
   topic_t = str(input().strip())
   topic.append(topic_t)

max_topics = 0
groups = 0
for t1 in range(len(topic) - 1):
    for t2 in range(t1 + 1, len(topic)):
        p1 = int(topic[t1], 2)
        p2 = int(topic[t2], 2)
        res = bin(p1 | p2).count("1")
        if res > max_topics:
            max_topics = res
            groups = 1
        elif res == max_topics:
            groups += 1

print(max_topics)
print(groups)
