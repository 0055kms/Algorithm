def solution(genres, plays):
    answer = []
    """
    1. 장르별로 재생 수 저장해서 장르 내림차순 정렬
    2. 장르별로 (노래의 인덱스,재생 횟수) 저장 - 리스트 안에 넣으면 됨
    3.  2번을  1..재생 내림차순, 2..고유번호 오름차순 정렬
    """
    gen_count = {}
    gen_song = {}
    
    for i in range(len(plays)):
        gen = genres[i]
        play = plays[i]
        if gen not in gen_count:
            gen_count[gen] = play
            gen_song[gen] = [(i,play)]
        else:
            gen_count[gen] += play
            gen_song[gen].append((i,play))
    
    gg = list(gen_count.items())
    gg.sort(key = lambda x: -x[1])
    
    for gen in gg:
        l = gen_song[gen[0]]
        l.sort(key = lambda x: (-x[1],x[0]))
        l = l[:2]
        for i, j in l:
            answer.append(i)
    
    return answer