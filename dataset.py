"""
Shared data for the Mood Machine lab.

This file defines:
  - POSITIVE_WORDS: starter list of positive words
  - NEGATIVE_WORDS: starter list of negative words
  - SAMPLE_POSTS: short example posts for evaluation and training
  - TRUE_LABELS: human labels for each post in SAMPLE_POSTS
"""

# ---------------------------------------------------------------------
# Starter word lists
# ---------------------------------------------------------------------

POSITIVE_WORDS = [
    "happy",
    "great",
    "good",
    "love",
    "excited",
    "awesome",
    "fun",
    "chill",
    "relaxed",
    "amazing",
]

NEGATIVE_WORDS = [
    "sad",
    "bad",
    "terrible",
    "awful",
    "angry",
    "upset",
    "tired",
    "stressed",
    "hate",
    "boring",
]

# ---------------------------------------------------------------------
# Starter labeled dataset
# ---------------------------------------------------------------------

# Short example posts written as if they were social media updates or messages.
SAMPLE_POSTS = [
    "I love this class so much",
    "Today was a terrible day",
    "Feeling tired but kind of hopeful",
    "This is fine",
    "So excited for the weekend",
    "I am not happy about this",
]

# Human labels for each post above.
# Allowed labels in the starter:
#   - "positive"
#   - "negative"
#   - "neutral"
#   - "mixed"
TRUE_LABELS = [
    "positive",  # "I love this class so much"
    "negative",  # "Today was a terrible day"
    "mixed",     # "Feeling tired but kind of hopeful"
    "neutral",   # "This is fine"
    "positive",  # "So excited for the weekend"
    "negative",  # "I am not happy about this"
    "positive",  # "anyone else cooked for finals week? 🥶"
    "negative",  # "Can't wait to bomb finals 🤩"
    "positive",  # "lwk cooked that pop quiz",
    "negative",  # "feeling cute might crash out"
    "positive",  # "ts prof might be the greatest to ever do it"
    "mixed",     # "The campus cats are too cute... I wish they wouldn't run away 🥹"
    "negative",  # "dining hall feeding us straight slop ong 😂"
]

# TODO: Add 5-10 more posts and labels.
#
# Requirements:
#   - For every new post you add to SAMPLE_POSTS, you must add one
#     matching label to TRUE_LABELS.
#   - SAMPLE_POSTS and TRUE_LABELS must always have the same length.
#   - Include a variety of language styles, such as:
#       * Slang ("lowkey", "highkey", "no cap")
#       * Emojis (":)", ":(", "🥲", "😂", "💀")
#       * Sarcasm ("I absolutely love getting stuck in traffic")
#       * Ambiguous or mixed feelings
#
# Tips:
#   - Try to create some examples that are hard to label even for you.
#   - Make a note of any examples that you and a friend might disagree on.
#     Those "edge cases" are interesting to inspect for both the rule based
#     and ML models.
#
# Example of how you might extend the lists:
#
# SAMPLE_POSTS.append("Lowkey stressed but kind of proud of myself")
# TRUE_LABELS.append("mixed")
#
# Remember to keep them aligned:
#   len(SAMPLE_POSTS) == len(TRUE_LABELS)

SAMPLE_POSTS.append("anyone else cooked for finals week? 🥶")
TRUE_LABELS.append("negative")

SAMPLE_POSTS.append("Can't wait to bomb finals 🤩")
TRUE_LABELS.append("negative")

SAMPLE_POSTS.append("lwk cooked that pop quiz")
TRUE_LABELS.append("positive")

SAMPLE_POSTS.append("feeling cute might crash out")
TRUE_LABELS.append("negative")

SAMPLE_POSTS.append("ts prof might be the greatest to ever do it")
TRUE_LABELS.append("positive")

SAMPLE_POSTS.append("The campus cats are too cute... I wish they wouldn't run away 🥺")
TRUE_LABELS.append("mixed")

SAMPLE_POSTS.append("dining hall feeding us straight slop ong 😂😭")
TRUE_LABELS.append("negative")

SAMPLE_POSTS.append("Thank you White Monster for getting me through this exam season 🙂‍↕️")
TRUE_LABELS.append("positive")