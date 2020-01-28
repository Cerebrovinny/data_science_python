from scipy.stats import binom

# flip a coin 5 times, how the probability to give heads 3 times?
prob = binom.pmf(3, 5, 0.5)

#pass in 4 semaphores of 4 times, whats prob of take all green lights
# nenhuma, 1, 2 , 3, ou 4 times
binom.pmf(0, 4, 0.25)
binom.pmf(1, 4, 0.25)
binom.pmf(2, 4, 0.25)
binom.pmf(3, 4, 0.25)
binom.pmf(4, 4, 0.25)

#if 2 times semaphores
binom.pmf(4, 4, 0.5)

#accumulativy probability
binom.cdf(4, 4, 0.25)

#Exam with 90 questions the prob of shot 73 questions with 5 options in each
binom.pmf(73, 90, 0.25) * 100 # * 100 is to show percent rate