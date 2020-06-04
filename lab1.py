import random
import matplotlib.pyplot as plt

M = 10000
N = 11
p = 0
probability_l = []
avg_T = []


def send_messages(pp):
    i = 0
    messages_sum = 0
    while i <= N:
        if random.choices([1, 0], [pp, 1 - pp])[0] == 1:
            messages_sum += 1
        i += 1
    return messages_sum


while p <= (1/N):
    sum_of_sum_messages = []
    awaiting = []
    probability_l.append(p)
    for f_slot in range(M):
        messages_sum = send_messages(p)
        if not awaiting:
            awaiting.append(0)
        elif awaiting[f_slot - 1] <= 0:
            awaiting.append(messages_sum)
        else:
            awaiting.append((awaiting[f_slot - 1] - 1 + messages_sum))
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
