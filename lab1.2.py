import random
import matplotlib.pyplot as plt

M = 500
N = 11
p = 0.005
probability_l = []
loss = []

def send_messages(pp):
    messages = []
    for i in range(N):
        m = random.choices([1, 0], [pp, 1 - pp])
        messages.append(m[0])
    return sum(messages)

while p <= (1/N):
    collision = 0
    _sum = 0
    probability_l.append(p)
    for frame in range(M):
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