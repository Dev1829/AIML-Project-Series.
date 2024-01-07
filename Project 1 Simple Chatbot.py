class SimpleChatbot:
    def __init__(self):
        self.context = {}

    def greet(self):
        return "Hello! I'm your chatbot. How can I assist you today?"

    def respond_to_question(self, question):
        responses = {
            "How are you?": "I'm just a computer program, but thanks for asking!",
            "What's your name?": "I'm a chatbot. You can call me ChatGPT.",
            "How does weather look today?": "I'm sorry, I don't have real-time information. You can check a weather website.",
            "Tell me a joke.": "Sure, here's one: Why don't scientists trust atoms? Because they make up everything!",
            "What is the meaning of life?": "The meaning of life is a philosophical question. I'm here to help with more practical matters!",
        }

        return responses.get(question, "I'm not sure how to answer that. Can you ask something else?")

    def farewell(self):
        return "Goodbye! If you have more questions, feel free to ask later."

    def ask_user_questions(self):
        questions = ["What is your name?", "How can I assist you today?", "Do you have any specific preferences or concerns?"]
        user_responses = {}

        for question in questions:
            user_responses[question] = input(f"{question} ")

        return user_responses

    def start_chat(self):
        print(self.greet())

        # Ask user for information
        user_responses = self.ask_user_questions()

        # Store user responses in context
        self.context.update(user_responses)

        # Respond to user's input
        for _ in range(5):  # Ask five additional questions
            user_input = input("Ask me a question: ")
            if user_input.lower() == 'exit':
                break

            response = self.respond_to_question(user_input)
            print(response)

        print(self.farewell())


if __name__ == "__main__":
    chatbot = SimpleChatbot()
    chatbot.start_chat()
