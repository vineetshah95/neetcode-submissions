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
       ListNode previous = null;
       ListNode current = head;

       while (current != null){
            //Save
            ListNode next = current.next;
            //Reverse
            current.next = previous;
            //Change Previous
            previous = current;
            //Change current
            current = next;
       }
       return previous;
    }
}
