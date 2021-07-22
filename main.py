# This program has logic to solve the 12 rings problem.

# "You are given 12 rings and ond one of these rings is different from the others, but you don't know if it is
# lighter or heavier than the others. Identify the special ring in three weighings and determine whether it is lighter
# or heavier than the others."

# Source of the Problem:  "An Engineering Approach to Digital Design," by William Fletcher.

# Author of this Program:  Michael Jablonski, NR Systems, Inc., River Heights, Utah USA

# The solution to the 12 rings problem, which I used the specification/requirements for this program can be found
# here:

# https://www.mathsisfun.com/pool_balls_solution.html

import random

# constants

A_LESS_THAN_B = -1                # the ring on the left of the balance weighs less than the ring on the right
A_EQUALS_B = 0                    # scale is balanced
A_GREATER_THAN_B = 1              # the ring on the left of the balance weighs more than the ring on the right
LIGHT = -1                        # a light ring
HEAVY = 1                         # a heavy ring
UNKNOWN = 99
NUMBER_OF_POSSIBILITIES = 24      # 12 rings * 2 (light or heavy)

# All logic is done within a class to encapsulate the variables, avoiding global variables and
# passing lots of parameters around.

class Rings:

    def __init__(self, ring_number, ring_weight):

        self.target_ring_number = ring_number    # tells the program which ring to use as the special ring
        self.target_ring_weight = ring_weight    # tells the program the weight of the spcial ring

        self.ring_weights = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.balance_result = UNKNOWN
        self.special_ring_number = UNKNOWN       # the objective is to determine the number of the special ring
        self.special_ring_weight = UNKNOWN       # and the weight (light or heavy) of the special ring

        self.ring_weights[self.target_ring_number] = self.target_ring_weight

    def balance_rings(self, a, b):

        # weigh the rings

        a_sum = 0
        b_sum = 0

        for i in a:
            a_sum += self.ring_weights[i - 1]

        for i in b:
            b_sum += self.ring_weights[i - 1]

        if a_sum == b_sum:
            return A_EQUALS_B
        else:
            if a_sum > b_sum:
                return A_GREATER_THAN_B
            else:
                return A_LESS_THAN_B

    def solve_12_rings_problem(self):

        self.balance_result = self.balance_rings((1, 2, 3, 4), (5, 6, 7, 8))

        if self.balance_result == A_EQUALS_B:
            self.outcome_1()

        elif self.balance_result == A_LESS_THAN_B:
            self.outcome_2()

        elif self.balance_result == A_GREATER_THAN_B:
            self.outcome_3()

    def outcome_1(self):

        self.balance_result = self.balance_rings((6, 7, 8), (9, 10, 11))

        if self.balance_result == A_EQUALS_B:
            self.outcome_1a()

        elif self.balance_result == A_LESS_THAN_B:
            self.outcome_1b()

        elif self.balance_result == A_GREATER_THAN_B:
            self.outcome_1c()

    def outcome_2(self):

        self.balance_result = self.balance_rings((1, 2, 5), (3, 6, 12))

        if self.balance_result == A_EQUALS_B:
            self.outcome_2a()

        elif self.balance_result == A_LESS_THAN_B:
            self.outcome_2b()

        elif self.balance_result == A_GREATER_THAN_B:
            self.outcome_2c()

    def outcome_3(self):

        self.balance_result = self.balance_rings((5, 6, 1), (7, 2, 12))

        if self.balance_result == A_EQUALS_B:
            self.outcome_3a()

        elif self.balance_result == A_LESS_THAN_B:
            self.outcome_3b()

        elif self.balance_result == A_GREATER_THAN_B:
            self.outcome_3c()

    def outcome_1a(self):

        self.balance_result = self.balance_rings((12,), (1,))

        # Ring 12 should never balance with ring 1.
        assert self.balance_result != A_EQUALS_B, "method outcome_1a, balance_result == A_EQUALS_B"

        if self.balance_result == A_LESS_THAN_B:
            self.special_ring_number = 12
            self.special_ring_weight = LIGHT

        elif self.balance_result == A_GREATER_THAN_B:
            self.special_ring_number = 12
            self.special_ring_weight = HEAVY

    def outcome_1b(self):

        self.balance_result = self.balance_rings((9,), (10,))

        if self.balance_result == A_EQUALS_B:
            self.special_ring_number = 11
            self.special_ring_weight = HEAVY

        elif self.balance_result == A_LESS_THAN_B:
            self.special_ring_number = 10
            self.special_ring_weight = HEAVY

        elif self.balance_result == A_GREATER_THAN_B:
            self.special_ring_number = 9
            self.special_ring_weight = HEAVY

    def outcome_1c(self):

        self.balance_result = self.balance_rings((9,), (10,))

        if self.balance_result == A_EQUALS_B:
            self.special_ring_number = 11
            self.special_ring_weight = LIGHT

        elif self.balance_result == A_LESS_THAN_B:
            self.special_ring_number = 9
            self.special_ring_weight = LIGHT

        elif self.balance_result == A_GREATER_THAN_B:
            self.special_ring_number = 10
            self.special_ring_weight = LIGHT

    def outcome_2a(self):

        self.balance_result = self.balance_rings((7,), (8,))

        if self.balance_result == A_EQUALS_B:
            self.special_ring_number = 4
            self.special_ring_weight = LIGHT

        elif self.balance_result == A_LESS_THAN_B:
            self.special_ring_number = 8
            self.special_ring_weight = HEAVY

        elif self.balance_result == A_GREATER_THAN_B:
            self.special_ring_number = 7
            self.special_ring_weight = HEAVY

    def outcome_2b(self):

        self.balance_result = self.balance_rings((1,), (2,))

        if self.balance_result == A_EQUALS_B:
            self.special_ring_number = 6
            self.special_ring_weight = HEAVY

        elif self.balance_result == A_LESS_THAN_B:
            self.special_ring_number = 1
            self.special_ring_weight = LIGHT

        elif self.balance_result == A_GREATER_THAN_B:
            self.special_ring_number = 2
            self.special_ring_weight = LIGHT

    def outcome_2c(self):

        self.balance_result = self.balance_rings((3,), (1,))

        if self.balance_result == A_EQUALS_B:
            self.special_ring_number = 5
            self.special_ring_weight = HEAVY

        elif self.balance_result == A_LESS_THAN_B:
            self.special_ring_number = 3
            self.special_ring_weight = LIGHT

        elif self.balance_result == A_GREATER_THAN_B:
            self.special_ring_number = 3
            self.special_ring_weight = LIGHT

    def outcome_3a(self):

        self.balance_result = self.balance_rings((3,), (4,))

        if self.balance_result == A_EQUALS_B:
            self.special_ring_number = 8
            self.special_ring_weight = LIGHT

        elif self.balance_result == A_LESS_THAN_B:
            self.special_ring_number = 4
            self.special_ring_weight = HEAVY

        elif self.balance_result == A_GREATER_THAN_B:
            self.special_ring_number = 3
            self.special_ring_weight = HEAVY

    def outcome_3b(self):

        self.balance_result = self.balance_rings((5,), (6,))

        if self.balance_result == A_EQUALS_B:
            self.special_ring_number = 2
            self.special_ring_weight = HEAVY

        elif self.balance_result == A_LESS_THAN_B:
            self.special_ring_number = 5
            self.special_ring_weight = LIGHT

        elif self.balance_result == A_GREATER_THAN_B:
            self.special_ring_number = 6
            self.special_ring_weight = LIGHT

    def outcome_3c(self):

        self.balance_result = self.balance_rings((7,), (11,))

        if self.balance_result == A_EQUALS_B:
            self.special_ring_number = 1
            self.special_ring_weight = HEAVY

        else:
            self.special_ring_number = 7
            self.special_ring_weight = LIGHT


