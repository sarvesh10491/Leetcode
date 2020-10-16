/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */


struct ListNode* rotateRight(struct ListNode* head, int k){
    if(!head || !head->next)    // If list is empty or has only 1 node
        return head;
    
    int cnt=0;
    struct ListNode *cur, *tail;
    cur = head;

    while(cur){                 // Locate tail of original list & total no. of nodes in list
        tail = cur;
        cur = cur->next;
        cnt++;
    }
    
    int move = cnt-(k%cnt);     // In case if k is larger than total no. of nodes, we take mod of those two to decide required moves since it gets wrapped around
    cnt = 0;
    cur = head;                 // bring cur back to current list head
    
    while(cnt < move-1){        // while move forward in list is valid for rotation
        cur = cur->next;        // we move cur to next node
        cnt++;                  // and increase cnt to track untill we pass nodes required to be rotated
    }

    tail->next = head;          // make tail point to head of original list which will make it attached at end
    head = cur->next;           // cur->next will be new head of answer list
    cur->next = NULL;           // cur which is now last node of answer list will point to NULL

    return head;
}