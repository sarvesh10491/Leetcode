/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */


struct ListNode* removeNthFromEnd(struct ListNode* head, int n){
    if(!head->next)     // Case : Only 1 node in list
        return NULL;
    
    if(!head->next->next){      // Case : 2 nodes in list
        if(n==1){
            head->next = NULL;
            return head;
        }
        else{
            return head->next;
        }
    }
        
    
    struct ListNode *front, *rear;
    front = head;
    rear = head;
    
    while(n>0){     // Move front ptr n distance away from rear ptr
        front = front->next;
        n--;
    }
    if(!front)      // Case : front ptr is already at end of list => n==list element count
        return head->next;
        
    while(front->next){     // Move front ptr till end with same speed as rear ptr
        front = front->next;
        rear = rear->next;
    }
    rear->next = rear->next->next;      // Remove rear->next node which is nth from end
    
    
    return head;
}