"""
AI Assistant - Prompt Engineering Project (FIXED VERSION)
Uses Google's Gemini API 
Functions:
1. Answering Questions
2. Summarizing Text
3. Generating Creative Content
"""

import google.generativeai as genai
import os
from datetime import datetime

class AIAssistant:
    def __init__(self):
       
        self.api_key = os.environ.get("GOOGLE_API_KEY", "AIzaSyCNwnjU5zPLsAyphMmbl50DNgPgg2sxM0c")
        genai.configure(api_key=self.api_key)

        # Correct and supported model name1
        self.model = genai.GenerativeModel("models/gemini-2.0-flash")



        self.feedback_log = []

    def get_ai_response(self, prompt, system_message="You are a helpful AI assistant."):
        """Get response from Google Gemini API"""
        try:
            full_prompt = f"{system_message}\n\n{prompt}"
            response = self.model.generate_content(full_prompt)
            return response.text.strip()
        except Exception as e:
            return f"Error: {str(e)}\nPlease ensure your Google API key is set correctly."

    def answer_questions(self):
        """Function 1: Answer factual questions"""
        print("\n=== Question Answering Mode ===")
        question = input("\nEnter your question: ").strip()

        if not question:
            print("No question provided.")
            return

        prompt = f"Provide a clear and factual answer to: {question}"
        system_msg = "You are a knowledgeable assistant that provides accurate, factual information."
        response = self.get_ai_response(prompt, system_msg)

        print(f"\nAnswer: {response}")
        self.collect_feedback("Question Answering", question, response)

    def summarize_text(self):
        """Function 2: Summarize text"""
        print("\n=== Text Summarization Mode ===")
        print("Enter the text you want to summarize (press Enter twice when done):")

        lines = []
        while True:
            line = input()
            if line == "":
                if len(lines) > 0 and lines[-1] == "":
                    break
                lines.append(line)
            else:
                lines.append(line)

        text = "\n".join(lines[:-1])

        if not text.strip():
            print("No text provided.")
            return

        prompt = f"Summarize the following text in 3–5 sentences:\n\n{text}"
        system_msg = "You are an expert at summarizing text concisely while preserving main ideas."
        response = self.get_ai_response(prompt, system_msg)

        print(f"\nSummary: {response}")
        self.collect_feedback("Text Summarization", text[:100] + "...", response)

    def generate_creative_content(self):
        """Function 3: Generate creative content"""
        print("\n=== Creative Content Generation Mode ===")
        prompt_input = input("\nWhat should I create? ").strip()

        if not prompt_input:
            print("No request provided.")
            return

        prompt = f"Create engaging and creative content about: {prompt_input}"
        system_msg = "You are a creative writer with excellent storytelling abilities."
        response = self.get_ai_response(prompt, system_msg)

        print(f"\nCreative Output:\n{response}")
        self.collect_feedback("Creative Content", prompt_input, response)

    def collect_feedback(self, function_name, user_input, ai_response):
        """Collect user feedback"""
        print("\n" + "=" * 50)
        feedback = input("Was this response helpful? (yes/no): ").strip().lower()

        feedback_entry = {
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "function": function_name,
            "user_input": user_input[:100],
            "helpful": feedback == "yes"
        }

        self.feedback_log.append(feedback_entry)

        if feedback == "yes":
            print("Thank you for your positive feedback!")
        else:
            print("Thank you for your feedback. We’ll work on improving!")

    def show_feedback_summary(self):
        """Display feedback summary"""
        if not self.feedback_log:
            print("\nNo feedback collected yet.")
            return

        print("\n=== Feedback Summary ===")
        total = len(self.feedback_log)
        helpful = sum(1 for f in self.feedback_log if f["helpful"])

        print(f"Total interactions: {total}")
        print(f"Helpful responses: {helpful}")
        print(f"Success rate: {(helpful / total) * 100:.1f}%")

        print("\nRecent feedback:")
        for entry in self.feedback_log[-5:]:
            status = "✓" if entry["helpful"] else "✗"
            print(f"{status} [{entry['timestamp']}] {entry['function']}")

    def run(self):
        """Main loop for the AI Assistant"""
        print("=" * 60)
        print("     Welcome to Your AI Assistant (FREE)     ")
        print("=" * 60)
        print("\nThis assistant uses Google Gemini API (FREE)")
        print("\nFunctions:")
        print("1. Answer factual questions")
        print("2. Summarize text")
        print("3. Generate creative content")
        print("\nNote: Make sure to set your GOOGLE_API_KEY")

        while True:
            print("\n" + "=" * 60)
            print("Main Menu")
            print("=" * 60)
            print("1. Answer Questions")
            print("2. Summarize Text")
            print("3. Generate Creative Content")
            print("4. View Feedback Summary")
            print("5. Exit")

            choice = input("\nSelect an option (1-5): ").strip()

            if choice == "1":
                self.answer_questions()
            elif choice == "2":
                self.summarize_text()
            elif choice == "3":
                self.generate_creative_content()
            elif choice == "4":
                self.show_feedback_summary()
            elif choice == "5":
                print("\nThank you for using the AI Assistant!")
                print("Goodbye!")
                break
            else:
                print("\nInvalid option. Please select 1–5.")

if __name__ == "__main__":
    assistant = AIAssistant()
    assistant.run()
