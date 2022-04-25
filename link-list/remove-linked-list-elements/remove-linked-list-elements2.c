/*
1. if head is remove: preptr is NULL
2. if node is remove: preptr -> next = ptr->next
*/

/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode* removeElements(struct ListNode* head, int val){
    struct ListNode* ptr = head;
    struct ListNode* preptr=NULL;
    while(ptr){
        if(ptr -> val == val){
            if(!preptr){
                head = head->next;
                ptr = head;
            }
            else{
                preptr -> next = ptr -> next;
                ptr = ptr -> next;
            }
        }
        else{
            preptr = ptr;
            ptr = ptr -> next;
        }

    }
    return head;
}
