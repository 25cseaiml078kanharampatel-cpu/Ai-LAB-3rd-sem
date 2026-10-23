"""
Experiment 5: Mini-Max Algorithm
Aim: To implement the Mini-Max algorithm for decision making in a game tree using Python.
"""
import math

def minimax(depth, node_index, is_max, scores, max_depth):
    if depth == max_depth:
        return scores[node_index]

    if is_max:
        return max(
            minimax(depth + 1, node_index * 2, False, scores, max_depth),
            minimax(depth + 1, node_index * 2 + 1, False, scores, max_depth)
        )
    else:
        return min(
            minimax(depth + 1, node_index * 2, True, scores, max_depth),
            minimax(depth + 1, node_index * 2 + 1, True, scores, max_depth)
        )

if __name__ == '__main__':
    scores_input = input("Enter leaf node scores separated by space: ")
    scores = list(map(int, scores_input.split()))

    max_depth = int(math.log2(len(scores)))

    optimal_value = minimax(0, 0, True, scores, max_depth)
    print("The optimal value is:", optimal_value)
