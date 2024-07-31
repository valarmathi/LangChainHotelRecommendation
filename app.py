from flask import Flask
from HotelRecommendationBot import HotelRecommendationBot

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!!!"

if __name__=='__main__':
    print("Welcome to Hotel Recommendation chatbot");
    print("===================================================");
    hotelBot = HotelRecommendationBot()
    hotelBot.deploy()
    print("===================================================");
    print("Thank you for choosing Hotel Recommendation chatbot");
