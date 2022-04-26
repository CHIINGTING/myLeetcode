/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode* removeElements(struct ListNode* head, int val){
    struct ListNode **current = &head;
    while(*current){
        if((*current)->val == val){
            *current = (*current) -> next;
        }
        else
            current = &(*current) -> next;
    }
    return head;
}
