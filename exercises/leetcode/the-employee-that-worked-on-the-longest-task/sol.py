class Solution:
    def hardestWorker(self, n: int, logs: List[List[int]]) -> int:
        min_time = float("-inf")
        min_emp_id = float("inf")
        
        job_start = 0
        
        for log in logs:
            emp_id, job_end = log
            job_duration = job_end - job_start
            if job_duration > min_time:
                min_time = max(min_time, job_duration)
                min_emp_id = emp_id
            elif job_duration == min_time:
                min_emp_id = min(min_emp_id, emp_id)
                
            job_start = job_end
        
        return min_emp_id