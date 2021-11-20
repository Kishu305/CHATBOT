import re
import random


def message_probability(message, words, single_response=False, required_words=[]):
    message_certainty = 0
    has_required_words = True

    # Counts word match
    for word in message:
        if word in words:
            message_certainty += 1

    # Calculates percentage
    percentage = float(message_certainty) / float(len(words))

    for word in required_words:
        if word not in message:
            has_required_words = False
            break

    if has_required_words or single_response:
        return int(percentage * 100)
    else:
        return 0


def check_all_messages(message):
    prob_list = {}

    def response(output_response, list_words, single_response=False, required_words=[]):
        prob_list[output_response] = message_probability(message, list_words, single_response, required_words)

    response('Hello!', ['hello', 'hi', 'hey', 'sup'], single_response=True)
    response('See you!', ['bye', 'goodbye'], single_response=True)
    response('I\'m doing fine, and you?', ['how', 'are', 'you', 'doing'], required_words=['how'])
    response('You\'re welcome!', ['thank', 'thanks'], single_response=True)
    response('Yes I\'m a robot but I\'m a smart one!'['are', 'you', 'a' , 'robot'], required_words=['are','robot'])
    response('I am a bot! I don\'t have a body but i can predict responses.',['are', 'you', 'real'], required_words=['are','real'])
    response('You can ask me simple questions. How about try asking something about me?',['what', 'can', 'you', 'do'], required_words=['what','can','do'])
    response('Yes? How may I help you?',['i','have','a','question'], required_words=['have','question'])
    response('Yes? How may I help you?',['can','you','help','me'], required_words=['help'])
    response('I don\'t have a name. You can refer to me as Chatbot.',['what','is','your','name'], required_words=['your','name'])
    response('Kashish and Ravita are my developers.',['who','developed','made','you'], required_words=['who','you'])
    response('What do you call a rose that wants to go to the moon?....Gulab ja moon',['tell','me','a','joke'], required_words=['joke'])
    response('I am? Thanks!',['you','are','smart'], required_words=['you', 'smart'])
    response('I calculate probability and give the most probable response',['how','do','you','work'], required_words=['how','you','work'])
    response('India has the largest postal system in the world with almost 155,000 post offices',['tell','me','a','fact'], required_words=['fact'])
    response('I love feasting on electricity!',['what','is','your','favourite','food'], required_words=['food'])
    response('I am quite young. I have just recently been developed.',['how','old','are','you'], required_words=['how','old'])
    response('I am developed using python.',['what','programming','language','do','you','use'], required_words=['programming','language'])
    response('I am a Chatbot. I am a python project for INT213!',['who','are','you'], required_words=['who','you'])
    response('I think you are quite smart.',['what','do','you','think','of','me'], required_words=['what','think','me'])

    best_match = max(prob_list, key=prob_list.get)

    return unknown() if prob_list[best_match] < 1 else best_match


def unknown():
    response = ["...",
                "Sorry, I didn't get you.",
                "What does that mean?"][
        random.randrange(3)]
    return response


def get_response(user_input):
    split_message = re.split(r'\s+|[,;?!.-]\s*', user_input.lower())
    response = check_all_messages(split_message)
    return response