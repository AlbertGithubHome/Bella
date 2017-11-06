#include <fstream>
#include <string.h>
using namespace std;

#define COMMON_SERVER_STRING_LENGTH_512 512

int main()
{
    ofstream logfile("./logs/players_distribution.txt", ios::out);
    if (!logfile)
    {
        printf("open failed!\n");
        return 0;
    }

    // 先输出表头
    const char szHeaderInfo[COMMON_SERVER_STRING_LENGTH_512] = "PlayerUID\tAccoutName\tRoleName\tWorldIndex\tMapId\tWorldName\n";
    logfile.write((const char *)szHeaderInfo, strlen(szHeaderInfo));
    // LogDebug(szHeaderInfo);

    const char szOuputTemplate[COMMON_SERVER_STRING_LENGTH_512] = "%d\t%s\t%s\t%d\t%d\t%s\n";
    char szOutputBuffer[COMMON_SERVER_STRING_LENGTH_512] = {0};
    for (int nPlayerIndex = 0; nPlayerIndex < 10; ++nPlayerIndex)
    {
        snprintf(szOutputBuffer, sizeof(szOutputBuffer), szOuputTemplate,
            nPlayerIndex,
            "AccountName",
            "PlayerName",
            1,
            2,
            "g_SubWorld[nSubWorldIndex].GetBaseMapInfo()->GetMapName()");
        szOutputBuffer[COMMON_SERVER_STRING_LENGTH_512 - 1] = '\0';


        // 写入内容
        logfile.write((const char *)szOutputBuffer, strlen(szOutputBuffer));
        // LogDebug(szOutputBuffer);
    }

    // 关闭文件
    logfile.close();
    return 0;
}