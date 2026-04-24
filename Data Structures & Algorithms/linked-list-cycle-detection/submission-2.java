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
    public boolean hasCycle(ListNode head) {
        ListNode temp = head;
        ListNode Slow = head;
        ListNode Fast = head;
        while(Fast != null && Fast.next != null){
            Slow = Slow.next;
            Fast = Fast.next.next;
            if (Slow == Fast) return true;

        }
        return false;
    }
}
