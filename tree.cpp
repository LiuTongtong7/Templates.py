void preorder(TreeNode* root) {
    if (root == NULL)
        return;
    TreeNode *curr;
    stack<TreeNode*> st;
    st.push(root);
    while (!st.empty()) {
        curr = st.top();
        st.pop();
        visit(curr); // TODO
        if (curr->right)
            st.push(curr->right);
        if (curr->left)
            st.push(curr->left);
    }
}

void preorder(TreeNode* root) {
    TreeNode *curr = root;
    stack<TreeNode*> st;
    while (curr) {
        visit(curr);
        if (curr->right)
            st.push(curr->right);
        curr = curr->left;
        if (curr == NULL && !st.empty()) {
            curr = st.top();
            st.pop();
        }
    }
}

void inorder(TreeNode* root) {
    TreeNode *curr = root;
    stack<TreeNode*> st;
    while (curr != NULL || !st.empty()) {
        while (curr != NULL) {
            st.push(curr);
            curr = curr->left;
        }
        curr = st.top();
        st.pop();
        visit(curr); // TODO
        curr = curr->right;
    }
}

void morris(TreeNode* root) {
    TreeNode *curr = root, *prev = NULL;
    while (curr != NULL) {
        if (curr->left == NULL) {
            visit(curr); // TODO
            curr = curr->right;
        } else {
            prev = curr->left; // curr's predecessor
            while (prev->right != NULL && prev->right != curr)
                prev = prev->right;
            if (prev->right == NULL) {
                prev->right = curr;
                curr = curr->left;
            } else {
                prev->right = NULL;
                visit(curr); // TODO
                curr = curr->right;
            }
        }
    }
}

void postorder(TreeNode* root) {
    TreeNode *curr = root, *prev = NULL;
    stack<TreeNode*> st;
    while (curr != NULL || !st.empty()) {
        while (curr != NULL) {
            st.push(curr);
            curr = curr->left;
        }
        curr = st.top();
        if (curr->right != NULL && curr->right != prev) {
            curr = curr->right;
        } else {
            visit(curr); // TODO
            st.pop();
            prev = curr;
            curr = NULL;
        }
    }
}

void levelorder(TreeNode* root) {
    if (root == NULL)
        return;
    TreeNode* curr;
    queue<TreeNode*> qu;
    qu.push(root);
    while (!qu.empty()) {
        curr = qu.front();
        qu.pop();
        visit(curr); // TODO
        if (curr->left)
            qu.push(curr->left);
        if (curr->right)
            qu.push(curr->right);
    }
}
