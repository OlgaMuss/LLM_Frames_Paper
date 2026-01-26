import numpy as np

# 1. Prepare the Correlation and P-value Matrices
cols_for_corr = ['score_T1', 'score_T4', 'score_T7', cocreation_col]
labels = ['T1 Score', 'T4 Score', 'T7 Score', 'Co-creation']

# Calculate Spearman Rho and P-values
corr_matrix = np.zeros((len(cols_for_corr), len(cols_for_corr)))
p_matrix = np.zeros((len(cols_for_corr), len(cols_for_corr)))

for i, col1 in enumerate(cols_for_corr):
    for j, col2 in enumerate(cols_for_corr):
        rho, p = spearmanr(df_final_all[col1], df_final_all[col2])
        corr_matrix[i, j] = rho
        p_matrix[i, j] = p

# 2. Create the annotations (Rho + P-value in parentheses)
annot_matrix = []
for i in range(len(cols_for_corr)):
    row = []
    for j in range(len(cols_for_corr)):
        star = "*" if p_matrix[i, j] < 0.05 else ""
        label = f"{corr_matrix[i, j]:.2f}{star}\n(p={p_matrix[i, j]:.3f})"
        row.append(label)
    annot_matrix.append(row)

# 3. Visualization: Half Matrix (FLIPPED - showing upper triangle)
plt.figure(figsize=(10, 8))

# Create a mask for the LOWER triangle (this shows the UPPER triangle)
mask = np.tril(np.ones_like(corr_matrix, dtype=bool))

# Set up color palette (Coolwarm or Blues)
cmap = sns.diverging_palette(220, 20, as_cmap=True)

sns.heatmap(corr_matrix, 
            mask=mask, 
            annot=np.array(annot_matrix), 
            fmt="", 
            cmap=cmap, 
            center=0,
            vmin=-1, vmax=1,
            xticklabels=labels, 
            yticklabels=labels, 
            cbar_kws={'label': 'Spearman Rho (ρ)'},
            square=True,
            linewidths=.5)

plt.title("Correlation Matrix: Knowledge & Co-creation\n(with p-values)", fontweight='bold', fontsize=16, pad=30)
plt.tight_layout()
plt.show()
