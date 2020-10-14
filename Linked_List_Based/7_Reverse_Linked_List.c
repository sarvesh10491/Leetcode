/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */


struct ListNode* reverseList(struct ListNode* head){
    if(!head)           // If list is empty
        return NULL;
        
    struct ListNode *p, *c, *n;     // Create 3 pointers pointing to NULL/below nodes.
    p = NULL;
    c = head;
    n = head->next;
    
    while(n){           // while leading pointer n is not NULL
        c->next = p;    // Reverse direction of current node
        p = c;          // Move trailing pointer to current
        c = n;          // Move current pointer to next node which is also pointed by n
        n = n->next;    // Move leading pointer to next node
    }
    c->next = p;        // when current pointer is at last node here, reverse direction for last node pair & return current as new head of answer list
    return c;
}