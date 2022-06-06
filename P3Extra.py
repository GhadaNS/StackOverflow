from matplotlib import pyplot as plt
import numpy as np


def HistACC(Train, Test):
    X = ['GD', 'CN', 'JC', 'A', 'PA']
    Tr = [Train[x] for x in ['Sgd', 'Scn', 'Sjc', 'Sa', 'Spa']]
    Ts = [Test[x] for x in ['Sgd', 'Scn', 'Sjc', 'Sa', 'Spa']]
    x_axis = np.arange(len(X))
    fig, ax = plt.subplots()
    plt.title("Training & Testing Accuracy", fontsize=10)
    for s in ['top', 'bottom', 'left', 'right']:  # Remove axes splines
        ax.spines[s].set_visible(False)
    ax.xaxis.set_ticks_position('none')  # Remove x, y Ticks
    ax.yaxis.set_ticks_position('none')
    ax.grid(b=True, color='grey', linestyle='-.', linewidth=0.7, alpha=0.2)  # Add x, y gridlines
    plt.bar(x_axis - 0.1, Tr, width=0.2, label='Training ACC')
    plt.bar(x_axis + 0.1, Ts, width=0.2, label='Testing ACC')
    plt.xticks(x_axis, X)
    plt.xlabel('Similarity Measures')
    plt.ylabel('Accuracy')
    plt.legend()
    plt.savefig('Training & Testing Accuracy.png')  # Saving plot as png file
    # plt.show()
    plt.close()


def Hist(ACC, Str):
    X = list(ACC.keys())
    T = list(ACC.values())
    fig, ax = plt.subplots()
    ax.set_title(Str + "ing Accuracy", fontsize=10)
    for s in ['top', 'bottom', 'left', 'right']:  # Remove axes splines
        ax.spines[s].set_visible(False)
    ax.xaxis.set_ticks_position('none')  # Remove x, y Ticks
    ax.yaxis.set_ticks_position('none')
    ax.grid(b=True, color='gray', linestyle='-.', linewidth=0.7, alpha=0.2)  # Add x, y gridlines
    ax.xaxis.set_tick_params(pad=5)  # Add padding between axes and labels
    ax.yaxis.set_tick_params(pad=10)
    bars = ax.barh(X, T, 0.4)
    ax.bar_label(bars, padding=3)
    plt.ylabel('Similarity Measures')
    plt.xlabel('Accuracy')
    plt.savefig(Str + 'ing Accuracy.png')  # Saving plot as png file
    # plt.show()
    plt.close()
