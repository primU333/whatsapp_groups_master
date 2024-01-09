import time
from tkfontawesome import *
import tkinter as tk
from tkinter.ttk import *
from tkinter import *
from tkinter.scrolledtext import ScrolledText
from random import randrange
from runner_script import create_group, get_groups, get_group_id, add_participants
from tkinter import filedialog
import os
from configs import *
import sys



class Window(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Phone Protector')
        self.text = tk.StringVar()
        # self.root = root
        self.update_idletasks()
        # created_logs = []


        self.home_canvas = tk.Canvas(self, bg= '#0f490f', bd=5)
        self.home_canvas.pack(fill=BOTH, expand=1)

        self.home_frame = tk.Frame(self.home_canvas, bg= '#0f490f')
        self.home_frame.pack()

        self.home_title = tk.Label(self.home_frame, text='WhatsApp Groups Master', bg= '#0f490f', fg='#ffffff')
        self.home_title.config(font=('Arial', 60))
        self.home_title.pack(expand=1, fill=X, pady=0, padx=0)


        self.home_image = icon_to_image("whatsapp", fill="#f1f1f1", scale_to_width=300)
        # self.logo = self.home_image.resize((300, 300))
        # self.logo = ImageTk.PhotoImage(self.logo)
        self.logo_label = tk.Label(self.home_frame, image=self.home_image, bd=0)
        self.logo_label.image = self.home_image
        self.logo_label.configure(bg='#0f490f')
        self.logo_label.pack(pady=50)

        
        self.text = 'Start'
        start_btn = tk.Button(self.home_canvas, text=self.text, bg='#0f490f', fg='#c1c1c1', width=15, height=2, command=lambda:
            self.start_app(int(1)))
        start_btn.pack()
        
        
    #footer...................
        self.footer_frame = tk.Frame(self.home_canvas, bg= '#0f490f')
        self.footer_frame.pack(side=BOTTOM,  fill=X)
        footer = tk.Label(self.footer_frame, text='primU developers @copy 2024', bg='#0f490f', fg='#ffffff')
        footer.config(font=('Times New Roman', 10))
        footer.pack()




        self.main_canvas = tk.Canvas(self, bg= '#0f490f', bd=5)
        # self.main_canvas.pack(fill=BOTH, expand=1)

        self.main_frame = tk.Frame(self.main_canvas, bg= '#101010')
        self.main_frame.pack(fill=BOTH, expand=1, pady=0, side=TOP)

        self.main_image = icon_to_image("whatsapp", fill="#f1f1f1", scale_to_width=80)
        # self.logo = self.main_image.resize((300, 300))
        # self.logo = ImageTk.PhotoImage(self.logo)
        self.main_label = tk.Label(self.main_frame, image=self.main_image, bd=0)
        self.main_label.image = self.main_image
        self.main_label.configure(bg='#101010')
        self.main_label.pack(side=LEFT, padx=10)

        self.main_title = tk.Label(self.main_frame, text='WhatsApp Groups Master', bg= '#101010', fg='#ffffff')
        self.main_title.config(font=('Arial', 30))
        self.main_title.pack(expand=1, fill=X, pady=10, padx=0)


        
        groups_activity_frame = tk.Frame(self.main_canvas, bg='#0f490f', width=300, height=800)
        groups_activity_frame.pack(fill=BOTH, side=TOP, expand=1)

        create_groups_panel = tk.Frame(groups_activity_frame, bg='#1E201E', width=300, height=800)
        create_groups_panel.pack(side=LEFT, fill=BOTH, expand=1, pady=20, padx=10)

        # create groups title
        create_label = tk.Label(create_groups_panel, text='Create Groups', bg='#1E201E', fg='#f1f1f1')
        create_label.config(font=('Arial', 20))
        create_label.pack(pady=20)



        #Select Contacts...................................

        selcted_name_frame = tk.Frame(create_groups_panel, bg='#1E201E')
        selcted_name_frame.pack()

        select_file = tk.Button(create_groups_panel, text='Browse Phone Numbers List (csv) ==>', fg='#f1f1f1', bg='#1E201E', command=lambda:
            self.UploadFile(selcted_name_frame))
        select_file.config(font=('Arial', 10), width=50)
        select_file.pack()


        

        

#**********************Create_groups*****************************************************
        
        

        create_frame = tk.Frame(create_groups_panel, bg='#1E201E')
        create_frame.pack(pady=20)


        self.group_number_entry = tk.Entry(create_frame)
        self.group_number_entry.insert(0, 'Enter No of Groups eg. 10')
        self.group_number_entry.config(background='#1E201E', foreground='#f1f1f1', width=47)
        self.group_number_entry.pack(padx=5, pady=5)
        

        self.phone_nos = []

        

        create_btn = tk.Button(create_frame, text='Create', bg='#1E201E', fg='#ffffff', command=lambda:
                create_group(self.get_phones_from_file(), int(self.group_number_entry.get())))
        # create_btn.config(border=)
        create_btn.pack(pady=10)


    


#******************Log out*****************************
        logout_frame = tk.Frame(create_groups_panel, bg='#0f490f')
        logout_frame.pack(pady=30)

        logout_btn = tk.Button(self.main_canvas, text='Abort', bg='#770000', fg='#ffffff', width=15, height=2, command=lambda:
            self.destroy())
        logout_btn.pack(side=TOP)



# ***********************Add participants to the group*********************
        add_paticipants_panel = tk.Frame(groups_activity_frame, bg='#0F1E49', width=300, height=800)
        add_paticipants_panel.pack(side=RIGHT, fill=BOTH, expand=1, pady=20, padx=10)


# add groups title
        add_label = tk.Label(add_paticipants_panel, text='Add Participants', bg='#0F1E49', fg='#f1f1f1')
        add_label.config(font=('Arial', 20))
        add_label.pack(pady=20)

    #Select Contacts...................................
        add_selcted_name_frame = tk.Frame(add_paticipants_panel, bg='#0F1E49')
        add_selcted_name_frame.pack()

        add_select_file = tk.Button(add_paticipants_panel, text='Browse Participants Numbers List (csv) ==>', fg='#f1f1f1', bg='#0F1E49', command=lambda:
            self.UploadParticipants(add_selcted_name_frame))
        add_select_file.config(font=('Arial', 10), width=50)
        add_select_file.pack()


        

        

#**********************add_paticipants*****************************************************

        add_frame = tk.Frame(add_paticipants_panel, bg='#0F1E49')
        add_frame.pack(pady=20)

        raw_names = get_groups(PHONE_ID)
        choices = []

        for name in raw_names['names']:
            choices.append(name)

        self.selct_group = Combobox(add_frame, values=choices,)
        self.selct_group.set('Select Group')
        style = Style()
        style.configure("TCombobox", fieldbackground="#0F1E49")
        self.selct_group.config(background='#0F1E49', foreground='#f1f1f1', width=47, height=10)
        self.selct_group.bind("<<ComboboxSelected>>", self.on_group_change)
        self.selct_group.pack(padx=5, pady=5)

        add_btn = tk.Button(add_frame, text='Add', bg='#0F1E49', fg='#ffffff', command=lambda:
                add_participants(get_group_id(self.selct_group.get()), self.get_pats_from_file()))
        add_btn.pack(pady=10)


#**********************************Logs Panel***********************************************************
        logs_panel = tk.Frame(self.main_canvas, width=1000, bg='#000000', highlightbackground='#00ff00', highlightthickness=2)
        logs_panel.pack(pady=30, fill=X, expand=1, padx=50)

        logs_label = tk.Label(logs_panel, text='Activity Logs', fg='#ffffff', bg='#101010')
        logs_label.config(font=('Ubuntu', 15))
        logs_label.pack(side=TOP)


        # Create a Text widget to act as the console
        self.console = ScrolledText(logs_panel, wrap=tk.WORD, height=30, width=4)
        self.console.config(background='#000000', fg='#00ff00')
        self.console.pack(expand=True, fill='both')
        
        # Redirect stdout to the console
        sys.stdout = TextRedirector(self.console, "stdout")


        self.main_footer_frame = tk.Frame(self.main_canvas, bg= '#0f490f')
        self.main_footer_frame.pack(side=BOTTOM,  fill=X)
        main_footer = tk.Label(self.main_footer_frame, text='primU developers @copy 2024', bg='#0f490f', fg='#ffffff')
        main_footer.config(font=('Times New Roman', 10))
        main_footer.pack()

        
    def start_app(self, t):
        self.text = 'Loading...'
        while t:
            self.text = 'Loading...'
            
            mins, secs = divmod(t, 60)
            timer = '{:02d}: {:02d}'.format(mins, secs)
            # print(timer, end='\r')
            time.sleep(1)
            t -= 1
                # time.sleep(5)
            if t > 0:
                self.home_canvas.pack(fill=BOTH, expand=1)

            else:
                self.main_canvas.pack(fill=BOTH, expand=1)
                self.home_canvas.pack_forget()




    def create(self, group_count, phone_nos):
        for i in range(group_count):
            random_delay = randrange(1, 3) #set a random range to prevent consistency and connection annormally detectors that implement the ban

            create_group(f'Group no {i}', phone_nos)

            time.sleep(random_delay)


    def UploadFile(self, btnframe, event=None):
        abs_filename = filedialog.askopenfilename()
        self.filename = f'Selected file:   {os.path.basename(abs_filename)}'
        try:
            # Read the contents of the selected file
            with open(abs_filename, 'r') as source_file:
                content = source_file.read()
                
                # create destination file
                destination_path = 'phones.txt'
                
                if destination_path:
                    # Write the duplicated content to the destination file
                    with open(destination_path, 'w') as destination_file:
                        destination_file.write(content)
                    
                else:
                    print("Destination file Does not exist.")

        except Exception as e:
            print(f"An error occurred: {e}")

        slected_file_name = tk.Label(btnframe, text=self.filename, fg='gold', bg='#0f490f')
        slected_file_name.config(font=('Arial', 10))
        slected_file_name.pack()

        print('Selected:', self.filename)
        return
    
    def UploadParticipants(self, btnframe, event=None):
        abs_filename = filedialog.askopenfilename()
        self.filename = f'Selected file:   {os.path.basename(abs_filename)}'
        try:
            # Read the contents of the selected file
            with open(abs_filename, 'r') as source_file:
                content = source_file.read()
                
                # create destination file
                destination_path = 'participants.txt'
                
                if destination_path:
                    # Write the duplicated content to the destination file
                    with open(destination_path, 'w') as destination_file:
                        destination_file.write(content)
                    
                else:
                    print("Destination file Does not exist.")

        except Exception as e:
            print(f"An error occurred: {e}")

        slected_file_name = tk.Label(btnframe, text=self.filename, fg='gold', bg='#0f490f')
        slected_file_name.config(font=('Arial', 10))
        slected_file_name.pack()

        print('Selected:', self.filename)
        return


    def get_phones_from_file(self):
        file_path = 'phones.txt'
        numbers = [line.strip() for line in open(file_path, 'r')]
        return numbers
    
    def get_pats_from_file(self):
        file_path = 'participants.txt'
        numbers = [line.strip() for line in open(file_path, 'r')]
        return numbers
    

    def on_group_change(self, event):
        selected_item = self.selct_group.get()
        print(f"Selected Group: {selected_item}")
        return selected_item
    


class TextRedirector:
    def __init__(self, widget, tag="stdout"):
        self.widget = widget
        self.tag = tag

    def write(self, str):
        self.widget.insert(tk.END, str, (self.tag,))
        self.widget.see(tk.END)  # Scroll to the end of the text


if __name__ == "__main__":
    window = Window()
    window.mainloop()
