
import matplotlib.pyplot as plt

components = ["Top 16", "25%", "50%", "Bottom 16"]

# Enter accuracy values as percentages
gsm8k = [0.155, 0.124, 0.118, 0.114]
math = [0.038, 0.031, 0.023, 0.024]

fig, axes = plt.subplots(1, 2, figsize=(10, 4))

for ax, values, title in zip(
    axes, [gsm8k, math], ["GSM8K", "MATH"]
):
    ax.bar(components, values)
    ax.set_title(title)
    ax.set_ylabel("Accuracy")
    ax.set_ylim(0, max(values) * 1.2)
    ax.grid(axis="y", alpha=0.3)

plt.suptitle("PiSSA Rank 16: Singular Value Selection")
plt.tight_layout()
plt.savefig("/Users/razeen/Downloads/q3_accuracy.png", dpi=300)
plt.show()
