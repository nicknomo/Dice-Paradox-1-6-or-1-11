import random

def simulate_dice_matching(sample_size):
    # Initialize counters for each number 1–6
    observed_count = {}
    success_count = {}
    failure_count = {}

    for value in range(1, 7):
        observed_count[value] = 0
        success_count[value] = 0
        failure_count[value] = 0
    

    # Run the simulation
    for trial_number in range(sample_size):
        # Roll two dice
        die1 = random.randint(1, 6)
        die2 = random.randint(1, 6)

        # Randomly pick one of the two dice to observe
        if random.randint(0, 1) == 0:
            observed = die1
            other = die2
        else:
            observed = die2
            other = die1

        # Update counts
        observed_count[observed] += 1

        if other == observed:
            success_count[observed] += 1
        else:
            failure_count[observed] += 1

    # Display results
    print("\nSample Size:", sample_size, "\n")

    for value in range(1, 7):
        total = observed_count[value]
        successes = success_count[value]
        failures = failure_count[value]

        probability = successes / total if total > 0 else 0

        print("When the single, randomly observed dice is", value, ":")
        print("  Total cases:", total)
        print("  Match (success):", successes, "(" + str(round(probability, 6)) + ")")
        print("  No match (failure):", failures)
        print()

    return {
        "observed": observed_count,
        "success": success_count,
        "failure": failure_count
    }




simulate_dice_matching(900000)

