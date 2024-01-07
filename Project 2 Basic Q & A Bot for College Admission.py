class AdmissionChatbot:
    def __init__(self):
        self.context = {}

    def greet(self):
        return "Hello! I'm here to help you with your college admission queries. How can I assist you today?"

    def respond_to_question(self, question):
        responses = {
            "What are the admission procedures?": "The admission procedures entail the submission of an online application form, a pivotal step in the intricate process of joining our academic community. This carefully designed system ensures that aspiring individuals provide essential personal and academic details. This data, meticulously reviewed by the admissions committee, aids in assessing each applicant's suitability for our institution. The emphasis on an online platform streamlines and expedites the application process, reflecting our commitment to modern educational methodologies. Applicants are encouraged to follow the outlined guidelines, facilitating a seamless integration of diverse talents and perspectives into our esteemed academic environment.",
            
            "What are the admission requirements?": "The admission requirements encompass a multifaceted evaluation of prospective students. Candidates are expected to present a well-rounded application, including a minimum GPA of 3.0, compelling recommendation letters, and a thoughtfully composed essay. This holistic approach allows us to assess both academic aptitude and personal qualities crucial for success in our academic community. By considering these diverse elements, we aim to admit individuals with a demonstrated commitment to intellectual growth and a potential to contribute meaningfully to our institution. Our rigorous admission process reflects our dedication to fostering an enriching and diverse academic environment, preparing students for future success.",
            
            "Are there any upcoming deadlines?": "Deadlines vary, so it's essential to check the specific deadlines for the colleges you're interested in. Typically, application deadlines fall in the fall or winter of the previous academic year.",
            
            "How can I improve my chances of admission?": "To improve your chances, focus on maintaining a strong GPA, participating in extracurricular activities, and submitting a compelling personal statement. Each college may have additional recommendations.",
            
            "Tell me about scholarships": "Scholarships vary by college and may be merit-based, need-based, or awarded for specific achievements. Check with the financial aid office of the colleges you're interested in for detailed information.",
            
            "What extracurricular activities are available on campus?":"The campus offers a diverse array of extracurricular activities, ranging from student-run clubs and organizations to sports teams and cultural events. Engaging in these activities fosters a vibrant community, providing students with opportunities for personal growth, leadership development, and a well-rounded college experience. Explore our website or contact the student affairs office for a comprehensive list and details on how to get involved.",
            
            "Tell me about campus housing options.":"Explore diverse on-campus housing options, including residence halls and apartments. Visit our housing department's website or contact them directly for information on availability, costs, and the application process.",
            
            "What majors or programs does the college offer?":"Our college provides a diverse array of majors and programs, spanning arts, sciences, business, and more. Explore fields such as computer science, psychology, business administration, and engineering. Visit our official website or contact the academic advising office for a comprehensive list, ensuring you find the perfect academic path to pursue your passions and career goals.",
            
            "":"",
            
        }

        return responses.get(question, "I'm not sure about that. Can you ask something else?")

    def farewell(self):
        return "Good luck with your college admissions! If you have more questions, feel free to ask later."

    def ask_user_questions(self):
        questions = [
            "What is your preferred field of study?",
            "Do you have a specific location or type of college in mind?",
            "Any specific concerns or questions about the admission process?",
        ]
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
        while True:
            user_input = input("Ask me a question about college admissions (or type 'exit' to end the session): ")
            if user_input.lower() == 'exit':
                break

            response = self.respond_to_question(user_input)
            print(response)

        print(self.farewell())


if __name__ == "__main__":
    chatbot = AdmissionChatbot()
    chatbot.start_chat()
