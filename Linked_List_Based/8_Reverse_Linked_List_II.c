/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */


struct ListNode* reverseBetween(struct ListNode* head, int m, int n){
    if(!head || !head->next)    // If list is empty or has only 1 node
        return head;
    
    struct ListNode *dummy;
    dummy = malloc(sizeof(struct ListNode));
    dummy->next = head;
    
    struct ListNode *pre, *cur, *nxt, *tail1, *tail2;   // Create 3 pointers pointing to below nodes & 2 tail tracking pointers for inbetween list
    pre = dummy;
    cur = head;
    nxt = head->next;
    
    int diff = n-m+1;
    if(diff==1)         // If m==n, we need not do any computation 7 return list as is
        return head;
    
    while(m>1){         // Traverse list without making any changes untill we reach m
        pre = pre->next;
        cur = cur->next;
        nxt = nxt->next;
        m--;
    }
    tail1 = pre;        // pre will be tail of unchanged list at beginning
    tail2 = cur;        // cur will be tail of reversed list inbetween
    
    while(diff>0 && nxt){   // While nxt is valid & diff is valid, keep reversing list decrementing diff
        cur->next = pre;
        pre = cur;
        cur = nxt;
        nxt = nxt->next;
        diff--;
    }
    if(diff!=0){            // If we exited because nxt was NULL but diff is not, means we have 1 last node to be reversed before return
        cur->next = pre;
        pre = cur;
        cur = nxt;
    }
    tail1->next = pre;      // tail of unchanged list at beginning points to pre which is head of reversed list
    tail2->next = cur;      // tail of reversed list points to cur which is head of remaining list at end
    
    return dummy->next;
}