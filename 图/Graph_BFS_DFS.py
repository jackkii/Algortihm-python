# Graph_BFS_DFS
# -------------------------
# 图的遍历(深度搜索，广度搜索)
# -------------------------
# Jackkii   2019/06/20
#


class Vertex:     # 节点定义
    def __init__(self, key):
        self.id = key
        self.connectedTo = {}
        self.color = 'white'
        self.pred = None

    def addNeighbor(self, nbr_id, nbrvertex):                  # 添加节点id及节点进字典中
        self.connectedTo[nbr_id] = nbrvertex

    def __str__(self):
        return str(self.id) + 'connectedTo: ' + str([x.id for x in self.connectedTo])

    def getId(self):
        return self.id

    def getConnections(self):                                   # 返回邻居结点id，按升序排列
        return sorted(self.connectedTo.keys())

    def getColor(self):
        return self.color


class Graph:        # 图定义
    def __init__(self, num):                 # 初始化
        self.initnum = num                   # 初始图结点个数
        self.vertList = {}                   # 结点字典
        self.numVertices = 0                 # 已放入图的结点个数

    def __contrains__(self, n):              # 当遇到以for k in self语句时，直接返回vertlist中的object
        return n in self.vertList            # 也可使用key和对应字典用法来访问

    def addVertex(self, key):                # 添加新结点如图并返回此结点
        self.numVertices = self.numVertices + 1
        newVertex = Vertex(key)
        self.vertList[key] = newVertex
        return newVertex

    def initVertList(self):                  # 初始化图结点（加入initnum个数的顶点)
        for x in range(self.initnum):
            self.addVertex(x)

    def getVertex(self, n):                  # 返回第n个结点
        if n in self.vertList:
            return self.vertList[n]
        else:
            return None

    def addEdge(self, f, t, cost=0):         # 添加边，即将尾点加进始点的邻居
        if f not in self.vertList:           # 若不存在此结点则加入此结点
            self.addVertex(f)
        if t not in self.vertList:
            self.addVertex(t)

        self.vertList[f].addNeighbor(t, self.vertList[t])
        self.vertList[t].addNeighbor(f, self.vertList[f])       # 若无向图则需加此句

    def getVertices(self):
        return self.vertList.keys()


class Queue:                                # 使用队列来完成广度搜索
    def __init__(self):
        self.items = []                     # 使用列表构建队列

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0, item)          # 列表头部入队

    def dequeue(self):
        return self.items.pop()             # 列表尾部出队

    def size(self):
        return len(self.items)


def bfs(start):                             # 广度优先搜索，给一个图内的初始结点
    vertQueue = Queue()
    vertQueue.enqueue(start)                # 初始结点入队

    while vertQueue.size() > 0:             # 当队内有元素时
        currentVert = vertQueue.dequeue()   # 出队第一个结点（完成该结点的访问）
        print(currentVert.id, end=' ')

        for nbr_id in currentVert.getConnections():                      # 将当前元素未被访问过的结点加入队中（这里按升序加入
            if currentVert.connectedTo[nbr_id].getColor() == 'white':    # 白色为未被访问过
                currentVert.connectedTo[nbr_id].color = 'gray'           # 灰色为被访问过
                vertQueue.enqueue(currentVert.connectedTo[nbr_id])
        currentVert.color = 'black'                                      # 黑色为当前结点所有邻居都被访问过


class DFSGraph(Graph):                      # 深度搜索图，继承图（使用递归完成遍历
    def __init__(self, num):
        super().__init__(num)

    def dfs(self):                          # 对图进行深度搜索
        for aVertex in self:                # 将图中每一个结点初始化为白色
            aVertex = 'white'
        for aVertex in self:                # 进行访问
            if aVertex == 'while':
                self.dfsvisit(aVertex)

    def dfsvisit(self, startVertex):
        print(startVertex.id, end=' ')      # 访问该结点
        startVertex.color = 'gray'          # 变为灰色

        for nextVertex in startVertex.getConnections():                 # 对所有邻居
            if startVertex.connectedTo[nextVertex].color == 'white':    # 若未访问过，则访问
                self.dfsvisit(startVertex.connectedTo[nextVertex])
        startVertex.color = 'black'


if __name__ == '__main__':
    verticesnum = eval(input())
    edgenum = eval(input())

    # mydfsgraph = DFSGraph(verticesnum)
    mygraph = Graph(verticesnum)
    for x in range(edgenum):
        f, t = eval(input())
        mygraph.addEdge(f, t)
    #    mydfsgraph.addEdge(f, t)

    firstvertice = eval(input())        # 初始访问顶点
    bfs(mygraph.vertList[firstvertice])
    # mydfsgraph.dfsvisit(mydfsgraph.vertList[1])
