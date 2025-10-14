def a_b_p(depth, n_i, m_p, values, alpha, beta):
    if depth == 0 or n_i >= len(values):
        return values[n_i]
    
    if m_p: 
        max_eval = float('-inf')
        for i in range(2):
            eval = a_b_p(depth - 1, n_i * 2 + i, False, values, alpha, beta)
            max_eval = max(max_eval, eval)
            alpha = max(alpha, eval)
            if beta <= alpha:
                break
        return max_eval
    else:  
        min_eval = float('inf')
        for i in range(2):
            eval = a_b_p(depth - 1, n_i * 2 + i, True, values, alpha, beta)
            min_eval = min(min_eval, eval)
            beta = min(beta, eval)
            if beta <= alpha:
                break
        return min_eval


if __name__ == "__main__":
    values = [3, 5, 6, 9, 1, 2, 0, -1]
    depth = 3
    alpha = float('-inf')
    beta = float('inf')
    optimal_value = a_b_p(depth, 0, True, values, alpha, beta)
    print(f"Optimal value is: {optimal_value}")
