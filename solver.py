def solver(nodes, edges):
  solveMatrix(makeMatrix(nodes, edges))


def makeMatrix(nodes, edges):
  result = []
  for node in nodes:
    result.push(makeVectorFromNode(node, edges))

  for loop in getLoops(nodes, edges):
    result.push(makeVectorFromLoop(loop))

  return result

def makeVectorFromNode(node, edges):
  print "Not implemented yet"

def makeVectorFromLoop(loop):
  print "Not implemented yet"

def getLoops(nodes, edges):
  possLoops = getLoopsHelper(nodes[0], None, edges, [], len(edges))
  possLoops

def getLoopsHelper(startNode, currentNode, edges, loop, n):
  if currentNode in edges:
    return []
  if startNode == currentNode:
    return edges
  if n == 0:
    return []
  result = []
  for edge in connectedEdges(currentNode, edges):
    result += getLoopsHelper(startNode, otherNode(currentNode, edge), edges, loop+[edge], n - 1)
    result += getLoopsHelper(currentNode, otherNode(currentNode, edge), edges, [edge], n - 1)
  return result

def otherNode(currentNode, edge):
  if edge[0] == currentNode:
    return edge[1]
  return edge[0]

def connectedEdges(currentNode, edges):
  result = []
  for edge in edges:
    if edge[0] == currentNode or edge[1] == currentNode:
      result.push(edge)
  return result

def solveMatrix(matrix):
  print "Not implemented yet"

# test = [
#   (0, 1, [Resistor(2)]),
#   (0, 1, [Resistor(2)]),
#   (0, 1, [VoltageSource(6), Resistor(2)])
# ]

test = [
  (0, 1, [1]),
  (0, 1, [2]),
  (0, 1, [3,4])
]

print(getLoops([0,1], test))
