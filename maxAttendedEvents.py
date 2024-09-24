test_cases = [
    # Basic case: some overlapping, some non-overlapping
    [(1, 3), (2, 5), (4, 7), (1, 8), (5, 9), (8, 10)],  # Expected output: 3
    
    # All events overlap
    [(1, 5), (2, 6), (3, 7), (4, 8), (5, 9)],  # Expected output: 1
    
    # No events overlap
    [(1, 2), (3, 4), (5, 6), (7, 8)],  # Expected output: 4
    
    # Nested events (one event completely inside another)
    [(1, 10), (2, 3), (4, 5), (6, 7)],  # Expected output: 3
    
    # Multiple optimal solutions
    [(1, 2), (2, 3), (3, 4), (4, 5)],  # Expected output: 4
    
    # Edge case: Single event
    [(1, 100)],  # Expected output: 1
    
    # Edge case: Large number of small events
    [(i, i + 1) for i in range(1000)],  # Expected output: 1000
    
    # Edge case: Completely overlapping large events
    [(1, 1000000), (1, 1000000), (1, 1000000)],  # Expected output: 1
    
    # Large random intervals
    [(100, 200), (50, 150), (30, 120), (180, 250), (220, 300), (210, 310)],  # Expected output: 2
    
    # Random non-overlapping intervals with gaps
    [(1, 2), (5, 6), (10, 11), (15, 16), (20, 21)],  # Expected output: 5
]

test_answers = [3,2,4,3,4,1,1000,1,2,5]


def find_max_attendable_events(list_events : list[(int,int)]) -> int :

    #sort events by end
    list_events.sort(key=lambda x:x[1])

    intLastEventEnd = -1
    intTotalEventAttend = 0

    for event in list_events :
        if event[0] >= intLastEventEnd:
            intTotalEventAttend+=1
            intLastEventEnd = event[1]  

    return intTotalEventAttend

ls_func_answers = []

for event_list in test_cases :
    ls_func_answers.append(find_max_attendable_events(event_list))

print(ls_func_answers == test_answers)
    