/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode* removeElements(struct ListNode* head, int val){
    struct ListNode **current = &head;
    if(!*current){
        return NULL;
    }
    while(*current  &&(*current)->val == val){
        *current = (*current) -> next;
    }
    
    while((*current) && (*current)->next ){
        while(((*current)->next)&&((*current)->next->val == val)){
            (*current) -> next = (*current) -> next -> next;
        }
        current = &(*current)->next;
    }
    return head;
}
