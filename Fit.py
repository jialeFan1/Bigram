def first_fit(memory, request):
    for i in range(len(memory)):
        if memory[i] >= request:
            memory[i] -= request
            return True, memory
    return False, memory

def best_fit(memory, request):
    min_fit = None
    min_fit_index = -1
    for i in range(len(memory)):
        if memory[i] >= request and (min_fit is None or memory[i] < min_fit):
            min_fit = memory[i]
            min_fit_index = i
    if min_fit_index != -1:
        memory[min_fit_index] -= request
        return True, memory
    return False, memory

def worst_fit(memory, request):
    max_fit = None
    max_fit_index = -1
    for i in range(len(memory)):
        if memory[i] >= request and (max_fit is None or memory[i] > max_fit):
            max_fit = memory[i]
            max_fit_index = i
    if max_fit_index != -1:
        memory[max_fit_index] -= request
        return True, memory
    return False, memory

def allocate_memory(algorithm, requests):
    memory = [300, 200, 250]
    results = []
    for request in requests:
        if algorithm == 'first_fit':
            success, memory = first_fit(memory, request)
        elif algorithm == 'best_fit':
            success, memory = best_fit(memory, request)
        elif algorithm == 'worst_fit':
            success, memory = worst_fit(memory, request)
        results.append((request, success, memory.copy()))
        if not success:
            break
    return results

requests = [100, 150, 200, 200, 100]
algorithms = ['first_fit', 'best_fit', 'worst_fit']

for algo in algorithms:
    print(f"\n{algo.replace('_', ' ').title()}:")
    results = allocate_memory(algo, requests)
    for request, success, mem in results:
        print(f"Request {request}Kb: {'Allocated' if success else 'Failed'}, Memory Blocks: {mem}")
