import docx


def parse(docname):
    doc = docx.Document(docname)
    text_processed = []
    for paragraph in doc.paragraphs:
        text = paragraph.text

        if not ('<' in text or len(text) < 200 or '--' in text or '__' in text or '..' in text):
            if text[1].isdigit():
                text_processed.append(text[text.index(' ') + 1:] + ' ')
            elif text[0].isdigit():
                text_processed.append(text[text.index(' ') + 1:] + ' ')
            elif text[1] == ')':
                text_processed.append(text[2:] + ' ')
            elif text[2] == ')':
                text_processed.append(text[3:] + ' ')
            else:
                text_processed.append(text + ' ')
    return text_processed
