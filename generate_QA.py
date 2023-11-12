from Questgen import main
from translator import translate, en_ru, ru_en
from doc_parser import parse

paragraphs = [''.join(parse('input.docx')[5*i:5*i+5]) for i in range(10, 15)]

tokenizer_ru_en, model_ru_en = ru_en()
tokenizer_en_ru, model_en_ru = en_ru()
quest_gen = main.QGen()
answer_gen = main.AnswerPredictor()

qna_set = set()

for paragraph in paragraphs:
    russian_text = paragraph
    english_text = translate(russian_text, tokenizer_ru_en, model_ru_en)

    payload = {
        "input_text": "",
        "input_question": ""
    }
    output = quest_gen.predict_shortq(payload)
    questions = output.get("questions", {})

    for question_dict in questions:
        q = question_dict['Question']
        c = question_dict['context']
        payload["input_question"] = q
        payload["input_text"] = c
        a = answer_gen.predict_answer(payload)
        russian_q = translate(q, tokenizer_en_ru, model_en_ru)
        print(russian_q)
        russian_a = translate(a, tokenizer_en_ru, model_en_ru)
        print(russian_a)
        qna_set.add((russian_q, russian_a))
        print()

with open('ai_res.txt', 'w') as out:
    for question, answer in qna_set:
        print(question, file=out)
        print(answer, file=out)
        print(file=out)
