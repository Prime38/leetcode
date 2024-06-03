from concept.Graph.Graph import Graph
from concept.Stack.Stack import Stack


def deapth_first_search(g:Graph, start:int):
    if g.adj_list[start] is None:
        return
    ans=[]
    visited=[False]*g.nodes
    stack=Stack()
    stack.push(start)
    visited[start]=True
    while not stack.is_empty() :
        current_val=stack.pop()
        ans.append(current_val)
        current_head= g.adj_list[current_val].head
        while current_head is not None:
            if not visited[current_head.val] :
                stack.push(current_head.val)
                visited[current_head.val]=True
            current_head=current_head.next
    return ans




if __name__ == '__main__':
    g=Graph(10)
    g.add_edge(0,1)
    g.add_edge(0,2)
    g.add_edge(1,3)
    g.add_edge(1, 5)
    g.add_edge(2, 4)
    g.add_edge(2, 6)
    g.add_edge(3, 7)
    g.add_edge(3, 8)
    g.add_edge(4, 9)
    g.add_edge(4, 5)
    g.add_edge(5, 7)
    g.add_edge(5, 6)
    g.add_edge(6, 8)
    g.add_edge(6, 9)
    g.add_edge(7,0)
    g.add_edge(8, 5)
    g.add_edge(7, 9)
    g.add_edge(9, 3)
    g.add_edge(9, 5)

    # print(str(g))
    print(deapth_first_search(g,0))