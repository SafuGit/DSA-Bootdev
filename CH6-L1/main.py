def count_marketers(job_titles: list[str]):
  count = 0
  for job in job_titles:
    if job.lower() == "marketer":
      count += 1
  return count
