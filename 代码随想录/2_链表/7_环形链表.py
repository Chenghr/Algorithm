"""
    题目描述:
        给定一个链表的头节点  head ，返回链表开始入环的第一个节点。 
        如果链表无环，则返回 null。

        如果链表中有某个节点，可以通过连续跟踪 next 指针再次到达，则链表中存在环。 
        为了表示给定链表中的环，评测系统内部使用整数 pos 来表示链表尾连接到链表中的位置（索引从 0 开始）。
        如果 pos 是 -1，则在该链表中没有环。
        
        注意: pos 不作为参数进行传递，仅仅是为了标识链表的实际情况。

        不允许修改 链表。

    链接: https://leetcode-cn.com/problems/linked-list-cycle-ii
"""

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        """
            TODO: Redo again

            经典的快慢指针题目。

            判断是否有环:
                fast 指针前进速度是 slow 指针的两倍；
                如果 fast 与 slow 相遇，则有环；
                fast 走到终点，则无环。

            确定环的入口:
                假设从头结点到环形入口节点的节点数为 x; 
                环形入口节点到 fast 指针与 slow 指针相遇节点节点数为 y;
                从相遇节点再到环形入口节点节点数为 z; 
                
                则:
                    (x + y) * 2 = x + y + n*(y + z)
                
                要求的是 x, 因此有:
                    x = (n-1)*(y+z) + z, n >= 1

                n = 1 时，公式就化简为 x = z；
                    意味着 从头结点出发一个指针，从相遇节点 也出发一个指针，这两个指针每次只走一个节点， 
                    那么当这两个指针相遇的时候就是 环形入口的节点。
                
                n > 1 时，fast指针在环形转n圈之后才遇到 slow指针。
            
                因此我们通过如下方式找到环的入口:
                    从头结点出发一个指针，从相遇节点 也出发一个指针，这两个指针每次只走一个节点， 
                    当这两个指针相遇的时候就是 环形入口的节点。
                
        """
        fast, slow = head, head

        while fast != None and fast.next != None:
            # 判断是否有环，注意此处还要对于 fast.next 进行判断
            fast = fast.next.next
            slow = slow.next

            if fast == slow:
                break
        
        if fast == None or fast.next != None:
            return None
        
        slow = head

        while fast != slow:
            fast = fast.next
            slow = slow.next

        return slow