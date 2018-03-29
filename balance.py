def balancing(node):
	#if it has left or child children call balancing() on them
	if len(node.left_child) > 0:
		for i in range(len(node.left_child)):
			node.left_weight += balancing(node.left_child[i])
	if len(node.right_child) > 0:
		for i in range(len(node.right_child)):
			node.right_weight += balancing(node.right_child[i])

	#now balance current node
	node.weight_to_add = abs(node.left_weight - node.right_weight)
	node.balanced = True
	
	return (node.balance_weight + node.left_weight + node.right_weight + node.weight_to_add)


class Node(object):

    def __init__(self):
		self.balanced = False #boolean to check whether balance is balanced or not
		self.node_id = None 
		self.left_child = [] #array of left child nodes
		self.right_child = [] #array of right child nodes
		self.balance_weight = 10
		self.left_weight = 0 #total weight on left side
		self.right_weight = 0 #total weight of right side 
		self.weight_to_add = 0 #additional weight to make it balanced
        


def main(N, arr):
	Nodes = []

	# Creating a list of nodes with node id starting from 0
	for k in range(N):
		Nodes.append(Node())
		Nodes[k].node_id = k


	i = 0
	#loop in steps of 2:
	for j in range(0,len(arr),2):

		l_strs = list(map(int, arr[j].split(" ") ))
		Nodes[i].left_weight = l_strs[0]
		
		#if length of l_strs is greater than one that means it has left node
		if len(l_strs) > 1:
			Nodes[i].left_child = []
		for z in range(1, len(l_strs)):
			Nodes[i].left_child.append(Nodes[l_strs[z]])


		r_strs = list(map(int, arr[j+1].split(" ") ))
		Nodes[i].right_weight = r_strs[0]
		
		#if length of r_strs is greater than one that means it has right node
		if len(r_strs) > 1:
			Nodes[i].right_child = []
		for z in range(1, len(r_strs)):
			Nodes[i].right_child.append(Nodes[r_strs[z]])

		i += 1

	#balance each node
	for z in range(len(Nodes)):
		if not Nodes[z].balanced:
			balancing(Nodes[z])

	#output
	for m in range(len(Nodes)):
		if Nodes[m].left_weight < Nodes[m].right_weight:
			print(m ,":", Nodes[m].weight_to_add, "0")
		elif Nodes[m].left_weight >= Nodes[m].right_weight:
			print(m,": 0", Nodes[m].weight_to_add);




#input
N = int(input())
arr= []
for i in range(2*N):
	arr.append(input())

main(N, arr)




