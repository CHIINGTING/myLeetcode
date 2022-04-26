/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode* removeElements(struct ListNode* head, int val){
    struct ListNode **current = &head;
    struct ListNode * deleteNode;

    while(*current){
        while((*current)->val == val){
            deleteNode = *current;
            *current = (*current) -> next;
            free(deleteNode);
            if(!*current){
                return head;
            }
            
        }
        current = &(*current)->next;
    }
    return head;
}
