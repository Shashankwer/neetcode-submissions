class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        task_to_schedule = Counter(tasks)
        taskHeap = [-cnt for cnt in task_to_schedule.values()]
        heapq.heapify(taskHeap)
        time = 0
        q = []
        while taskHeap or q:
            print(taskHeap,q)
            time += 1
            if not taskHeap:
                time = q[0][1]
            else:
                cnt = 1 + heapq.heappop(taskHeap)
                if cnt:
                    q.append([cnt, time+n])
            if q and q[0][1] == time:
                heapq.heappush(taskHeap, q.pop(0)[0])
        return time