# starts both counters (# ll does not exist but should be a linked list class)
counter = ll.head
half = ll.head

# returns none if linked list is empty
if counter is None:
    return(None)

# returns the head if it is the only node
elif counter.next is None:
    return(counter)

# otherwise begin the counter loop
else:
    counting = 1
    while counting == 1:
        counter = counter.next
        if counter is not None:
            if counter.next is None:
                counting = 0
            else:
                counter = counter.next
                half = half.next
    return half
