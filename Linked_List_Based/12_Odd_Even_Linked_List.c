/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */


struct ListNode* oddEvenList(struct ListNode* head){
    if(!head) return NULL;
    
    struct ListNode *l1, *l2, *head2;
    l1 = head;
    l2 = head->next;
    head2 = l2;     // Store starting node of even node's list
    
    while(l2 && l2->next){
        l1->next = l2->next;        // Update odd node to point to next odd node
        l2->next = l2->next->next;  // Update even node to point to next even node
        l1 = l1->next;
        l2 = l2->next;
    }
    
    l1->next = head2;   // Point last node of odd node's list to even node's list's start
    
    return head;
}