# CRELS-REUNION-2026
# Synchronicity Probability Model (Exploratory)

import random

TARGET_WORDS = 44000
TARGET_LUCK = 4400

def synchronicity_score(words_count, lucky_amount):
    """
    Simple resonance score based on distance
    from the 44 / 4400 pattern.
    """
    word_diff = abs(words_count - TARGET_WORDS)
    luck_diff = abs(lucky_amount - TARGET_LUCK)

    score = 1 / (1 + word_diff + luck_diff)
    return score


def simulate_trials(trials=1000):
    results = []

    for _ in range(trials):
        words = random.randint(40000, 48000)
        luck = random.randint(4000, 4800)

        score = synchronicity_score(words, luck)
        results.append(score)

    return sum(results) / len(results)


if __name__ == "__main__":
    avg_score = simulate_trials()
    print(f"Average Synchronicity Score: {avg_score:.6f}")
