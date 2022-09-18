
>Trie树模板，可用于查找单词是否存在

```cpp
class Trie {
    vector<Trie*> next;
    bool end;

    Trie* find(const string& s) {
        Trie* node = this;
        for (auto& c : s) {
            if (node) node = node->next[c-'a'];
            else break;
        }
        return node;
    }

public:
    Trie() : next(26), end(false) {
    }

    void insert(const string& word) {
        Trie* node = this;
        for (auto& c : word) {
            if (!node->next[c-'a']) node->next[c-'a'] = new Trie();
            node = node->next[c-'a'];
        }
        node->end = true;
    }

    bool search(const string& word) {
        Trie* node = find(word);
        return node && node->end;
    }

    bool startsWith(const string& prefix) {
        Trie* node = find(prefix);
        return !!node;
    }
};
```