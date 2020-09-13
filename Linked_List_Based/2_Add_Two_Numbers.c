/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */

// In place addition implementation
//-----------------------------------
struct ListNode* addTwoNumbers(struct ListNode* l1, struct ListNode* l2){
    struct ListNode *ans, *end;     // ans for answer list head, end for tracking end of answer list
    ans = l2;   // l2 will be used to store addition results for return
    
    int sum=0, carry=0;
    
    while(l1->next && l2->next){    // Loop till both lists have digits & break on last position where both lists have digits
        sum = l1->val + l2->val + carry;
        if(sum>9){
            sum = sum%10;
            carry = 1;
        }
        else
            carry = 0;
        
        l2->val = sum;
        end = l2;
        l1 = l1->next;
        l2 = l2->next;
    }
    
    if(!l2->next){     // If l2 list is smaller than l1 list, append l1 list to l2 to sum up remaining extra digits
        l2->next = l1->next;
    }
    
    sum = l1->val + l2->val + carry;    // Adding last common position digits for both lists
    if(sum>9){
        sum = sum%10;
        carry = 1;
    }
    else
        carry = 0;
    
    l2->val = sum;
    end = l2;
    l2 = l2->next;
    
    while(l2){      // Continue with remaining extra elements from bigger list
        sum = l2->val + carry;
        if(sum>9){
            sum = sum%10;
            carry = 1;
        }
        else
            carry = 0;
        
        l2->val = sum;
        end = l2;
        l2 = l2->next;
    }
    
    if(carry){      // If last node digit + carry is >10, add new node to accomodate additional carry digit
        struct ListNode *added;
        added = malloc(sizeof(struct ListNode));
        added->val = 1;
        added->next = NULL;
        end->next = added;
    }
    
    return ans;
}