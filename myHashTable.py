class dictionary:
	maxLoadFactor = 0
	entries = 0
	cells = None
	size = 0

	def __init__(self,size,maxLoadFactor):
		self.maxLoadFactor = maxLoadFactor
		self.size = size
		self.cells = []
		for index in range(size):
			self.cells.append(Node(None,None))

class Node:
	key = None
	value = None
	nextNode = None

	def __init__(self,value,key):
		self.value = value
		self.key = key
	

def getIndex(size, key): 
	key = str(key)
	prime = 31
	index = 0
	for i in range(len(key)):
		index = prime * index + ord(key[i])
	
	return index % size


def getLoadFactor(entries,size):
	return entries / size


def resize(oldDict):
	loadFactor = getLoadFactor(oldDict.entries,oldDict.size)
	#print(f"{loadFactor=}")
	if (loadFactor <= oldDict.maxLoadFactor):
		return oldDict

	newDict = dictionary(oldDict.size * 2, oldDict.maxLoadFactor)
	oldCells = oldDict.cells

	for index in range(oldDict.size):
		currentNode = oldCells[index]
		if (currentNode.key == None):
			continue

		while (currentNode != None):
			insert(newDict,currentNode.value,currentNode.key)
			currentNode = currentNode.nextNode

	oldDict = None
	return resize(newDict)


"""Insert"""
def insert(dict,value,key):
	index = getIndex(dict.size,key)
	cells = dict.cells
	newNode = Node(value,key)
	if (cells[index].key != None and cells[index].key != "delete"):
		newNode.nextNode = cells[index]
		
	cells[index] = newNode
	dict.entries += 1
	return resize(dict)
	

"""Search"""
def search(dict,keyToSearch):
	cells = dict.cells
	index = getIndex(dict.size, keyToSearch)
	nodeWithKey = getNodeWithKey(cells[index],keyToSearch)

	if (nodeWithKey != None):
		return nodeWithKey.value
	return None


"""Delete"""
def delete(dict,keyToDelete):
	cells = dict.cells
	index = getIndex(dict.size,keyToDelete)
	nodeToDelete = getNodeWithKey(cells[index],keyToDelete)

	if (nodeToDelete == None):
		return dict

	if (nodeToDelete == cells[index]):
		nodeToDelete.value = "deleted"
		nodeToDelete.key = "deleted"
		if (nodeToDelete.nextNode != None):
			cells[index] = nodeToDelete.nextNode
		return dict

	prevNode = getPrevNode(cells[index],keyToDelete)
	if (prevNode != None):
		prevNode.nextNode = prevNode.nextNode.nextNode
	return dict
	

"""Ver si dos palabras son permutaciones"""
def checkIfPermutations(str1,str2):
	if (len(str1) != len(str2)):
		return False

	sumOfOrds1 = 0
	sumOfOrds2 = 0
	size = len(str1)
	for index in range(size):
		sumOfOrds1 += ord(str1[index])
		sumOfOrds2 += ord(str2[index])

	return (sumOfOrds1 == sumOfOrds2)


"""Ver si una lista tiene elementos duplicados"""
def checkIfDuplicates(list):
	dict = dictionary(6,1.5)
	for element in list:
		if (search(dict,element) != None):
			return True
		insert(dict,element,element)
	return False


"""Contar repeticiones de caracteres en una cadena"""
def countOccurrences(string):
	newStr = ""
	occurrences = 0
	size = len(string)
	
	for index in range(size):
		occurrences += 1
		
		if (index == size -1):
			if (string[index] != string[index - 1]):
				occurrences = 1
			newStr += (string[index] + str(occurrences))
			
		elif (string[index] != string[index + 1]):
			newStr += (string[index] + str(occurrences))
			occurrences = 0

	return newStr
	

"""Ver si un string es substring de otro"""
def getFirstOccurrence(str1,str2):
	if (len(str1) < len(str2)):
		return None
		
	lenOfStr = len(str1)
	lenOfSub = len(str2)
	subIndex = 0
	for index in range(lenOfStr):
		if (subIndex == lenOfSub):
			return index - lenOfSub
		if (str1[index] == str2[subIndex]):
			subIndex += 1
		else:
			subIndex = 0
	return None


"""Ver si un conjunto es subconjunto de otro"""
def checkIfSubSet(set1,set2):
	if (len(set1) < len(set2)):
		return None

	dictSet1 = createDictionary(set1,6,1.5)
	for element in set2:
		if (search(dictSet1,element) == None):
			return False
	return True

	
"""Funciones auxiliares"""
def getNodeWithKey(currentNode,keyToSearch):
	while (currentNode != None):
		if (currentNode.key == keyToSearch):
			return currentNode
		currentNode = currentNode.nextNode
	return None


def getPrevNode(currentNode,keyToSearch):
	while (currentNode.nextNode != None):
		if (currentNode.nextNode.key == keyToSearch):
			return currentNode
		currentNode = currentNode.nextNode
	return None


def createDictionary(str,size,maxLoadFactor):
	dict = dictionary(size,maxLoadFactor)
	for char in str:
		insert(dict, char, char)

	return resize(dict)


"""Prints"""
def printAllIndexes(dict):
	cells = dict.cells
	size = dict.size
	for cell in cells:
		printIndex(cell)


def printIndex(currentNode):
	print("[", end = "")
	while (currentNode != None):
		print(currentNode.value, end="")
		if (currentNode.nextNode != None):
			print("",end=", ")
		currentNode = currentNode.nextNode
	print("]")
