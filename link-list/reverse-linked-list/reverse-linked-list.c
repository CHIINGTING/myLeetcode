/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */


struct ListNode* reverseList(struct ListNode* head){
    struct ListNode* ptr = head;
    struct ListNode* pre=NULL;
    struct ListNode* temp=NULL;
    while(ptr){
        temp = ptr->next;
        ptr->next = pre;
        pre = ptr;
        ptr = temp;
    }
    return pre;
}