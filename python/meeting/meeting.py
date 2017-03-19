#每一行数据代表一条会议申请
#(会议编号,开始时间,结束时间)
MeetingList = [
	(1,13,15),
	(2,11,13),
	(3,20,22),
	(4,16,19),
	(5,11,16),
	(6,8,14),
	(7,14,18),
	(8,9,12),
	(9,16,20),
	(10,13,17)
]


def meeting_cmp(data):
    return data[2]

MeetingList = sorted(MeetingList, 
	key=meeting_cmp)
#for x in MeetingList:
#	print(x)
#以下是输出结果，按结束时间排序的

Result = []	#保存结果
endtime = -1
for x in MeetingList:
	if x[1] > endtime:
		Result.append(x)
		endtime = x[2]

for x in Result:
	print(x)
#以下为最终的结果
