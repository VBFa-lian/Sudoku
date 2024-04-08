import numpy as np

class DancingLinkNode:
    """Nodes in a Dancing Links data structure. Each Node stores the pointer to the Node above it, 
    below it, on its left and on its right. For this project, we do not need these Nodes to
    store other imformation in them.
    """

    def __init__(self, row: int, col: int, head: 'DancingLinkNode' = None) -> None:
        """Create a new Dancing Links Node at given row and column. The row index of
        column head Node are -1, and the row and column index of root Node are both -1.

        The rows and columns of Dancing Links are all circular linked lists, so for all new Nodes
        its all four pointers initially point to itself.

        Args:
            row (int): the row index
            col (int): the column index
            head (DancingLinkNode): the head of the column this node in. If this node itself is the head
            or root then leave this None
        """
        self.__left: 'DancingLinkNode' = self
        self.__right: 'DancingLinkNode' = self
        self.__above: 'DancingLinkNode' = self
        self.__below: 'DancingLinkNode' = self

        if head != None:
            self.__head = head
        else : 
            self.__head: 'DancingLinkNode' = self
        self.__loc = (row, col)

    def get_left(self) -> 'DancingLinkNode':
        """
        Returns:
            DancingLinkNode: the Node on the left of this Node.
        """
        return self.__left
    
    def get_right(self) -> 'DancingLinkNode':
        """
        Returns:
            DancingLinkNode: the Node on the right of this Node.
        """
        return self.__right
    
    def get_above(self) -> 'DancingLinkNode':
        """
        Returns:
            DancingLinkNode: the Node above this Node.
        """
        return self.__above
    
    def get_below(self) -> 'DancingLinkNode':
        """
        Returns:
            DancingLinkNode: the Node below this Node.
        """
        return self.__below
    
    def get_head(self) -> 'DancingLinkNode':
        """
        Returns:
            DancingLinkNode: the head node of the column this Node in 
        """
        return self.__head

    def set_left(self, node: 'DancingLinkNode'):
        """Set the Node on the left of this Node.
        """
        self.__left = node

    def set_right(self, node: 'DancingLinkNode'):
        """Set the Node on the left of this Node.
        """
        self.__right = node

    def set_above(self, node: 'DancingLinkNode'):
        """Set the Node on the left of this Node.
        """
        self.__above = node

    def set_below(self, node: 'DancingLinkNode'):
        """Set the Node on the left of this Node.
        """
        self.__below = node

    def get_loc(self) -> tuple[int, int]:
        """
        Returns:
            tuple[int, int]: the (row, col) tuple of this Node. 
            The row index of head Nodes are -1, and the row and column index of root Node are both -1.
        """
        return self.__loc
    
