from collections import Counter
from responses import responses, blank_spot
from user_functions import preprocess, compare_overlap, pos_tag, extract_nouns, compute_similarity
import spacy
word2vec = spacy.load('en')

exit_commands = ("quit", "goodbye", "exit", "no")

class ChatBot:
  
  #define .make_exit() below:
  def make_exit(self, user_message):
    for command in exit_commands:
      if command in user_message:
        print("Goodbye my love!")
  #define .chat() below:

  def chat(self):
    user_message = input("Welcome to the Diner Bot 01! Please ask me anything.\n")
    while not self.make_exit(user_message):
      user_message = self.respond(user_message)
  #define .find_intent_match() below:
  def find_intent_match(self, responses, user_message):
    bow_model = Counter(preprocess(user_message))
    processed_responses = [Counter(preprocess(response)) for response in responses]
    similarity_list = [compare_overlap(user_message, response) for response in processed_responses]
    response_index = similarity_list.index(max(similarity_list))
    return responses[response_index]
  #define .find_entities() below:
  def find_entities(self, user_message):
    tagged_user_message = pos_tag(preprocess(user_message))
    message_nouns = extract_nouns(tagged_user_message)
    tokens = word2vec(" ".join(message_nouns))
    category = word2vec(blank_spot)
    word2vec_result = compute_similarity(tokens, category)
    word2vec_result.sort(key=lambda x: x[2])
    if len(word2vec_result) > 1:
      return word2vec_result[-1][0]
    else:
      return blank_spot
  #define .respond() below:
  def respond(self, user_message):
    best_response = self.find_intent_match(responses, user_message)
    entity = self.find_entities(user_message)
    print(best_response.format(entity))
    input_message = input("Ask away.\n")
    return input_message

#initialize ChatBot instance below:
test_bot = ChatBot()
#call .chat() method below:
test_bot.chat()


