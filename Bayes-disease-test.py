prior = 0.001
likelihood = 0.99

p_d = prior * likelihood + (1.0 - prior) * (1.0 - likelihood)

posterior = likelihood * prior / p_d

print("posterior = %.3f" % posterior)
