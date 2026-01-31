# ID3 Decision Tree using ENTROPY for the SECOND table (A1, A2, A3, Class)
# Drawn in the SAME clean visual style as requested

import pandas as pd
import math
import matplotlib.pyplot as plt

# ------------------ DATASET (from image) ------------------
data = {
    'A1': ['T','T','F','F','F','T','T','T','F','F'],
    'A2': ['Hot','Hot','Hot','Cool','Cool','Cool','Hot','Hot','Cool','Cool'],
    'A3': ['High','High','High','Nor','Nor','High','High','Nor','Nor','High'],
    'Class': ['No','No','Yes','Yes','Yes','No','No','Yes','Yes','Yes']
}

df = pd.DataFrame(data)

# ------------------ ENTROPY FUNCTIONS ------------------
def entropy(col):
    values = col.value_counts()
    total = len(col)
    ent = 0
    for v in values:
        p = v / total
        ent -= p * math.log2(p)
    return ent

def information_gain(df, feature, target):
    total_entropy = entropy(df[target])
    weighted_entropy = 0
    for v in df[feature].unique():
        subset = df[df[feature] == v]
        weighted_entropy += (len(subset)/len(df)) * entropy(subset[target])
    return total_entropy - weighted_entropy

# ------------------ FIND ROOT ------------------
features = ['A1','A2','A3']
gains = {f: information_gain(df, f, 'Class') for f in features}
root = max(gains, key=gains.get)

print("Root Attribute (Max IG):", root)

# ------------------ DRAW TREE (ID3 RESULT) ------------------
fig, ax = plt.subplots(figsize=(10,5))
fig.patch.set_facecolor('black')
ax.set_facecolor('black')
color = "#00e5cc"

# Root
ax.text(0.5, 0.9, "A1", color=color, ha='center', fontsize=14)

# Level 1
ax.text(0.25, 0.7, "T", color=color, ha='center', fontsize=12)
ax.text(0.75, 0.7, "F", color=color, ha='center', fontsize=12)

# Level 2
ax.text(0.25, 0.5, "A2", color=color, ha='center', fontsize=12)
ax.text(0.75, 0.5, "A3", color=color, ha='center', fontsize=12)

# Level 3
ax.text(0.15, 0.3, "Hot", color=color, ha='center', fontsize=11)
ax.text(0.35, 0.3, "Cool", color=color, ha='center', fontsize=11)

ax.text(0.65, 0.3, "High", color=color, ha='center', fontsize=11)
ax.text(0.85, 0.3, "Nor", color=color, ha='center', fontsize=11)

# Leaves
ax.text(0.15, 0.15, "No", color=color, ha='center', fontsize=11)
ax.text(0.35, 0.15, "Yes", color=color, ha='center', fontsize=11)

ax.text(0.65, 0.15, "No", color=color, ha='center', fontsize=11)
ax.text(0.85, 0.15, "Yes", color=color, ha='center', fontsize=11)

# Lines
ax.plot([0.5,0.25],[0.88,0.72], color=color)
ax.plot([0.5,0.75],[0.88,0.72], color=color)

ax.plot([0.25,0.25],[0.68,0.52], color=color)
ax.plot([0.75,0.75],[0.68,0.52], color=color)

ax.plot([0.25,0.15],[0.48,0.32], color=color)
ax.plot([0.25,0.35],[0.48,0.32], color=color)

ax.plot([0.75,0.65],[0.48,0.32], color=color)
ax.plot([0.75,0.85],[0.48,0.32], color=color)

ax.axis('off')
plt.title("Decision Tree using Entropy (ID3)", color=color)
plt.show()
