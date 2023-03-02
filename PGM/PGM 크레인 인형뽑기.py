def solution(board, moves):
    answer = 0
    N = len(board)
    basket = [-1]
    
    for move in moves:
        move -= 1
        for i in range(N):
            if board[i][move]:
                if basket[-1] == board[i][move]:
                    basket.pop()
                    answer += 2
                else:
                    basket.append(board[i][move])
                board[i][move] = 0
                break
    return answer
