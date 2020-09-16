/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */


struct ListNode* mergeTwoLists(struct ListNode* l1, struct ListNode* l2){
    // Create a temporary node that acts as starting node of merged list. We will exclude this in end.
    // Create a tracker pointer that will move ahead in every merge iteration to track end node of list.
    struct ListNode *tmp, *tr;
    tmp = malloc(sizeof(struct ListNode));
    tr = tmp;
    
    while(l1 && l2){    // while there are valid nodes in both lists
        if(l1->val < l2->val){      // Case : current List 1 node value is smaller than current List 2 node value
            tr->next =  l1;         // Make next of current end of merged list(i.e. tr) point to latest smaller node(i.e. l1)
            l1 = l1->next;          // Move latest smaller node pointer(i.e. l1) to next node
        }
        else{                       // Case : current List 2 node value is smaller than or equal to current List 1 node value
            tr->next = l2;          // Make next of current end of merged list(i.e. tr) point to latest smaller node(i.e. l2)
            l2 = l2->next;          // Move latest smaller node pointer(i.e. l2) to next node
        }
        tr = tr->next;              // Move tracker pointer to next node which will be updated end of merged list till that iteration
    }
    
    tr->next = l1 ? l1 : l2;        // Case : when one of l1 or l2 is NULL, Make next of current end of merged list(i.e. tr) point to remaining list
    
    return tmp->next;               // Restore temporary node which was placeholder starting node & return next node of it from where required merged list starts.
}