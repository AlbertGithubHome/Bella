-- -*- coding: utf-8 -*-
-- find the line of containing chinese in files

function start_find_chinese( ... )
    local find_count = 0;
    local outfile = io.open('strkey_ko_untranslate.txt', 'wb')
    local infile = io.open('strkey_ko.txt', 'rb')

    for line in infile:lines() do
        print(string.find(line, '(%d%c)', 1, false))
        if string.find(line, '(.*[\u4E00-\u9FA5]+)|([\u4E00-\u9FA5]+.*)', 1, false) then
            outfile:write(line)
            find_count = find_count + 1
        end
    end

    outfile:close()
    infile:close()
    return find_count
end


local count = start_find_chinese()
print("find complete! count =", count)
