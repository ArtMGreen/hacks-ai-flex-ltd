from Questgen import main


OS_wikipedia = "An operating system (OS) is system software that manages computer hardware and software resources, and provides common services for computer programs. Time-sharing operating systems schedule tasks for efficient use of the system and may also include accounting software for cost allocation of processor time, mass storage, peripherals, and other resources. For hardware functions such as input and output and memory allocation, the operating system acts as an intermediary between programs and the computer hardware, although the application code is usually executed directly by the hardware and frequently makes system calls to an OS function or is interrupted by it. Operating systems are found on many devices that contain a computer – from cellular phones and video game consoles to web servers and supercomputers. "


payload = {
    "input_text": OS_wikipedia,
    "max_questions": 10000
}

qg = main.QGen()
output = qg.predict_shortq(payload)
statement, questions = output["statement"], output["questions"]
qna_set = set()
for question_dict in questions:
    qna_set.add((question_dict['Question'], question_dict['Answer']))

for question, answer in qna_set:
    print(question)
    print(answer)
    print()