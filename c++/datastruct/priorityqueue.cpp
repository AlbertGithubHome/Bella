#include <iostream>
#include <queue>
using namespace std;


struct student {
    string name;
    int score;
};

struct cmp_custom {
    bool operator()(student& x, student& y) {
        return x.score > y.score;
    }
};

void max_k_score()
{
    vector<student> stu_list = {{"Andy", 89}, {"Bella", 79}, {"Cary", 92}, {"Dick", 60}, {"Ray", 70}};
    int k = 3;

    priority_queue<student, vector<student>, cmp_custom> q;
    for (auto stu : stu_list) {
        if (q.size() == k) {
            if (stu.score > q.top().score) {
                q.pop();
                q.push(stu);
            }
        }
        else q.push(stu);
    }

    while (!q.empty()) {
        cout << q.top().name << ":" << q.top().score << endl;
        q.pop();
    }
}

void max_k_score_2()
{
    vector<student> stu_list = {{"Andy", 89}, {"Bella", 79}, {"Cary", 92}, {"Dick", 60}, {"Ray", 70}};
    int k = 3;

    auto cmp = [](student& x, student& y) { return x.score > y.score; };
    priority_queue<student, vector<student>, decltype(cmp)> q(cmp);
    for (auto stu : stu_list) {
        if (q.size() == k) {
            if (stu.score > q.top().score) {
                q.pop();
                q.push(stu);
            }
        }
        else q.push(stu);
    }

    while (!q.empty()) {
        cout << q.top().name << ":" << q.top().score << endl;
        q.pop();
    }
}

void max_k_num()
{
    int source_data[10] = {3, 5, 8, 1, 10, 2, 9, 15, 13, 16};
    int k = 5;

    priority_queue<int, vector<int>, greater<int>> q;
    for (auto n : source_data) {
        if (q.size() == k) {
            if (n > q.top()) {
                q.pop();
                q.push(n);
            }
        }
        else q.push(n);
    }

    while (!q.empty()) {
        cout << q.top() << endl;
        q.pop();
    }
}

void common_sort()
{
    int source_data[10] = {3, 5, 8, 1, 10, 2, 9, 15, 13, 16};
    priority_queue<int> q;
    for (auto n : source_data) q.push(n);

    while (!q.empty()) {
        cout << q.top() << endl;
        q.pop();
    }
}


int main(int argc, char* argv[])
{
    max_k_score();
    max_k_score_2();

    cout << "max_k_num" << endl;

    max_k_num();

    cout << "common_sort" << endl;

    common_sort();

    return 0;
}