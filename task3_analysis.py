import pandas as pd
import numpy as np


# --------------------------------------------------
# 1. LOAD THE CLEAN CSV
# --------------------------------------------------

input_file = "data/trends_clean.csv"

df = pd.read_csv(input_file)

print(f"Loaded data: {df.shape}")


# Print the first 5 rows
print("\nFirst 5 rows:")
print(df.head())


# Calculate average score and average comments
average_score = df["score"].mean()
average_comments = df["num_comments"].mean()

print(f"\nAverage score   : {average_score:.2f}")
print(f"Average comments: {average_comments:.2f}")


# --------------------------------------------------
# 2. ANALYSIS USING NUMPY
# --------------------------------------------------

# Convert score column into a NumPy array
scores = df["score"].to_numpy()

# Calculate NumPy statistics
mean_score = np.mean(scores)
median_score = np.median(scores)
std_score = np.std(scores)

highest_score = np.max(scores)
lowest_score = np.min(scores)

print("\n--- NumPy Stats ---")

print(f"Mean score   : {mean_score:.2f}")
print(f"Median score : {median_score:.2f}")
print(f"Std deviation: {std_score:.2f}")
print(f"Max score    : {highest_score}")
print(f"Min score    : {lowest_score}")


# --------------------------------------------------
# FIND CATEGORY WITH MOST STORIES
# --------------------------------------------------

category_counts = df["category"].value_counts()

most_common_category = category_counts.idxmax()
most_common_count = category_counts.max()

print(
    f"\nMost stories in: "
    f"{most_common_category} "
    f"({most_common_count} stories)"
)


# --------------------------------------------------
# FIND STORY WITH MOST COMMENTS
# --------------------------------------------------

most_commented_index = df["num_comments"].idxmax()

most_commented_story = df.loc[
    most_commented_index, "title"
]

most_commented_count = df.loc[
    most_commented_index, "num_comments"
]

print(
    f'\nMost commented story: '
    f'"{most_commented_story}" '
    f'— {most_commented_count} comments'
)


# --------------------------------------------------
# 3. ADD NEW COLUMNS
# --------------------------------------------------

# Engagement measures comments received per upvote
df["engagement"] = df["num_comments"] / (df["score"] + 1)


# Mark stories as popular when their score is
# greater than the overall average score
df["is_popular"] = df["score"] > average_score


# --------------------------------------------------
# 4. SAVE THE ANALYSED DATA
# --------------------------------------------------

output_file = "data/trends_analysed.csv"

df.to_csv(output_file, index=False)

print(f"\nSaved to {output_file}")