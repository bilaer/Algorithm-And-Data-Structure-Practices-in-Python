#########################################################
#                   disjoint set                        #
#########################################################
# disjoint set is the data structure used to maintain   #
# sets that are disjoint to each other                  #
#                                                       #
# The performance addition, union and finding           #
# elements of disjoint set is nearly linear             #
#                                                       #
# disjoint set is very useful in different areas.       #
# It can be used in Kruskal's algorithm, a minimum      #
# spanning tree generate algorithm. It can be used to   #
# make maze.                                            #
#                                                       #
#########################################################



class DisjSet(object):
    def __init__(self, size):
        self.size = size
        # Initialize the the list to -1s which representing that
        # Similar to MakeSet function
        self.set = [-1]*size

    # Find the the root node of a given number.
    # It use path compression method to optimize the performance.
    # Path compression will update the node while traversing through the forest recursively
    def find(self, x):
        #print("in find %d" %(x))
        if(x > self.size or x < 0):
            #print("argument %d does not exist" %(x))
            return None
        else:
            if(self.set[x] < 0):
                #print("here1")
                #print("return %d" %x)
                return x
            else:
                #print("here2")
                result = self.find(self.set[x])
                self.set[x] = result
                return result

    # Union function use union-by-height method to improve the efficiency.
    # It always set the parent of node with smaller tree size to the larger one
    # After setting up the parent, it sum up the size of this new tree and give it to the
    # root of the this tree
    def union(self, x, y):
        if x >= 0 or x < self.size or y >= 0 or y < self.size:
            # Find the roots of x and y, compress the path while it searching the root
            rootX = self.find(x)
            rootY = self.find(y)
            if(rootX != rootY):
                if self.set[rootX] < self.set[rootY]:
                    self.set[rootY] = self.set[rootY] + self.set[rootX]
                    self.set[rootX] = rootY

                else:
                    self.set[rootX] = self.set[rootX] + self.set[rootY]
                    self.set[rootY] = rootX
            else:
                print("two arguments are in the same set")
                return
        else:
            print("arguments does not exist")
            return


    # Some trival helper functions
    def getSize(self):
        return self.size

    def printDisjSet(self):
        print(self.set)



if __name__ == "__main__":
    newSet = DisjSet(8)
    newSet.printDisjSet()
    newSet.union(4, 5)
    newSet.printDisjSet()
    newSet.union(6, 7)
    newSet.printDisjSet()
    newSet.union(5, 7)
    newSet.printDisjSet()
    newSet.union(3, 7)
    newSet.printDisjSet()
    newSet.union(2, 7)
    newSet.printDisjSet()
    newSet.union(1, 7)
    newSet.printDisjSet()
    newSet.union(0, 7)
    newSet.printDisjSet()
    newSet.union(5, 6)


