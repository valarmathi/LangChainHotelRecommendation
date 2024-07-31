from modules.InitializeConversation import initial_conversation
from modules.ChatCompletions import get_chat_completions
from modules.ChatCompletions  import get_chat_response
from modules.IntentConfirmation import intent_confirmation_layer
import modules.HotelRecommendationUtil as hotelUtil
from modules.Dictionarypresent import dictionary_present

#from modules.IntentConfirmation import intent_confirmation_layer
class HotelRecommendationBot:
    def deploy(self):
        conversation = initial_conversation()
        introduction = get_chat_completions(conversation)
        
        print(introduction + '\n')
        top_3_hotels = None
    
        user_input = ''
        while(user_input != "exit"):
            user_input = input("")

            if top_3_hotels is None:    
                response_assistant = get_chat_response(conversation, user_input)
                print(response_assistant.content)

                system = 'help users retrieve top 3 hotel based on the user preference. The list of hotels should be returned in the format which user can understand. The list of hotels and the user preferences are already shared with you. please use the data as needed'
                op = get_chat_completions(system)
                print('====== op ====', op)