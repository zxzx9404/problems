# 진짜 간만에 제대로 변수명 지어봄
# 72ms
# 부모 노드와 자식 노드 정보를 통해 품

from collections import defaultdict

N, M = map(int, input().split())
child_node = defaultdict(list)  # {'부모' : [자식1, 자식2]} 형태
parent_node = defaultdict(list)  # {'자식' : [부모1, 부모2]} 형태
root_node = []  # 원천 공급책
all_nodes = set()  # 그냥 모든 노드

for _ in range(M):
    parent, child = input().split()
    child_node[parent].append(child)  # 부모에 자식 넣고
    parent_node[child].append(parent)  # 자식에 부모 넣고
    all_nodes.update(parent, child)  # 모든 노드에 넣고

for node in all_nodes:  # 모든 노드 돌면서
    if not parent_node[node]:  # 부모가 없으면
        root_node.append(node)  # 원천 공급책임

arrested_brokers = list(input().split())[1:]  # 체포된 브로커

def kill_edge(node):  # 체포된 애의 자식 노드의 부모 노드에서 본인을 지워줌
    for child in child_node[node]:
        if node in parent_node[child]:
            parent_node[child].pop(parent_node[child].index(node))
            if not parent_node[child]:  # 만약 자식이 더 이상 부모가 없다면 (== 마약 공급 X)
                kill_edge(child)  # 걔의 자식또한 같은과정을 반복

for broker in arrested_brokers:
    kill_edge(broker)

ans = 0
for child, parent in parent_node.items():  # 체포된 마약상 아니면서, 원천 공급책 아니면서, 아직 부모(공급책)이 있는 경우
    if child not in arrested_brokers and child not in root_node and parent:
        ans +=1

print(ans)