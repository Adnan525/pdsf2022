import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

sid = pd.read_excel("myexcel.xls", sheet_name="SID")
uid = pd.read_excel("myexcel.xls", sheet_name="UID")
fig, axs = plt.subplots(2, 3)
plt.subplots_adjust(hspace=0.4)
# fig.tight_layout()

# s group
axs[0, 0].hist(sid["Ass1"], color = "blue", bins = 20)
axs[0, 0].set_title("S Group: Ass1")
axs[0, 0].set_xlabel("Mark")
axs[0, 0].set_ylabel("Probability")

axs[0, 1].hist(sid["Ass2"], color = "green", bins = 20)
axs[0, 1].set_title("S Group: Ass2")
axs[0, 1].set_xlabel("Mark")
axs[0, 1].set_ylabel("Probability")

axs[0, 2].hist(sid["FE"], color = "red", bins = 20)
axs[0, 2].set_title("S Group: FE")
axs[0, 2].set_xlabel("Mark")
axs[0, 2].set_ylabel("Probability")

# u group
axs[1, 0].hist(uid["Ass1"], color = "blue", bins = 20)
axs[1, 0].set_title("U Group: Ass1")
axs[1, 0].set_xlabel("Mark")
axs[1, 0].set_ylabel("Probability")

axs[1, 1].hist(uid["Ass2"], color = "green", bins = 20)
axs[1, 1].set_title("U Group: Ass2")
axs[1, 1].set_xlabel("Mark")
axs[1, 1].set_ylabel("Probability")

axs[1, 2].hist(uid["FE"], color = "red", bins = 20)
axs[1, 2].set_title("U Group: FE")
axs[1, 2].set_xlabel("Mark")
axs[1, 2].set_ylabel("Probability")

win = plt.gcf()
win.set_size_inches(15, 13)
plt.show()