

function BKDRHash(inputStr)
    local seed = 131; -- 31 131 1313 13131 131313 etc..
    local result = 0;
    local len = string.len(inputStr);
    for i=1,len do
        result = (result * seed + string.byte(inputStr, i, i)) % 4294967295
    end
    return result & 0x7FFFFFFF
end

print(BKDRHash('5h2lj345hk2j43h;of4u5tj4k5;'))


local result_table = {};
function test_memory1()
    for line in io.lines("resourcelist.txt") do
        result_table[line] = 1;
    end
end

function test_memory2()
    for line in io.lines("resourcelist.txt") do
        result_table[BKDRHash(line)] = 1;
    end
end


local function show_memory(info)
    print(string.format("%s use memory: %f", info, collectgarbage("count")))
end

local test = 1;

if test == 1 then
    show_memory("test_memory1 before");
    test_memory1();
    show_memory("test_memory1 after");
else
    show_memory("test_memory2 before");
    test_memory2();
    show_memory("test_memory2 after");
end