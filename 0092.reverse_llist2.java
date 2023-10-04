class Solution {
    public ListNode reverseBetween(ListNode head, int m, int n) {
        int count = 0;
        ListNode l1 = null, l2 = null, curr = head, prev = null;
        boolean flag = false;
        while (curr != null) {
            count++;
            if (count == m) {
                l1 = prev;
                l2 = curr;
                flag = true;
            }
            if (count == n + 1) {
                break;
            }
            if (flag) {
                ListNode temp = curr.next;
                curr.next = prev;
                prev = curr;
                curr = temp;
            } else {
                prev = curr;
                curr = curr.next;
            }
        }

        if (l1 != null) {
            l1.next = prev;
        } else {
            head = prev;
        }
        l2.next = curr;
        return head;
    }
}