"""
Experiment 6: Alpha-Beta Pruning
Aim: To implement the Alpha-Beta Pruning algorithm for an adversarial search game tree using Python.
"""
import math

def minimax(depth, node_index, is_max, scores, alpha, beta, max_depth):
    if depth == max_depth:
        return scores[node_index]

    if is_max:
        max_eval = -math.inf
        for i in range(2):
            eval = minimax(depth + 1, node_index * 2 + i, False, scores, alpha, beta, max_depth)
            max_eval = max(max_eval, eval)
            alpha = max(alpha, eval)
            if beta <= alpha:
                break
        return max_eval
    else:
        min_eval = math.inf
        for i in range(2):
            eval = minimax(depth + 1, node_index * 2 + i, True, scores, alpha, beta, max_depth)
            min_eval = min(min_eval, eval)
            beta = min(beta, eval)
            if beta <= alpha:
                break
        return min_eval

if __name__ == '__main__':
    scores = []
    num_nodes = 8
    print("Enter 8 leaf node values:")
    for i in range(num_nodes):
        val = int(input())
        scores.append(val)

    max_depth = int(math.log2(len(scores)))

    optimal_value = minimax(0, 0, True, scores, -math.inf, math.inf, max_depth)
    print("The optimal value is:", optimal_value)