def weight_to_string(w):
    if w == LIGHT:
        return "Light"
    else:
        return "Heavy"


def test_the_rings_class():
    num_errors = 0
    count = 0

    for i in range(0, 2):
        if i == 0:
            ring_wt = LIGHT
        else:
            ring_wt = HEAVY

        for j in range(0, 12):
            ring_num = j
            rings_12_test = Rings(ring_num, ring_wt)
            rings_12_test.solve_12_rings_problem()
            count += 1
            if ring_num + 1 != rings_12_test.special_ring_number or ring_wt != rings_12_test.special_ring_weight:
                num_errors += 1

    print(" Number of Tests:  ", count)
    print("Number of Errors:  ", num_errors)
    if count == NUMBER_OF_POSSIBILITIES and num_errors == 0:
        print("pass")
    else:
        print("fail")


# Main Program

# # Randomly select the special ring and its weight and then find that ring and determine if it is light or heavy.

ring_number = random.randint(0, 11)
ring_weight = random.randint(0, 1)

if ring_weight == 0:
    ring_weight = LIGHT
else:
    ring_weight = HEAVY

rings_12 = Rings(ring_number, ring_weight)
rings_12.solve_12_rings_problem()

print("Result")
print(" Target Ring Number:  ", rings_12.target_ring_number + 1)
print(" Target Ring Weight:  ", weight_to_string(rings_12.target_ring_weight))
print("Special Ring Number:  ", rings_12.special_ring_number)
print("Special Ring Weight:  ", weight_to_string(rings_12.special_ring_weight))
print("              Rings:  ", rings_12.ring_weights)

test_the_rings_class()

print('end of 12 rings program')
