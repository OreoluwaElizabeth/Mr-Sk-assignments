pass_count = 0
fail_count = 0 

for i in range(1, 16):
      score = int(input(f"Enter score for student {i}: "))

      if score >= 45:
          pass_count += 1
      else:
          fail_count += 1

print(f"Number of students who passed: {pass_count}")
print(f"Number of students who failed: {fail_count}") 