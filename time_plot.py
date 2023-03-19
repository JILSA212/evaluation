import matplotlib.pyplot as plt

model_names = ["t5_small_500_epochs", "t5_small_1000_epochs", "t5_small_1500_epochs", "facebook_bart_200_epochs"]
x_values = [20, 40, 60, 80]
y_values = [216, 405, 580, 634]

plt.bar(x_values, y_values, tick_label = model_names, width = 10, color = ['blue'])
plt.xlabel('Model Names')
plt.ylabel('Time taken (in minutes)')
plt.xticks(rotation=10)
plt.title('Time taken by different models to train')
plt.savefig("data/plots/time_plot.png")