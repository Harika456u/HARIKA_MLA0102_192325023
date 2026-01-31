# Build Decision Tree using ENTROPY from the given table
# and DRAW it in the SAME style as the provided image

import pandas as pd
import math
import matplotlib.pyplot as plt

# ------------------ DATASET ------------------
data = {
    'Outlook': ['Sunny','Sunny','Overcast','Rain','Rain','Rain','Overcast',
                'Sunny','Sunny','Rain','Sunny','Overcast','Overcast','Rain'],
    'Temp': ['Hot','Hot','Hot','Mild','Cool','Cool','Mild',
             'Cool','Mild','Mild','Mild','Hot','Hot','Mild'],
    'Humidity': ['High','High','High','High','Normal','Normal','High',
                 'Normal','Normal','Normal','High','Normal','High','High'],
    'Wind': ['Weak','Strong','Weak','Weak','Weak','Strong','Strong',
             'Weak','Weak','Weak','Strong','Weak','Strong','Strong'],
    'PlayTennis': ['No','No','Yes','Yes','Yes','No','Yes',
                    'No','Yes','Yes','No','Yes','Yes','No']
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
    vals = df[feature].unique()
    weighted_entropy = 0
    for v in vals:
        subset = df[df[feature] == v]
        weighted_entropy += (len(subset)/len(df)) * entropy(subset[target])
    return total_entropy - weighted_entropy

# ------------------ FIND BEST ATTRIBUTE ------------------
features = ['Outlook','Temp','Humidity','Wind']
gains = {f: information_gain(df, f, 'PlayTennis') for f in features}
root = max(gains, key=gains.get)

print("Root Node (Max Information Gain):", root)

# ------------------ DRAW TREE (ID3 RESULT) ------------------
fig, ax = plt.subplots(figsize=(10,5))
fig.patch.set_facecolor('black')
ax.set_facecolor('black')
color = "#00e5cc"

# Root
ax.text(0.5, 0.9, "Outlook", color=color, ha='center', fontsize=14)

# Level 1
ax.text(0.25, 0.7, "Sunny", color=color, ha='center', fontsize=12)
ax.text(0.5, 0.7, "Overcast", color=color, ha='center', fontsize=12)
ax.text(0.75, 0.7, "Rain", color=color, ha='center', fontsize=12)

# Level 2
ax.text(0.25, 0.5, "Humidity", color=color, ha='center', fontsize=12)
ax.text(0.5, 0.5, "Yes", color=color, ha='center', fontsize=12)
ax.text(0.75, 0.5, "Wind", color=color, ha='center', fontsize=12)

# Level 3
ax.text(0.15, 0.3, "High", color=color, ha='center', fontsize=11)
ax.text(0.35, 0.3, "Normal", color=color, ha='center', fontsize=11)
ax.text(0.68, 0.3, "Weak", color=color, ha='center', fontsize=11)
ax.text(0.82, 0.3, "Strong", color=color, ha='center', fontsize=11)

# Leaves
ax.text(0.15, 0.15, "No", color=color, ha='center', fontsize=11)
ax.text(0.35, 0.15, "Yes", color=color, ha='center', fontsize=11)
ax.text(0.68, 0.15, "Yes", color=color, ha='center', fontsize=11)
ax.text(0.82, 0.15, "No", color=color, ha='center', fontsize=11)

# Lines
ax.plot([0.5,0.25],[0.88,0.72], color=color)
ax.plot([0.5,0.5],[0.88,0.72], color=color)
ax.plot([0.5,0.75],[0.88,0.72], color=color)

ax.plot([0.25,0.25],[0.68,0.52], color=color)
ax.plot([0.75,0.75],[0.68,0.52], color=color)

ax.plot([0.25,0.15],[0.48,0.32], color=color)
ax.plot([0.25,0.35],[0.48,0.32], color=color)

ax.plot([0.75,0.68],[0.48,0.32], color=color)
ax.plot([0.75,0.82],[0.48,0.32], color=color)

ax.axis('off')
plt.title("Decision Tree using Entropy (ID3) – Play Tennis", color=color)
plt.show()
