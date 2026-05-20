# Bayesian Network Builder

This project implements a simple Bayesian Network system from scratch in Python. 

The program allows users to:
* Create Bayesian network nodes
* Define dependencies between variables
* Store conditional probabilities
* Query probabilities
* Compute total probability
* Apply Bayes’ Theorem
* Compute joint probabilities

## Interactive Menu
The program allows the user to type in numbers corresponding to different commands to manipulate the network: 
```text
1: Add a Node
2: Set a Dependency
3: Define a Probability
4: Find a Probability
5: Display Network
6: Total Probability
7: Bayes Formula
8: Joint Probability
9: Quit
```

---

## What Is a Bayesian Network?

A Bayesian Network is a probabilistic graphical model that represents:

* random variables as nodes
* dependencies as directed edges
* conditional probabilities between variables

<img width="883" height="397" alt="image" src="https://github.com/user-attachments/assets/3e357ddc-1a9c-417a-ad5a-0f18882ef751" />

## Conditional Probability Tables (CPTs)

A Conditional Probability Table defines the probability of a variable given one or more parent variables.

In Bayesian Networks, CPTs are used to represent dependencies between events.

### Eg:

| Rain | P(Wet Grass = Yes) | P(Wet Grass = No) |
|------|--------------------|-------------------|
| Yes  | 0.95               | 0.05              |
| No   | 0.10               | 0.90              |

## Bayes’ Theorem
Bayes' Theorem is a formula used to calculate the probability of an event based on prior knowledge of conditions related to that event. 

```math
P(A|B) = \frac{P(B|A) \cdot P(A)}{P(B)}
```

Where:

* (P(A|B)) = probability of A given B
* (P(B|A)) = reverse conditional probability
* (P(A)) = prior probability
* (P(B)) = evidence probability

---

## Author

Micayla Pang
