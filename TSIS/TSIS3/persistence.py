import json
import os

def load_scores():
    if not os.path.exists("leaderboard.json"):
        return []
    with open("leaderboard.json") as f:
        return json.load(f)

def save_score(name, score, distance):
    scores = load_scores()
    scores.append({"name": name, "score": score, "distance": distance})
    scores = sorted(scores, key=lambda x: x["score"], reverse=True)[:10]

    with open("leaderboard.json", "w") as f:
        json.dump(scores, f, indent=4)


def load_settings():
    if not os.path.exists("settings.json"):
        return {"sound": True, "difficulty": "easy"}
    with open("settings.json") as f:
        return json.load(f)

def save_settings(settings):
    with open("settings.json", "w") as f:
        json.dump(settings, f, indent=4)