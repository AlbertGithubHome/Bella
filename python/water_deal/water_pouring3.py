A , B, C = 8, 5, 3
init_state, target_state = (8, 0, 0), (4, 4, 0)

def get_next_state(a, b, c):
    return {
        ((0,a+b,c) if a+b <= B else (a-(B-b),B,c)):'A->B',
        ((0,b,a+c) if a+c <= C else (a-(C-c),b,C)):'A->C',
        ((b+a,0,c) if b+a <= A else (A,b-(A-a),c)):'B->A',
        ((a,0,b+c) if b+c <= C else (a,b-(C-c),C)):'B->C',
        ((c+a,b,0) if c+a <= A else (A,b,c-(A-a))):'C->A',
        ((a,c+b,0) if c+b <= B else (a,B,c-(B-b))):'C->B'
    }

def find_result(start):
    if start == target_state:
        return [start]

    lookup = set(start)
    path_pool = [[start]]

    while path_pool:
        main_path = path_pool.pop(0)
        tail_state = main_path[-1]

        next_state_dict = get_next_state(*tail_state).items()
        for (state, desc) in next_state_dict:
            if state not in lookup:
                lookup.add(state)
                new_path = main_path + [desc, state]
                if state == target_state:
                    return new_path
                else:
                    path_pool.append(new_path)
    return []

print(find_result(init_state))

'''
现在有三个容积分别是3升、5升和8升的水桶，其中容积为8升的水桶中装满了水，容积为3升和容积为5升的水桶是空的。

三个水桶都没有体积刻度，现在需要将大水桶中的8升水等分成两份，每份都是4升水，（附加条件是只能使用另外两个空水桶）
'''