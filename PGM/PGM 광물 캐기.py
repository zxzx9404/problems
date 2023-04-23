def solution(picks, minerals):
    ans = 155
    
    def dfs(idx, dia, iron, stone, fatigue):
        nonlocal ans
        # 다 캤거나 or 연장 다 씀
        if idx >= len(minerals) or not (dia + iron + stone):
            ans = min(fatigue, ans)
        
        dia_pick, iron_pick, stone_pick = 0, 0, 0
        for i in range(idx, min(idx+5, len(minerals))):
            dia_pick += 1
            iron_pick += 5 if minerals[i] == 'diamond' else 1
            stone_pick += 25 if minerals[i] == 'diamond' else 5 if minerals[i] == 'iron' else 1

        if dia:
            dfs(idx+5, dia-1, iron, stone, fatigue + dia_pick)
        if iron:
            dfs(idx+5, dia, iron-1, stone, fatigue + iron_pick)
        if stone:
            dfs(idx+5, dia, iron, stone-1, fatigue + stone_pick)
     
    dfs(0, picks[0], picks[1], picks[2], 0)
    return ans

# solution([1, 3, 2], ["diamond", "diamond", "diamond", "iron", "iron", "diamond", "iron", "stone"])
# solution([0, 1, 1], ["diamond", "diamond", "diamond", "diamond", "diamond", "iron", "iron", "iron", "iron", "iron", "diamond"])
