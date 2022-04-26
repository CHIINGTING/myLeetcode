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
    while(*current){
        while((*current)->val == val){
            *current = (*current) -> next;
            if(!*current){
                return head;
            }
        }
        current = &(*current)->next;
    }
    return head;
}
