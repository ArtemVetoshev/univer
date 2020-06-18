import random
import matplotlib.pyplot as plt

M = 10000
N = 11
p = 0
probability_l = []
avg_T = []

def send_messages(pp):
    messages = []
    for i in range(N):
        m = random.choices([1, 0], [pp, 1 - pp])
        messages.append(m[0])
    return sum(messages)

while p <= (1/N):
    awaiting = []
    probability_l.append(p)
    for frame in range(M):
        messages_sum = send_messages(p)
        if not awaiting:
            awaiting.append(0)
        elif awaiting[frame - 1] <= 0:
            awaiting.append(messages_sum)
        else:
            awaiting.append((awaiting[frame - 1] - 1 + messages_sum))
    awaiting_sum = sum(awaiting)
    if not avg_T:
        avg_T.append(0)
    else:
        avg_T.append(awaiting_sum / p)
    p += 0.01

plt.xlabel("probability")
plt.ylabel("avg_time")
plt.plot(probability_l, avg_T)
plt.show()