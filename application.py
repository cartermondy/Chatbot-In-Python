import tkinter as tk
import openai
from tkinter import *
from pdf_convertor import PDF_Reader
from tkinter import filedialog



BG_gray = "#ABB2B9"
BG_color = "#17202A"
TEXT_color = "#EAECEE"

FONT = "Helvetica 14"
FONT_BOLD = "Helvetica 13 bold"

class ChatbotApp:
    
    def __init__(self):
        self.window = Tk()
        self._setup_main_window()
        openai.api_key = #Input open AI API Key 
    
    def run(self):
        self.window.mainloop()
        

    def _setup_main_window(self):
        self.window.title("Chat")
        self.window.resizable(width=True, height=True)
        self.window.configure(width=470, height=550, bg=BG_color)
        
        # head label
        head_label = Label(self.window, bg=BG_color, fg=TEXT_color,
                           text="ChatBot App", font=FONT_BOLD, pady=10)
        head_label.place(relwidth=1)
        
        # divider
        line = Label(self.window, width=450, bg=BG_gray)
        line.place(relwidth=1, rely=0.07, relheight=0.012)
        
        # text widget
        self.text_widget = Text(self.window, width=20, height=2, bg=BG_color, fg=TEXT_color,
                                font=FONT, padx=1, pady=5)
        self.text_widget.place(relheight=0.65, relwidth=1, rely=0.08)
        self.text_widget.configure(cursor="arrow", state=DISABLED)
        
        # scroll bar
        scrollbar = Scrollbar(self.text_widget)
        scrollbar.place(relheight=1, relx=0.974)
        scrollbar.configure(command=self.text_widget.yview)
        
        # bottom label
        bottom_label = Label(self.window, bg=BG_gray, height=80)
        bottom_label.place(relwidth=1, rely=0.825)
        
        # message entry box
        self.msg_entry = Entry(bottom_label, bg="#2C3E50", fg=TEXT_color, font=FONT)
        self.msg_entry.place(relwidth=0.5, relheight=0.06, rely=0.008, relx=0.011)
        self.msg_entry.focus()
        self.msg_entry.bind("<Return>", self._on_enter_pressed)
        
        # send button
        send_button = Button(bottom_label, text="Send", font=FONT_BOLD, width=10, bg=BG_gray,
                             command=lambda: self._on_enter_pressed(None))
        send_button.place(relx=0.75, rely=0.008, relheight=0.06, relwidth=0.22)
        
        # browse button
        browse_button = Button(bottom_label, text="Browse PDF", font=FONT_BOLD,
                               command=self.browse_pdf_file)
        browse_button.place(relx=0.55, rely=0.008, relheight=0.06, relwidth=0.22)
        

    def browse_pdf_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("PDF Files", "*.pdf")])
        if file_path:
            with open(file_path, 'rb') as file:
                file_contents = file.read().decode('utf-8', errors='ignore')
                self.text_widget.configure(state=tk.NORMAL)
                self.text_widget.insert(tk.END, f"\nFile Contents:\n{file_contents}\n")
                self.text_widget.configure(state=tk.DISABLED)
        
    def _on_enter_pressed(self, event):
        msg = self.msg_entry.get()
        self._insert_message(msg, "You")
        
    def _insert_message(self, msg, sender):
        if not msg:
            return
        self.msg_entry.delete(0, END)
        msg1 = f"{sender}: {msg}\n\n"
        self.text_widget.configure(state=NORMAL)
        self.text_widget.insert(END, msg1)
        self.text_widget.configure(state=DISABLED)
        
        # Chabot response
        bot_response = self.chat_bot(msg)
        msg2 = f"Chatbot: {bot_response}\n\n"
        self.text_widget.configure(state=NORMAL)
        self.text_widget.insert(END, msg2)
        self.text_widget.configure(state=DISABLED)
        
        self.text_widget.see(END)

    def chat_bot(self, user_input):
        response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {
            "role": "user",
            "content": user_input
             },
            {
            "role": "assistant",
            "content": "for me"
            }
            ],
            temperature=1,
            max_tokens=256,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0
            )
        return response.choices[0].message["content"]
    
        
if __name__ == "__main__":
    app = ChatbotApp()
    app.run()