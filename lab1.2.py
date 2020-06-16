import random
import matplotlib.pyplot as plt

M = 500
N = 11
p = 0.005
probability_l = []
loss = []


def send_messages(pp):
    i = 0
    messages = []
    while i <= N:
        if random.random() <= pp:
            messages.append(1)
        else:
            messages.append(0)
        i += 1
    messages_sum = sum(messages)
    return messages_sum


while p <= (1/N):
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
    loss.append(collision / _sum)
    p += 0.01

plt.xlabel("probability")
plt.ylabel("packet_loss_probability")
plt.plot(probability_l, loss)
plt.show()
