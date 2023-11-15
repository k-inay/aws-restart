file_path = "/home/ec2-user/environment/preproinsulin-seq-clean.txt"

with open(file_path, 'r') as file:
    content = file.read()

# Extract characters from position 35 to 50
specific_text = content[89:110]

print("Extracted text:", specific_text)