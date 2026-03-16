from collections import defaultdict

def detect_attacks(events, threshold=3):

    attempts = defaultdict(int)

    for event in events:
        ip = event["ip"]
        attempts[ip] += 1

    attackers = {}

    for ip, count in attempts.items():
        if count >= threshold:
            attackers[ip] = count

    return attackers
