def fifo(pages, frames):
    memory = []
    page_faults = 0
    for page in pages:
        if page not in memory:
            if len(memory) < frames:
                memory.append(page)
            else:
                memory.pop(0)
                memory.append(page)
            page_faults += 1
        print(memory)
    return page_faults, memory

def optimal(pages, frames):
    memory = []
    page_faults = 0
    for i in range(len(pages)):
        page = pages[i]
        if page not in memory:
            if len(memory) < frames:
                memory.append(page)
            else:
                future_uses = []
                for m in memory:
                    if m in pages[i:]:
                        future_uses.append(pages[i:].index(m))
                    else:
                        future_uses.append(float('inf'))
                memory.pop(future_uses.index(max(future_uses)))
                memory.append(page)
            page_faults += 1
        print(memory)
    return page_faults, memory

def lru(pages, frames):
    memory = []
    last_used = []
    page_faults = 0
    for page in pages:
        if page in memory:
            last_used[memory.index(page)] = 0
        else:
            if len(memory) < frames:
                memory.append(page)
                last_used.append(0)
            else:
                idx_to_replace = last_used.index(max(last_used))
                memory[idx_to_replace] = page
                last_used[idx_to_replace] = 0
            page_faults += 1
        last_used = [x + 1 for x in last_used]
        print(memory)
    return page_faults, memory

pages = [0, 0, 1, 1, 0, 1, 2, 2, 1, 2, 3, 3, 1, 4, 4, 0, 0, 2, 1, 1, 2, 1, 4, 0, 4, 0, 5, 1]
frames_count = 4

print("FIFO:")
fifo_faults, fifo_final = fifo(pages, frames_count)
print("Page Faults:", fifo_faults, "Final Frames:", fifo_final)

print("\nOptimal:")
optimal_faults, optimal_final = optimal(pages, frames_count)
print("Page Faults:", optimal_faults, "Final Frames:", optimal_final)

print("\nLRU:")
lru_faults, lru_final = lru(pages, frames_count)
print("Page Faults:", lru_faults, "Final Frames:", lru_final)
