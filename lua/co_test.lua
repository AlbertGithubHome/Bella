function main1()
    task_method_1()
end

-- lua 没有 sleep 函数，使用while循环模拟
function sleep(n)
    local t = os.clock()
    while os.clock() - t <= n do end
end

function task_method_1()
    print(string.format("program start at %s", os.date("%H:%M:%S")))

    -- 求和
    local sum = 0;
    for i=1,10 do
        sum = sum + i;
    end

    -- 等待
    sleep(5);

    -- 展示
    print(string.format("program end at %s and sum = %d", os.date("%H:%M:%S"), sum))
end




function task_method_2()
    print(string.format("program start at %s", os.date("%H:%M:%S")))

    -- 求和
    local sum = 0;
    for i=1,10 do
        sum = sum + i;
    end

    -- 注册回调函数，进行等待
    add_callback(5, call_back_print, sum)
end

function call_back_print(data)
    --展示结果
    print(string.format("program end at %s and sum = %d", os.date("%H:%M:%S"), data))
end

function add_callback(inteval, func, data)
    interval_time = inteval
    call_back = func
    msg_data = data
end

function main2()
    local t0 = os.clock();
    local t = t0;

    task_method_2()

    while true do
        local now = os.clock()
        if now - t >= 1 then
            print(string.format("program run %f seconds", now - t0))
            t = now;

            if interval_time and call_back and now - t0 >= interval_time then
                call_back(msg_data)
                break;
            end
        end
    end
end







function task_method_3()
    print(string.format("program start at %s", os.date("%H:%M:%S")))

    -- 求和
    local sum = 0;
    for i=1,10 do
        sum = sum + i;
    end

    -- 等待
    coroutine.yield(5);

    -- 展示
    print(string.format("program end at %s and sum = %d", os.date("%H:%M:%S"), sum))
end


function main3()
    local t0 = os.clock();
    local t = t0;

    local co = coroutine.create(task_method_3)
    local status, interval = coroutine.resume(co)

    while true do
        local now = os.clock()
        if now - t >= 1 then
            print(string.format("program run %f seconds", now - t0))
            t = now;

            if now - t0 >= interval then
                coroutine.resume(co)
                break;
            end
        end
    end
end

main3()