import numpy as np
import matplotlib.pyplot as plt
import statistics as stat

dest_folder = "/Users/msavasci/Desktop/Courses/Spring23/COMPSCI621/Project_Final_Report/"

# set height of bar (Wall)
randoop = [95.07]
evosuite = [97.87]
tackletest = [98.53]
 
font_size = 22.0
n_groups = 1

# create plot
fig, ax = plt.subplots(figsize=(9,6))
index = np.arange(n_groups)
bar_width = 0.1
opacity = 0.5

# rects1 = plt.bar(index, baselineOne, bar_width,
# alpha=opacity,
# color='dodgerblue',
# label='Baseline: 58W',
# hatch='XXX',
# edgecolor = "black")

rects1 = plt.bar(index, randoop, bar_width,
alpha=opacity,
color='red',
label='Randoop',
hatch='***',
edgecolor = "black")

rects2 = plt.bar(index + bar_width, evosuite, bar_width,
alpha=opacity,
color='green',
label='Evosuite',
hatch='///',
edgecolor = "black")

rects3 = plt.bar(index + 2 * bar_width, tackletest, bar_width,
alpha=opacity,
color='blue',
label='TackleTest',
hatch='+++',
edgecolor = "black")

# plt.xlabel('Person')
plt.ylabel('Instruction Coverage (%)', fontsize=font_size, fontweight='bold', font="helvetica")
plt.xlabel('Tools', fontsize=font_size, fontweight='bold', font="helvetica")
plt.ylim(0,101)
# plt.xticks(index + bar_width, fontsize=font_size)
plt.xticks([]) 
# plt.tick_params(bottom = False)
plt.yticks(fontsize=font_size)
plt.yticks(np.arange(0, 101, step=10.0))
# plt.legend(fontsize=18)
ax.legend(fontsize=font_size, ncol=4, loc='best', bbox_to_anchor=(1.2, 1.2))
ax.set_axisbelow(True)
ax.yaxis.grid(color='lightgrey', linestyle='dashed')

ax.spines["top"].set_visible(False)
ax.spines["top"].set_visible(False)
ax.spines["left"].set_visible(False)
ax.spines["left"].set_visible(False)
ax.spines["right"].set_visible(False)
ax.spines["right"].set_visible(False)
ax.spines["bottom"].set_linewidth(2)
# ax1.spines["left"].set_linewidth(2)
ax.spines["right"].set_linewidth(2)
ax.spines["bottom"].set_capstyle("round")

plt.savefig(f"{dest_folder}/Coverage_comparison.pdf", format="pdf", bbox_inches='tight')

plt.show()