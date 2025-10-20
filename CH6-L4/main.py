def last_work_experience(work_experiences):
  if len(work_experiences) == 0:
    return None
  return work_experiences[len(work_experiences) - 1]
