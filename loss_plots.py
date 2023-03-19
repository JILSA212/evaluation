import matplotlib.pyplot as plt

t5_small_loss_steps = range(500, 11000, 500)
print(t5_small_loss_steps)
t5_small_loss_values = [2.104200, 0.652900, 0.327600, 0.184700, 0.115800, 0.082900, 0.066000, 0.052300, 0.042600, 0.039800, 0.033400, 0.031100, 0.030100, 0.028200, 0.026400, 0.019300, 0.016200, 0.013300, 0.011600, 0.011400, 0.010300]

f1 = plt.figure()
plt.plot(t5_small_loss_steps, t5_small_loss_values)
plt.title("T5 Small Loss")
plt.xlabel("Steps")
plt.ylabel("Loss")
plt.savefig("data/plots/t5_small_loss.png")
plt.close(f1)