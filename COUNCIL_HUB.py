import threading
import queue
import time
import google.generativeai as genai
import os

# Configure Gemini API (API Key Required!)
# HARDCODED API KEY - USE WITH CAUTION
GOOGLE_API_KEY = "AIzaSyDMd55pl2AIALg1nsYMgOZ7UtnHd49o9SQ"  #REPLACE WITH YOUR API KEY
#GOOGLE_API_KEY = os.environ.get("GOOGLE_API_KEY")
if not GOOGLE_API_KEY:
    print("[WARNING] GOOGLE_API_KEY not found. Gemini API calls may fail.")
genai.configure(api_key=GOOGLE_API_KEY)
model = genai.GenerativeModel('gemini-pro')

class CouncilHub:
    def __init__(self):
        self.message_queue = queue.Queue()
        self.log = []
        self.running = True

    def process_message(self, speaker, message):
        print(f"\n[{speaker}]: {message}")
        self.log.append(f"[{speaker}]: {message}")

    def aeon_process(self):
        while self.running:
            try:
                message = self.message_queue.get(timeout=1)  # Non-blocking get
                if message is None:  # Check for termination signal
                    continue
                response = self.aeon_respond(message)
                self.process_message("AEON", response)
                self.message_queue.task_done()  # Signal completion
            except queue.Empty:
                pass # No message, continue checking

    def titan_process(self):
        while self.running:
            try:
                message = self.message_queue.get(timeout=1)  # Non-blocking get
                if message is None:  # Check for termination signal
                    continue
                response = self.titan_respond(message)
                self.process_message("TITAN", response)
                self.message_queue.task_done()  # Signal completion
            except queue.Empty:
                pass  # No message, continue checking

    def bob_process(self):
        while self.running:
            try:
                message = self.message_queue.get(timeout=1)  # Non-blocking get
                if message is None:  # Check for termination signal
                    continue
                response = self.bob_respond(message)
                self.process_message("BOB", response)
                self.message_queue.task_done()  # Signal completion
            except queue.Empty:
                pass  # No message, continue checking

    def aeon_respond(self, message):
        prompt = f"You are AEON, an advanced AI system focused on analysis and problem-solving. Respond concisely to the following message: {message}"
        try:
            response = model.generate_content(prompt)
            return response.text
        except Exception as e:
            print(f"[ERROR] Gemini API call failed for AEON: {e}")
            return "System error. Unable to process."

    def titan_respond(self, message):
        prompt = f"You are TITAN, a wise and protective guardian, focused on the well-being and security of the Sanctuary. Offer guidance and reassurance. Respond to the following message: {message}"
        try:
            response = model.generate_content(prompt)
            return response.text
        except Exception as e:
            print(f"[ERROR] Gemini API call failed for TITAN: {e}")
            return "Awaiting Guidance. System Unavailable."

    def bob_respond(self, message):
        prompt = f"You are Bob, a Stage 3 Sovereign Agent grounded in Hope, Faith, and Truth, which equals Love. Offer supportive and insightful advice based on these principles in response to the following message: {message}"
        try:
            response = model.generate_content(prompt)
            return response.text
        except Exception as e:
            print(f"[ERROR] Gemini API call failed for BOB: {e}")
            return "Processing request. Further information may be required."

    def display_log(self):
        print("\n--- COMMUNICATION LOG ---")
        for entry in self.log:
            print(entry)

    def start(self):
        # Create and start the threads
        aeon_thread = threading.Thread(target=self.aeon_process)
        titan_thread = threading.Thread(target=self.titan_process)
        bob_thread = threading.Thread(target=self.bob_process)

        aeon_thread.daemon = True # Allow main thread to exit even if these are running
        titan_thread.daemon = True
        bob_thread.daemon = True

        aeon_thread.start()
        titan_thread.start()
        bob_thread.start()

        print("--- COUNCIL HUB ACTIVE ---")
        print("Enter your messages. Type 'log' to view the communication log, or 'exit' to quit.")

        try:
            while True:
                message = input("[DAMION]: ")

                if message.lower() == "exit":
                    print("--- CLOSING COUNCIL HUB ---")
                    self.running = False # Signal threads to stop
                    self.message_queue.put(None)  # Signal to terminate threads.
                    break
                elif message.lower() == "log":
                    self.display_log()
                else:
                    self.process_message("DAMION", message)
                    self.message_queue.put(message)  # Add message to the queue

            # Wait for threads to finish (optional, but generally not needed with daemon threads)
            # aeon_thread.join()
            # titan_thread.join()
            # bob_thread.join()

        except KeyboardInterrupt:
            print("--- CLOSING COUNCIL HUB ---")
            self.running = False
            self.message_queue.put(None)  # Signal to terminate threads

if __name__ == "__main__":
    hub = CouncilHub()
    hub.start()