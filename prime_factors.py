# Python Challenge 1 from LinkedIn Learning
# Find prime factors of a number

def find_prime_factors(N):
	factors = list()
	divisor = 2
	while (divisor <= N):
		if (N % divisor) == 0:
			factors.append(divisor)
			N=N/divisor
		else:
			divisor += 1
	return factors

print(find_prime_factors(630))
