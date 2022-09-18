
>Trie树计算前缀的模板

```cpp
class Trie {
    vector<Trie*> next;
    int cnt;
public:
    Trie() : next(26), cnt(0){}
    Trie* find(const string& s) {
        Trie* node = this;
        for (auto c : s) if (!node) node = node->next[c-'a']; else break;
        return node;
    }

    void insert(const string& s) {
        Trie* node = this;
        for (auto c : s) {
            if (!node->next[c-'a']) node->next[c-'a'] = new Trie();
            node = node->next[c-'a'];
            node ->cnt++;
        }
    }

    int sumCnt(const string& s) {
        int sum = 0;
        Trie* node = this;
        sum += node->cnt;
        for (auto c : s) {
            node = node->next[c-'a'];
            if (node) sum += node->cnt; else break;
        }
        return sum;
    }
};
```

具体使用参考 [6183. 字符串的前缀分数和](https://leetcode.cn/problems/sum-of-prefix-scores-of-strings/)

```cpp
class Solution {
    class Trie {
        vector<Trie*> next;
        int cnt;
    public:
        Trie() : next(26), cnt(0){}
        Trie* find(const string& s) {
            Trie* node = this;
            for (auto c : s) if (!node) node = node->next[c-'a']; else break;
            return node;
        }

        void insert(const string& s) {
            Trie* node = this;
            for (auto c : s) {
                if (!node->next[c-'a']) node->next[c-'a'] = new Trie();
                node = node->next[c-'a'];
                node ->cnt++;
            }
            //node ->cnt++;
        }

        int sumCnt(const string& s) {
            int sum = 0;
            Trie* node = this;
            sum += node->cnt;
            for (auto c : s) {
                node = node->next[c-'a'];
                if (node) sum += node->cnt; else break;
            }
            return sum;
        }
    };
public:
    vector<int> sumPrefixScores(vector<string>& words) {
        Trie* t = new Trie();
        for (auto& s : words)  t->insert(s);

        int i = 0;
        vector<int> ans(words.size());

        for (auto& s : words)  ans[i++] = t->sumCnt(s);

        return ans;
    }
};
```