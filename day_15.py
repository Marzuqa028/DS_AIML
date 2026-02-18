# -*- coding: utf-8 -*-
"""
Created on Wed Feb 18 10:46:16 2026

@author: sumai
"""
# Probability of rolling a 4 on a fair die
favorable = 1
total_outcomes = 6
probability = favorable / total_outcomes
print(probability)

# Independent events example
p_rain = 0.3
p_traffic = 0.2
p_both = p_rain * p_traffic
print(p_both)

# Conditional probability example
p_A_and_B = 0.1
p_B = 0.4
p_A_given_B = p_A_and_B / p_B
print(p_A_given_B)

# Bayes' theorem example
p_disease = 0.01
p_positive_given_disease = 0.9
p_positive = 0.05
p_disease_given_positive = (p_positive_given_disease * p_disease) / p_positive
print(p_disease_given_positive)

#task 1 The Sample Space Map
sample_space = {("click","scroll"),("click","exit"),("click","click"),("scroll","click"),("scroll","exit"),("scroll","scroll"),("exit","scroll"),("exit","click"),("exit","exit")}
count = 0
for a,b in sample_space:
    if a == "click" or b == "click":
        count +=1
probability = count / len(sample_space)
print("Probability of at least one click: ", probability)

#1.2(dice)
import random
count_1 = 0
trials = 1000
for _ in range(trials):
    die1 = random.randint(1, 6)
    die2 = random.randint(1, 6)
    if die1 + die2 == 7:
        count_1 += 1
experimental_probability = count_1 / trials
print("Number of times sum = 7:", count_1)
print("Experimental Probability:", experimental_probability)


#task 2 The Logic of Dependency 
coin = ["head","tail"]
dice = [1,2,3,4,5,6]
prob_head = 1/2
prob_6 = 1/6
prob_head_and_6 = prob_head *prob_6
print("Probability of getting head and 6: ",prob_head_and_6)
bag = ["R"]*5 + ["B"]*5
total = len(bag)
red = bag.count("R")
prob_first = red / total
prob_second = (red - 1) / (total - 1)
prob_both = prob_first * prob_second
print("Probabilty that both are red: ", prob_both)


#task 3 The Bayesian Filter 
prob_spam = 0.1
prob_ham = 0.9
prob_free_given_spam = 0.9
prob_free_given_ham = 0.05
prob_free = (prob_free_given_spam * prob_spam) +(prob_free_given_ham * prob_ham)
prob_spam_given_free = (prob_free_given_spam * prob_spam) / prob_free
print("P(Spam | Free):", prob_spam_given_free)


















