import requests
import time
import json
import os
from datetime import datetime


# HackerNews API endpoints
TOP_STORIES_URL = "https://hacker-news.firebaseio.com/v0/topstories.json"
ITEM_URL = "https://hacker-news.firebaseio.com/v0/item/{}.json"

HEADERS = {
    "User-Agent": "TrendPulse/1.0"
}


# Category keywords from the assignment
CATEGORY_KEYWORDS = {
    "technology": [
        "ai", "software", "tech", "code", "computer",
        "data", "cloud", "api", "gpu", "llm"
    ],
    "worldnews": [
        "war", "government", "country", "president",
        "election", "climate", "attack", "global"
    ],
    "sports": [
        "nfl", "nba", "fifa", "sport", "game", "team",
        "player", "league", "championship"
    ],
    "science": [
        "research", "study", "space", "physics",
        "biology", "discovery", "nasa", "genome"
    ],
    "entertainment": [
        "movie", "film", "music", "netflix", "game",
        "book", "show", "award", "streaming"
    ]
}


def get_category(title):
    """
    Check the story title against the category keywords.
    Return the first matching category.
    """
    title_lower = title.lower()

    for category, keywords in CATEGORY_KEYWORDS.items():
        for keyword in keywords:
            if keyword in title_lower:
                return category

    return None


def fetch_story(story_id):
    """Fetch one story from HackerNews."""
    try:
        response = requests.get(
            ITEM_URL.format(story_id),
            headers=HEADERS,
            timeout=10
        )

        response.raise_for_status()
        return response.json()

    except requests.RequestException as error:
        print(f"Failed to fetch story {story_id}: {error}")
        return None


def main():
    # Fetch the list of top story IDs
    try:
        response = requests.get(
            TOP_STORIES_URL,
            headers=HEADERS,
            timeout=10
        )

        response.raise_for_status()
        story_ids = response.json()[:500]

    except requests.RequestException as error:
        print(f"Failed to fetch top stories: {error}")
        return

    collected_stories = []

    # Keep track of how many stories we have collected
    # in each category.
    category_counts = {
        category: 0
        for category in CATEGORY_KEYWORDS
    }

    # Process the top 500 stories
    for story_id in story_ids:

        # Stop when all five categories have 25 stories
        if all(count == 25 for count in category_counts.values()):
            break

        story = fetch_story(story_id)

        if not story:
            continue

        # Only process stories that have a title
        title = story.get("title", "")

        if not title:
            continue

        category = get_category(title)

        # Ignore stories that don't match any category
        if category is None:
            continue

        # Don't collect more than 25 for one category
        if category_counts[category] >= 25:
            continue

        current_time = datetime.now().isoformat()

        story_data = {
            "post_id": story.get("id"),
            "title": title,
            "category": category,
            "score": story.get("score", 0),
            "num_comments": story.get("descendants", 0),
            "author": story.get("by"),
            "collected_at": current_time
        }

        collected_stories.append(story_data)
        category_counts[category] += 1

        print(
            f"Collected {category}: "
            f"{category_counts[category]}/25"
        )

    # Create data directory if it doesn't exist
    os.makedirs("data", exist_ok=True)

    # Create today's filename
    date_string = datetime.now().strftime("%Y%m%d")
    output_file = f"data/trends_{date_string}.json"

    # Save the collected stories
    with open(output_file, "w", encoding="utf-8") as file:
        json.dump(
            collected_stories,
            file,
            indent=4,
            ensure_ascii=False
        )

    print(
        f"Collected {len(collected_stories)} stories. "
        f"Saved to {output_file}"
    )

    print("Category totals:")
    for category, count in category_counts.items():
        print(f"{category}: {count}")


if __name__ == "__main__":
    main()