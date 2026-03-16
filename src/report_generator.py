def generate_report(attackers):

    print("\nSSH Brute Force Detection Report")
    print("--------------------------------")

    if not attackers:
        print("No brute force attacks detected.")
        return

    print("\nTop Attackers:\n")

    sorted_attackers = sorted(
        attackers.items(),
        key=lambda x: x[1],
        reverse=True
    )

    rank = 1

    for ip, attempts in sorted_attackers:
        print(f"{rank}. {ip} -> {attempts} failed attempts")
        rank += 1
