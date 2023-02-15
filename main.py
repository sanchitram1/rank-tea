'''Main script for the project.'''

import os
import sys
import random
import networkx as nx 

def build_tea_graph() -> nx.Graph:
    # TODO: Build the tea_graph & calculate tearank for each node
    pass 

def push_results(results):
    # TODO: Push the results to a database
    pass 

def compare_packages(package1, package2):
    print(f"Which package is better: {package1} or {package2}?")
    choice = input("Enter 1 for the first package, 2 for the second package, or 0 for a tie: ")
    while choice not in {"0", "1", "2"}:
        choice = input("Invalid choice. Please enter 1, 2, or 0: ")
    return int(choice)


def main():
    '''Main function for the project.'''
    num_pairs = int(input("How many pairs do you want to compare? "))
    tea_graph = build_tea_graph()
    pairs = random.sample(tea_graph.nodes, 2*num_pairs)
    results = []
    for i in range(num_pairs):
        package1, package2 = pairs[2*i], pairs[2*i+1]
        choice = compare_packages(package1, package2)
        if choice == 1:
            results.append((package1, package2, 1))
        elif choice == 2:
            results.append((package1, package2, -1))
        else:
            results.append((package1, package2, 0))
    push_results(results)

if __name__ == '__main__':
    main()
    