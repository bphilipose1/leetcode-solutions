/*
// Definition for a Node.
class Node {
public:
    int val;
    vector<Node*> neighbors;
    Node() {
        val = 0;
        neighbors = vector<Node*>();
    }
    Node(int _val) {
        val = _val;
        neighbors = vector<Node*>();
    }
    Node(int _val, vector<Node*> _neighbors) {
        val = _val;
        neighbors = _neighbors;
    }
};
*/

class Solution {
public:
    unordered_map<Node*, Node*> visited;
    Node* cloneGraph(Node* node) {
        if (!node)  { //if we run out mimic the nullptr edge
            return nullptr;
        }

        //we alrady worked on this node and stored the clone, just re-return the clone
        if(visited.count(node)) { //exitance check
            return visited[node];
        }

        //duplicate the current node we are on
        Node* clone = new Node(node->val);
        visited[node] = clone; //store the reference of the new node

        for(Node* neighbor: node->neighbors)//coppy the references that go out from the new cloned node
            clone->neighbors.push_back(cloneGraph(neighbor));
        return clone;
    }
};