import math

# Parameters for the binomial formula
n = 20  # Number of trials
k = 2   # Number of successes
p = 9 / 3200  # Probability of success

# Binomial coefficient: n! / (k! * (n - k)!)
binom_coeff = math.comb(n, k)

# Binomial probability: P(X = k) = (n choose k) * p^k * (1-p)^(n-k)
p_exactly_2 = binom_coeff * (p ** k) * ((1 - p) ** (n - k))
print(f"{p_exactly_2}%")