print("\nexample 1:");
data_table = {a = 1, b = 2, 3, 4, 5, 6};
function filter(data_tb)
    for k,v in pairs(data_tb) do
        if v % 2 == 0 then
            data_tb[k] = nil;
        end
    end
end

-- 过滤掉偶数
filter(data_table);
for k,v in pairs(data_table) do
    print(k,v)
end

--[[
example 1:
1   3
3   5
a   1
]]

print("\nexample 2:");
data_table = {a = 1, b = 2, 3, 4, 5, 6};
function destroy(data_tb)
    data_tb = {};
end

-- 销毁整个表
destroy(data_table);
for k,v in pairs(data_table) do
    print(k,v)
end

--[[
example 2:
1   3
2   4
3   5
4   6
b   2
a   1
]]

--[[ C++
#include <iostream>
using namespace std;


void change_string(char* pStr)
{
    pStr[0] = '5';
    pStr[1] = '0';

    pStr = "only test\n";
}

int main()
{
    char szContent[32] = "help";
    
    change_string(szContent);
    cout << szContent << endl;

    return 0;
}

50lp
]]

print("\nexample 3:");
function counter()
    local count = 0;
    return function()
        count = count + 1;
        return count;
    end
end

func = counter();
print(func());
print(func());
print(func());
--[[
example 3:
1
2
3
]]

print("\nexample 4:");
local t1 = {i = 1};
local t2 = t1;
t1.i = 666;
print(t2.i)
--[[
example 4:
666
]]

print("\nexample 5:");
local t1 = {i = 1};
local t2 = t1;
t1 = {i = 11};
print(t2.i)
--[[
example 5:
1
]]

--下面开始进入正题
print("\nexample 6:");
local tb = {i= 1};

function outer()
    return function()
        local t = tb;
        print(t.i);
    end
end

local show = outer();
tb = {i = 6};
show();
--[[
example 6:
6
]]


print("\nexample 7:");
local tb = {i= 1};

function outer()
    local t = tb;
    return function()
        print(t.i);
    end
end

local show = outer();
tb = {i = 7};
show();
--[[
example 7:
1
]]
