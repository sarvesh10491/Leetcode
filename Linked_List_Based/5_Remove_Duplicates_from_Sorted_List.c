/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */


struct ListNode* deleteDuplicates(struct ListNode* head){
    if(!head || !head->next)
        return head;
    
    struct ListNode *pre, *cur;     // Set 1st node as pre & 2nd as cur
    pre = head;
    cur = head->next;
    
    while(cur){
        if(cur->val == pre->val)    // If cur is same node as pre, set pre next to next node of cur node
            pre->next = cur->next;
        else                        // If new node than pre node, set pre to this node
            pre = cur;
        
        cur = cur->next;
    }
    
    return head;
}