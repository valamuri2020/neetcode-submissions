from collections import Counter
import heapq
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # coolDown = {'A': [remainingCycles, taskCount]}, if remainingCycles == 0, add back into the heap

        maxHeap = []
        coolDown = {}

        task_freq = Counter(tasks)
        for task, freq in task_freq.items():
            heapq.heappush(maxHeap, (-freq, task))
        
        cycles = 0
        while maxHeap or coolDown:
            tasksToCleanUp = []
            for task in coolDown:
                coolDown[task][0] -= 1
                if coolDown[task][0] == 0:
                    tasksToCleanUp.append(task)
                    
                    if coolDown[task][1] != 0:
                        heapq.heappush(maxHeap, (-coolDown[task][1], task))
                    
            
            for task in tasksToCleanUp:
                del coolDown[task]
            
            if maxHeap:
                workItem = heapq.heappop(maxHeap)
                taskCount, task = workItem
                taskCount = -taskCount
                remaining = taskCount - 1
                if remaining > 0:
                    coolDown[task] = [n+1, remaining]

            cycles += 1
        
        return cycles