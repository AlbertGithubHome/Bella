

//打印当前调用堆栈，默认获取堆栈深度为12层，目前只有Windows版本实现
void PrintTraceStack(char* szBriefInfo = NULL);


#ifdef WIN32
#include "windows.h"
#include "dbghelp.h"
void PrintTraceStack(char* szBriefInfo /*= NULL*/)
{
    static const int MAX_STACK_FRAMES = 12;
    void *pStack[MAX_STACK_FRAMES];
    static char szStackInfo[COMMON_CLIENT_MSG_LEN_1024 * MAX_STACK_FRAMES];
    static char szFrameInfo[COMMON_CLIENT_MSG_LEN_2048];

    HANDLE process = GetCurrentProcess();
    SymInitialize(process, NULL, TRUE);
    WORD frames = CaptureStackBackTrace(0, MAX_STACK_FRAMES, pStack, NULL);
    strcpy(szStackInfo, szBriefInfo == NULL ? "stack traceback:\n" : szBriefInfo);

    for (WORD i = 0; i < frames; ++i) {
        DWORD64 address = (DWORD64)(pStack[i]);

        DWORD64 displacementSym = 0;
        char buffer[sizeof(SYMBOL_INFO)+MAX_SYM_NAME * sizeof(TCHAR)];
        PSYMBOL_INFO pSymbol = (PSYMBOL_INFO)buffer;
        pSymbol->SizeOfStruct = sizeof(SYMBOL_INFO);
        pSymbol->MaxNameLen = MAX_SYM_NAME;

        DWORD displacementLine = 0;
        IMAGEHLP_LINE64 line;
        //SymSetOptions(SYMOPT_LOAD_LINES);
        line.SizeOfStruct = sizeof(IMAGEHLP_LINE64);

        if (SymFromAddr(process, address, &displacementSym, pSymbol) && SymGetLineFromAddr64(process, address, &displacementLine, &line))
        {
            snprintf(szFrameInfo, sizeof(szFrameInfo), "\t%s() at %s:%d(0x%x)\n", pSymbol->Name, line.FileName, line.LineNumber, pSymbol->Address);
        }
        else
        {
            snprintf(szFrameInfo, sizeof(szFrameInfo), "\terror: %d\n", GetLastError());
        }
        strcat(szStackInfo, szFrameInfo);
    }
    CFS_FILELOGS::WriteLog(log_type_error, szStackInfo);
#else
void PrintTraceStack(char* szBriefInfo /*= NULL*/)
{
    CFS_FILELOGS::WriteLog(log_type_error, "%s: PrintTraceStack function is unrealized on this operating system\n",
        szBriefInfo == NULL ? "stack traceback" : szBriefInfo);
#endif // WIN32
}