class Solution {
public:
    vector<long long> resultArray(vector<int>& nums, int k) {
        vector<long long> res(k), cur(k), nxt(k);
        for (int v : nums) {
            int r = v % k;
            fill(nxt.begin(), nxt.end(), 0);
            for (int x = 0; x < k; ++x)
                nxt[x * r % k] += cur[x];
            nxt[r]++;
            cur = nxt;
            for (int x = 0; x < k; ++x)
                res[x] += cur[x];
        }
        return res;
        
    }
};