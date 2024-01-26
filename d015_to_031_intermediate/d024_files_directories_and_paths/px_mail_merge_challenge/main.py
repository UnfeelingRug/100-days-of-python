# Bring in the names from the file and save them to a list, split by line.
with open('d015_to_031_intermediate/d024_files_directories_and_paths/px_mail_merge_challenge/Input/Names/invited_names.txt') as f:
    names = f.readlines()
    
# Strip the names of trailing characters, insert them into the letter text, then save to a new file.
with open('d015_to_031_intermediate/d024_files_directories_and_paths/px_mail_merge_challenge/Input/Letters/starting_letter.txt') as f:
    og_text = f.read()
    for i in range(len(names)):
        name = names[i].strip()
        new_text = og_text.replace('[name]', name)
        name = name.replace(" ", "_")
        with open(f'd015_to_031_intermediate/d024_files_directories_and_paths/px_mail_merge_challenge/Output/ReadyToSend/letter_{name}.txt', mode='w') as w:
            w.write(new_text)
