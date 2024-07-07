placeholder="[name]"
with open(r"Mail+Merge+Project+Start\Mail Merge Project Start\Input\Names\invited_names.txt") as names_file:
    names=names_file.readlines()
with open(r"Mail+Merge+Project+Start\Mail Merge Project Start\Input\Letters\starting_letter.txt") as letter_file:
    letter_contents=letter_file.read()
    for name in names:
        striped_names=name.strip()
        new_letter=letter_contents.replace(placeholder,striped_names)
        with open(rf"C:\Users\lahya\OneDrive\Desktop\python projects\Mail+Merge+Project+Start\Mail Merge Project Start\Output\Letter_for_{striped_names}.txt",mode="w") as completed_letter:
            completed_letter.write(new_letter)

        
