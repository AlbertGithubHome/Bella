// testMapBracket.cpp : 定义控制台应用程序的入口点。
//

#include <map>
#include <iostream>
#include <algorithm>
using namespace std;

class CReportCard
{
public:
    CReportCard() { m_mapStuNo2Score.clear(); }
    ~CReportCard() { m_mapStuNo2Score.clear(); }
public:
    void LoadScores(); // 模拟录入成绩
    int  GetScoreByStudentNo(const int nStudentNo); // 根据学号查询成绩
    void PrintReportCard(); // 打印成绩单
private:
    map<int, int> m_mapStuNo2Score;
};

void CReportCard::LoadScores()
{
    m_mapStuNo2Score[1001] = 99;
    m_mapStuNo2Score[1002] = 94;
    m_mapStuNo2Score[1004] = 89;
    m_mapStuNo2Score[1005] = 92;
    m_mapStuNo2Score[1007] = 80;
}

int CReportCard::GetScoreByStudentNo(const int nStudentNo)
{
    //return m_mapStuNo2Score[nStudentNo];
    map<int, int>::const_iterator itor = m_mapStuNo2Score.find(nStudentNo);
    return itor != m_mapStuNo2Score.end() ? itor->second : 0;
}

void CReportCard::PrintReportCard()
{
    cout << "show report card start----->" << endl;
    std::for_each(m_mapStuNo2Score.begin(), m_mapStuNo2Score.end(), [](std::map<int, int>::reference socrepair) 
    {
        std::cout << socrepair.first << "'s score = " << socrepair.second << "\n";
    });
    cout << "show report card end<------" << endl;
}

int main(int argc, char* argv[])
{
    CReportCard obj;
    obj.LoadScores();

    cout << "student no = 1001, score = " << obj.GetScoreByStudentNo(1001) << endl;
    cout << "student no = 1004, score = " << obj.GetScoreByStudentNo(1004) << endl;

    obj.PrintReportCard();

    cout << endl;
    cout << "student no = 1011, score = " << obj.GetScoreByStudentNo(1011) << endl;
    cout << "student no = 1014, score = " << obj.GetScoreByStudentNo(1014) << endl;

    obj.PrintReportCard();

    return 0;
}

