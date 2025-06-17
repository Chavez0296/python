def lineup(artists,set_times):

    if not artists and not set_times:
        return {}
    
    return dict(zip(artists,set_times))


artists1 = ["Kendrick Lamar", "Chappell Roan", "Mitski", "Rosalia"]
set_times1 = ["9:30 PM", "5:00 PM", "2:00 PM", "7:30 PM"]

artists2 = []
set_times2 = []

print(lineup(artists1, set_times1))
print(lineup(artists2, set_times2))


def get_artist_info(artist, festival_schedule):
    
    if festival_schedule.get(artist) == None:
        return "{'message': 'Artist not found'}"
    else:
        return festival_schedule.get(artist) 



festival_schedule = {
    "Blood Orange": {"day": "Friday", "time": "9:00 PM", "stage": "Main Stage"},
    "Metallica": {"day": "Saturday", "time": "8:00 PM", "stage": "Main Stage"},
    "Kali Uchis": {"day": "Sunday", "time": "7:00 PM", "stage": "Second Stage"},
    "Lawrence": {"day": "Friday", "time": "6:00 PM", "stage": "Main Stage"}
}

print(get_artist_info("Blood Orange", festival_schedule)) 
print(get_artist_info("Taylor Swift", festival_schedule))  

def total_sales(ticket_sales):

    total = 0
    for key in ticket_sales:
        total += ticket_sales[key]

    return total
    pass

ticket_sales = {"Friday": 200, "Saturday": 1000, "Sunday": 800, "3-Day Pass": 2500}

print(total_sales(ticket_sales))


def identify_conflicts(venue1_schedule, venue2_schedule):
    res = {}

    for i in venue1_schedule:
        for j in venue2_schedule:
            if i == j and venue1_schedule[i] == venue2_schedule[j]:
                res[j] = venue1_schedule[j]

    return res

    pass


venue1_schedule = {
    "Stromae": "9:00 PM",
    "Janelle Monáe": "8:00 PM",
    "HARDY": "7:00 PM",
    "Bruce Springsteen": "6:00 PM"
}

venue2_schedule = {
    "Stromae": "9:00 PM",
    "Janelle Monáe": "10:30 PM",
    "HARDY": "7:00 PM",
    "Wizkid": "6:00 PM"
}

print(identify_conflicts(venue1_schedule, venue2_schedule))


def best_set(votes):

    freq = {}
    
    for vote in votes.values():
        if vote in freq:
            freq[vote] += 1
        else:
            freq[vote] = 1
    
    res = max(freq, key=freq.get)

    return res

    pass


votes1 = {
    1234: "SZA", 
    1235: "Yo-Yo Ma",
    1236: "Ethel Cain",
    1237: "Ethel Cain",
    1238: "SZA",
    1239: "SZA"
}

votes2 = {
    1234: "SZA", 
    1235: "Yo-Yo Ma",
    1236: "Ethel Cain",
    1237: "Ethel Cain",
    1238: "SZA"
}

print(best_set(votes1))
print(best_set(votes2))


def max_audience_performances(audiences):

    freq = {}

    for aud in audiences:
        if aud in freq:
            freq[aud] += 1
        else:
            freq[aud] = 1

    max_aud_val = max(freq.keys())
    sums = max_aud_val * freq[max_aud_val]

    return sums
    pass


audiences1 = [100, 200, 200, 150, 100, 250]
audiences2 = [120, 180, 220, 150, 220]

print(max_audience_performances(audiences1))
print(max_audience_performances(audiences2))


def is_balanced(code):
    count = {}
    freq = {}
    for i in range(len(code)):
        if code[i] not in count:
            count[code[i]] = 0
        count[code[i]] +=1
    
    for i in count.keys():
        
        if count[i] not in freq:
            freq[count[i]] = 0
        freq[count[i]] +=1

    #print(count)
    #print(freq)

    if len(freq) == 1:
        f, letter_count = next(iter(freq.items()))
        if f == 1 or letter_count == 1:
            return True
    elif len(freq) == 2:
        f1, f2 = sorted(freq.keys())
        v1, v2 = freq[f1], freq[f2]

        if (f1 == 1 and v1 == 1) or (f2 == f1 + 1 and v2 == 1):
            return True
    
    return False
    pass

code1 = "arghh"
code2 = "haha"

print(is_balanced(code1)) 
print(is_balanced(code2)) 

def find_treasure_indices(gold_amounts, target):
    
    table = {}

    for i, amt in enumerate(gold_amounts):
        t = target - amt
        
        if t in table: #if a subtracted value is in the table then the two values subtracted equal 0
            return [table[t],i] 
        
        table[amt] = i #store value subtracted and index

    return []       
    pass

gold_amounts1 = [2, 7, 11, 15]
target1 = 9

gold_amounts2 = [3, 2, 4]
target2 = 6

gold_amounts3 = [3, 3]
target3 = 6

print(find_treasure_indices(gold_amounts1, target1))  
print(find_treasure_indices(gold_amounts2, target2))  
print(find_treasure_indices(gold_amounts3, target3))  

from collections import defaultdict
def organize_pirate_crew(group_sizes):
    group = defaultdict(list)
    res = []
    for i, size in enumerate(group_sizes):
        group[size].append(i)
        
        if len(group[size]) == size:
            res.append(group[size])
            group[size] = []

    return res
    pass


group_sizes1 = [3, 3, 3, 3, 3, 1, 3]
group_sizes2 = [2, 1, 3, 3, 3, 2]

print(organize_pirate_crew(group_sizes1))
print(organize_pirate_crew(group_sizes2)) 