class DancingLinks:
    """The Dancing Links data structure.
    """

    def __init__(self, row: int, col: int) -> None:
        """Create a new Dancing Links with give rows and columns.

        Args:
            row (int): number of rows in this Dancing Links (except heads)
            col (int): number of columns in this Dancing Links.
        """
        self.__shape = (row, col)
        self.__firsts = np.empty(row, DancingLinkNode)
        self.__root = DancingLinkNode(-1, -1)
        self.__build()
        self.__row_count = 0

    def __build(self):
        """Build this Dancing Links
        """
        prev = self.__root
        for c in range(self.__shape[1]):
            node = DancingLinkNode(-1, c)
            prev.set_right(node)
            node.set_left(prev)
            prev = node
        prev.set_right(self.__root)
        self.__root.set_left(prev)

    def append_row(self, col_indexes: list[int], row_index = -1):
        """Append a new row to this Dancing Links

        Args:
            col_indexes (list[int]): the list of column indexes of Nodes in this row
            row_index (int): the index of the row to insert. If not specified then the row will be 
            appended at the end
        """
        if row_index == -1:
            row_index = self.__row_count
        for col_index in col_indexes:
            head = self.__root.get_right()
            while head != self.__root:
                if head.get_loc()[1] == col_index:
                    node = DancingLinkNode(row_index, col_index, head)
                    head.get_above().set_below(node)
                    node.set_above(head.get_above())
                    head.set_above(node)
                    node.set_below(head)
                    if self.__firsts[row_index] == None:
                        self.__firsts[row_index] = node
                    self.__firsts[row_index].get_left().set_right(node)
                    node.set_left(self.__firsts[row_index].get_left())
                    self.__firsts[row_index].set_left(node)
                    node.set_right(self.__firsts[row_index])
                    break
                head = head.get_right()
        self.__row_count += 1

    def remove_index(self, col_index: int) -> DancingLinkNode:
        """Remove the column at given index and all the rows that share Nodes with this column

        Args:
            col_index (int): the index of the column to be remove
    
        Returns:
            DancingLinkNode: the head of the removed column
        """
        head = self.__root.get_right()
        while head != self.__root:
            if head.get_loc()[1] == col_index:
                head.get_left().set_right(head.get_right())
                head.get_right().set_left(head.get_left())
                current = head.get_below()
                while current != head:
                    node = current.get_right()
                    while node != current:
                        node.get_above().set_below(node.get_below())
                        node.get_below().set_above(node.get_above())
                        node = node.get_right()
                    current = current.get_below()
                return head
            head = head.get_right()
        else:
            print('column not found')
            return None

    def remove(self, head: DancingLinkNode):
        """Remove the column of given head node and all the rows that share Nodes with this column

        Args:
            head (DancingLinkNode): head node of the column to remove
        """
        head.get_left().set_right(head.get_right())
        head.get_right().set_left(head.get_left())
        current = head.get_below()
        while current != head:
            node = current.get_right()
            while node != current:
                node.get_above().set_below(node.get_below())
                node.get_below().set_above(node.get_above())
                node = node.get_right()
            current = current.get_below()
    #    print('remove col ', head.get_loc()[1])
    #    print(self)


    def recover(self, head: DancingLinkNode):
        """Recover the column and related rows removed with the given head node

        Args:
            head (DancingLinkNode): head node of the head to recover
        """
        head.get_left().set_right(head)
        head.get_right().set_left(head)
        current = head.get_below()
        while current != head:
            node = current.get_right()
            while node != current:
                node.get_above().set_below(node)
                node.get_below().set_above(node)
                node = node.get_right()
            current = current.get_below()
    #    print('recover col ', head.get_loc()[1])
    #    print(self)
        

    def dancing(self, ans: list[int]):
        if self.__root.get_right() == self.__root:
        #    print('empty!')
            return True
        
        head = self.__root.get_right()
        while head != self.__root:
            if head.get_below() == head:
            #    print('not covered')
                return False
            head = head.get_right()

        not_ans = set()
        head = self.__root.get_right()
        while head != self.__root:
        #    print('remove col head', head.get_loc()[1])
            self.remove(head)
            current = head.get_below()
            while current != head:
                if current.get_loc()[0] in not_ans:
                    current = current.get_below()
                    continue
                ans.append(current.get_loc()[0])
                removed = []
                node = current.get_right()
            #    print('remove row', current.get_loc()[0])
                while node != current:
                    removed.append(node.get_head())
                    self.remove(node.get_head())
                    node = node.get_right()
                if self.dancing(ans):
                    return True
            #    print('recover row', current.get_loc()[0])
                while len(removed) > 0:
                    self.recover(removed.pop())
                not_ans.add(ans.pop())
                current = current.get_below()
        #    print('recover col head', head.get_loc()[1])
            self.recover(head)
            head = head.get_right()
        return False

    def __str__(self) -> str:
        arr = np.zeros((self.__shape[0] + 1, self.__shape[1]), int)
        for c in range(self.__shape[1]):
            arr[0, c] = -1
        head = self.__root.get_right()
        while head != self.__root:
            arr[head.get_loc()[0] + 1, head.get_loc()[1]] = head.get_loc()[1]
        #    if head in self.__stack_of_removed:
        #        head = head.get_right()
        #        continue
            current = head.get_below()
            while current != head:
                arr[current.get_loc()[0] + 1, current.get_loc()[1]] = 1
                current = current.get_below()
            head = head.get_right()
        out = str(arr)
        return out[:out.index('\n')].replace('-1', ' _') + out[out.index('\n'):].replace('0', '.')



    
