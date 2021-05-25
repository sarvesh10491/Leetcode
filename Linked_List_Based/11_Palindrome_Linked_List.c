/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */


bool isPalindrome(struct ListNode* head){
    struct ListNode *p,*c,*n,*f;
    p = NULL;
    c = head;
    n = head->next;
    f = c;
    
    if(!head) return false;  // no nodes in list
    if(!head->next) return true;    // 1 node in list
    if(!head->next->next){  // 2 nodes in list
        if(head->val == head->next->val) return true;
        else return false;
    }
    
    while(f && f->next){    // Reverse list till middle node
        f = f->next->next;
        c->next = p;
        p = c;
        c = n;
        n = n->next;
    }
    if(f)   // If odd no. of nodes in list, middle node can be skipped.
        c = n;
    
    while(c && p){  // Compare late of list from middle node with 1st half for matching values (1st is reversed already in previous step)
        if(c->val != p->val)
            return false;
        c = c->next;
        p = p->next;
    }
    return true;
}