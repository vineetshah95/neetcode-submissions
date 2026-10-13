/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */

class Solution {
    public ListNode reverseList(ListNode head) {
        ListNode current = head;
        ListNode previous = null;

        while(current != null){
            //SAVE
            ListNode next = current.next;
            //REVERSE
            current.next=previous;
            //MOVE PREVIOUS
            previous = current;
            //MOVE CURRENT
            current = next;
        }
        return previous;
    }
}
