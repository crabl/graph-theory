def construct_alternating_path(v, e, a_list):
    alternating_list = a_list
    vertex_list = v
    edge_list = e

    if len(vertex_list) == 1:
        print a_list

    if len(vertex_list) == 0:
        return a_list

    current_vertex = vertex_list[0]
    for edge in edge_list:
        if current_vertex in edge:
            other_index = 1 - edge.index(current_vertex) # HACK
            
            if edge[other_index] in vertex_list:
                alternating_list.append(edge)
                for vertex in edge:
                    vertex_list.remove(vertex)
                return construct_alternating_path(vertex_list, edge_list, alternating_list)
            
    # There are no edges in our edge_list with the
    # current vertex, so remove it from our list
    vertex_list.remove(current_vertex)
    return construct_alternating_path(vertex_list, edge_list, alternating_list)


if __name__ == "__main__":
    num_vertices = int(raw_input("Number of vertices: "))
    V = range(0, num_vertices)
    V = [str(v) for v in V]
    E = []
    num_edges = int(raw_input("Number of edges: "))

    for i in range(0, num_edges):
        line = raw_input("")
        E.append(tuple(line.split(' ')))

    print construct_alternating_path(V, E, [])
