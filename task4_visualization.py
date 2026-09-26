import pandas as pd
import matplotlib.pyplot as plt
import os


# --------------------------------------------------
# LOAD DATA
# --------------------------------------------------

input_file = "data/trends_analysed.csv"

df = pd.read_csv(input_file)

print(f"Loaded {len(df)} stories from {input_file}")


# Create the output folder if it does not already exist
os.makedirs("outputs", exist_ok=True)


# --------------------------------------------------
# CHART 1 - TOP 10 STORIES BY SCORE
# --------------------------------------------------

# Sort stories by score and select the top 10
top_stories = df.sort_values(
    by="score",
    ascending=False
).head(10).copy()


# Shorten titles longer than 50 characters
top_stories["short_title"] = top_stories["title"].apply(
    lambda title: title[:50] + "..."
    if len(title) > 50
    else title
)


plt.figure(figsize=(10, 6))

plt.barh(
    top_stories["short_title"],
    top_stories["score"]
)

# Reverse the order so the highest score appears at the top
plt.gca().invert_yaxis()

plt.title("Top 10 Stories by Score")
plt.xlabel("Score")
plt.ylabel("Story Title")

plt.tight_layout()

# Save BEFORE showing the chart
plt.savefig(
    "outputs/chart1_top_stories.png",
    dpi=150
)

plt.show()

plt.close()


# --------------------------------------------------
# CHART 2 - STORIES PER CATEGORY
# --------------------------------------------------

category_counts = df["category"].value_counts()


plt.figure(figsize=(8, 6))

plt.bar(
    category_counts.index,
    category_counts.values
)

plt.title("Stories per Category")
plt.xlabel("Category")
plt.ylabel("Number of Stories")

plt.xticks(rotation=30)

plt.tight_layout()

# Save the chart
plt.savefig(
    "outputs/chart2_categories.png",
    dpi=150
)

plt.show()

plt.close()


# --------------------------------------------------
# CHART 3 - SCORE VS COMMENTS
# --------------------------------------------------

plt.figure(figsize=(10, 6))


# Separate popular and non-popular stories
popular = df[df["is_popular"] == True]
not_popular = df[df["is_popular"] == False]


# Plot non-popular stories
plt.scatter(
    not_popular["score"],
    not_popular["num_comments"],
    label="Not Popular"
)


# Plot popular stories
plt.scatter(
    popular["score"],
    popular["num_comments"],
    label="Popular"
)


plt.title("Score vs Comments")
plt.xlabel("Score")
plt.ylabel("Number of Comments")
plt.legend()

plt.tight_layout()

# Save the chart
plt.savefig(
    "outputs/chart3_scatter.png",
    dpi=150
)

plt.show()

plt.close()


# --------------------------------------------------
# BONUS - TRENDPULSE DASHBOARD
# --------------------------------------------------

fig, axes = plt.subplots(
    2,
    2,
    figsize=(16, 11)
)


# -------------------------
# Dashboard Chart 1
# -------------------------

axes[0, 0].barh(
    top_stories["short_title"],
    top_stories["score"]
)

axes[0, 0].invert_yaxis()

axes[0, 0].set_title("Top 10 Stories by Score")
axes[0, 0].set_xlabel("Score")
axes[0, 0].set_ylabel("Story Title")


# -------------------------
# Dashboard Chart 2
# -------------------------

axes[0, 1].bar(
    category_counts.index,
    category_counts.values
)

axes[0, 1].set_title("Stories per Category")
axes[0, 1].set_xlabel("Category")
axes[0, 1].set_ylabel("Number of Stories")

axes[0, 1].tick_params(
    axis="x",
    rotation=30
)


# -------------------------
# Dashboard Chart 3
# -------------------------

axes[1, 0].scatter(
    not_popular["score"],
    not_popular["num_comments"],
    label="Not Popular"
)

axes[1, 0].scatter(
    popular["score"],
    popular["num_comments"],
    label="Popular"
)

axes[1, 0].set_title("Score vs Comments")
axes[1, 0].set_xlabel("Score")
axes[1, 0].set_ylabel("Number of Comments")
axes[1, 0].legend()


# Hide the unused fourth subplot
axes[1, 1].axis("off")


# Overall dashboard title
fig.suptitle(
    "TrendPulse Dashboard",
    fontsize=20
)

plt.tight_layout()

# Save the dashboard
plt.savefig(
    "outputs/dashboard.png",
    dpi=150,
    bbox_inches="tight"
)

plt.show()

plt.close()


print("\nAll visualizations created successfully!")
print("Files saved in the outputs/ folder.")