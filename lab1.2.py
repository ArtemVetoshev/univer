import random
import matplotlib.pyplot as plt

M = 500
N = 11
p = 0.005
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
    collision = 0
    _sum = 0
    probability_l.append(p)
    for f_slot in range(M):
        messages_sum = send_messages(p)
        # если отправили два сообщения одновременно
        if messages_sum > 1:
            # случится коллизия
            collision += messages_sum
        _sum += messages_sum
    avg_T.append(collision / _sum)
    p += 0.01

plt.xlabel("probability")
plt.ylabel("packet_loss_probability")
plt.plot(probability_l, avg_T)
plt.show()
