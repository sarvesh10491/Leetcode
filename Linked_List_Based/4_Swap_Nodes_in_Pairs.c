/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */


struct ListNode* swapPairs(struct ListNode* head){
    if(!head || !head->next)    // Case : if there are less than 2 nodes in list
        return head;
    
    struct ListNode *tr, *cur, *new_cur, *ans; 
        
    tr = malloc(sizeof(struct ListNode));   // Temporary node that acts as starting node of list during operation. We will exclude this in end.
    tr->next = head;
    cur = head;
    ans = head->next;   // 2nd node will be head of final swapped list which we will return
    
    while(tr->next && tr->next->next){      // Check if new pair of nodes are available to swap in every iteration
        tr->next = cur->next;               // Connect already swapped list tail with next head of next pair
        new_cur = cur->next->next;          // Set new cur pointer of next pair
        cur->next->next = cur;              // Swap direction of current pair
        cur->next = new_cur;                // Make cur pointer which is tail of latest swapped pair point to head of next pair
        tr = tr->next->next;                // Move tracker by 2 nodes to point to tail of swapped list so far
        cur = cur->next;                    // Restore cur pointer to new cur pointer in next pair
    }
    
    return ans;
}