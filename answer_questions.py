from Questgen import main
from translator import translate, en_ru, ru_en
from doc_parser import parse
import pandas


def answer_questions(question_list):
    paragraphs = ''.join(parse('input.docx'))

    tokenizer_ru_en, model_ru_en = ru_en()
    tokenizer_en_ru, model_en_ru = en_ru()
    answer_gen = main.AnswerPredictor()

    answer_list = list()

    english_text = translate(paragraphs, tokenizer_ru_en, model_ru_en)

    payload = {
        "input_text": english_text,
        "input_question": ""
    }

    for russian_question in question_list[:10]:
        print(russian_question)
        english_question = translate(russian_question, tokenizer_ru_en, model_ru_en)
        payload["input_question"] = english_question
        output = answer_gen.predict_answer(payload)
        russian_output = translate(output, tokenizer_en_ru, model_en_ru)
        print(russian_output)
        answer_list.append(russian_output)
        print()

    return answer_list




file = pandas.read_excel('Questions_list.xlsx')

questions = file['question'].values.tolist()
answers = answer_questions(questions)

df = pandas.DataFrame({'answer': answers})

file["answer"] = df["answer"]

file.to_excel("answers.xlsx")
