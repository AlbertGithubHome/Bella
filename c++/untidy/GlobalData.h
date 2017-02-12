#pragma once

#include "stdafx.h"

#include <stdio.h>
#include <memory.h>
#include <Windows.h> 
#include <winsock.h>

//#include "AInterface.h"
//#include "AThread.h"
//#include "ARingBuffer.h"
//#include "AServer.h"

#pragma comment(lib, "ws2_32.lib") 

#define MAX_LENGTH	1024

// resault
#define INVALID_VALUE	-1
#define SUCCESS_VALUE	0

// data size
#define KB	1024
#define MB	1024 * KB
#define GB	1024 * MB

// size for ring buffer 
#define RB_SPACE	2
#define PACK_HEADER_SIZE	SIZEOF_DWORD_SIZE	

// all kinds of size
#define SIZEOF_BYTE_SIZE	sizeof(BYTE)
#define SIZEOF_WORD_SIZE	sizeof(WORD)
#define SIZEOF_DWORD_SIZE	sizeof(DWORD)

#define SIZEOF_CHAR_SIZE	sizeof(char)
#define SIZEOF_SHORT_SIZE	sizeof(short)
#define SIZEOF_INT_SIZE		sizeof(int)
#define SIZEOF_LONG_SIZE	sizeof(long)

typedef	unsigned char	BYTE;
typedef unsigned short	WORD;
typedef unsigned long	DWORD;



