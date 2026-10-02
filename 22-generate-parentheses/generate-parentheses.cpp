class Solution {
public:
    vector<string> generateParenthesis(int n) {
        vector<string> result;
        backtrack("", 0, 0, n, result);
        return result;
    }

private:
    void backtrack(string current, int open, int close, int max, vector<string>& result) {
        if (current.length() == max * 2) {
            result.push_back(current);
            return;
        }

        if (open < max)
            backtrack(current + "(", open + 1, close, max, result);
        if (close < open)
            backtrack(current + ")", open, close + 1, max, result);
    }
};
        
   