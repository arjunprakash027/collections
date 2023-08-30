import collections

predefined_questions = [
    "what is the capital of india",
    "where is west bengal",
]
predefined_answers = [
    "The capital of India is New Delhi.",
    "westbengal is in the eastern part of india",
]

word_count_matrix = collections.defaultdict(int)

def similarity_matching(input_question,predifined_questions):
    input_question = input_question.lower()
    #input_question = re.sub(r'[^\w\s]', '', input_question)

    max_similarity = -1
    most_similart_question = None

    for predefined_question in predifined_questions:
        predefined_question = predefined_question.lower()
        #predefined_question = re.sub(r'[^\w\s]', '', predefined_question)
        similarity = len(simi_words := (set(input_question.split()) & set(predefined_question.split())))
        print(similarity)
        print(simi_words)

        for word in simi_words:
            word_count_matrix[word] += 1

        if similarity > max_similarity:
            max_similarity = similarity
            most_similart_question = predefined_question
    
    return most_similart_question


def get_ans(input_question,predefined_questions,predefined_answers):
    most_similart_question = similarity_matching(input_question,predefined_questions)
    index = predefined_questions.index(most_similart_question)

    return predefined_answers[index]

input_question = "What is west bengal where?"
answer = get_ans(input_question, predefined_questions, predefined_answers)
print(answer)
print(word_count_matrix)