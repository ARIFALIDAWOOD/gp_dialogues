import pyperclip

narr_prompt = """
Context: Converting Hinglish to high quality Hindi sentences.
Steps to Follow:
1. Make the sentence better by adding more improvements if needed.
2. Add pauses at needed places to make it sound dramatic and intriguing.
3. Convert it to Hindi with proper pronunciation and with all the above mentioned features.
Other Intructions: Don't convert Hinglish to Hinglish-Diacritic; Make sure the hindi words pronunciation is correct; Reply with Hindi sentence only;don't include double quotes; Only add pauses if the existing pauses are not dramatic enough;You are allowed to improvise wherever necessary;

Sentence:"""

gp_prompt = """
Context: Converting Hinglish to high with more drama.
Steps to Follow:
1. Make the sentence better, addditions are not allowed.
2. Add pauses at needed places to make it sound dramatic and intriguing.
3. Convert it to Hindi with proper pronunciation and with all the above mentioned features.
Other Intructions: Don't convert Hinglish to Hinglish-Diacritic; Make sure the hindi words pronunciation is correct; Reply with Hindi sentence only;don't include double quotes; Only add pauses if the existing pauses are not dramatic enough;You are allowed to improvise wherever necessary;

Sentence:"""
prompt_to_use = narr_prompt if input("Narrator ? : ").upper() in ["Y", " " ] else gp_prompt
pyperclip.copy(prompt_to_use+"\n"+input("Enter Prompt: "))
print("Prompt copied to clipboard")