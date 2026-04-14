/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        ListNode* root = new ListNode;
        ListNode* temp = root;
        ListNode* num1 = l1;
        ListNode* num2 = l2;
        int carry = 0;
        int count = 0;
        int total = 0;

        int temp1, temp2;
        while(num1 != nullptr || num2 != nullptr || carry != 0)   {
            if(temp == root && count == 0)  {
                count++;
            }
            else if(temp != root || count != 0)    {
                temp->next = new ListNode();
                temp = temp->next;
            }
            
            if(num1 == nullptr) {
                temp1 = 0;
            }
            else    {
                temp1 = num1->val;
            }
            if(num2 == nullptr) {
                temp2 = 0;
            }
            else    {
                temp2 = num2->val;
            }

            if((temp1 + temp2 + carry) >= 10)   {
                temp->val = (temp1 + temp2 + carry) % 10;
                carry = 1;
            }
            else    {
                temp->val = (temp1 + temp2 + carry);
                carry = 0;
            }

            if(num1 != nullptr) {
                num1 = num1->next;
            }
            if(num2 != nullptr)
                num2 = num2->next;
        }
        return root;
    }
};