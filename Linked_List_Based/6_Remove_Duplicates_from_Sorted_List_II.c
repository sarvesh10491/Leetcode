/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */

struct ListNode* deleteDuplicates(struct ListNode* head){
    if(!head || !head->next)    // If list has only 1 node or is empty, return as is
        return head;
    
    struct ListNode *dummy;     // dummy node to act as placeholder before head node. dummy->next will serve as head of final answer list
    dummy = malloc(sizeof(struct ListNode));
    dummy->next = head;
        
    struct ListNode *pre, *cur, *lastdup;
    pre = dummy;
    cur = head;
    
    while(cur && cur->next){                // Check if we have valid pair of nodes available to compare
        if(cur->val == cur->next->val){     // If pair of nodes as duplicates, we keep checking for how long dup nodes streak is
            lastdup = cur->next;
            while(lastdup->next && lastdup->next->val == lastdup->val){
                lastdup = lastdup->next;
            }
            cur = lastdup->next;            // Once we come out current dup nodes streak, set cur to first non-dup node & pre->next point to this which removes all dup nodes we've seen
            pre->next = cur;
        }
        else{                               // If no dup nodes in pair, keep moving ahead by 1 node
            pre = cur;
            cur = cur->next;
        }
    }
    return dummy->next;
}