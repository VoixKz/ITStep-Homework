from tkinter import *
from tkinter import filedialog, messagebox
import requests, json, os

class PostFetcher():
    def __init__(self, root):
        self.window = root
        self.window.title("Fetch post from JSONPlaceholder")

        self.window.geometry('600x400')
        self.window.columnconfigure(0, weight=1)
        self.window.columnconfigure(1, weight=1)
        self.window.columnconfigure(2, weight=1)
        self.window.columnconfigure(3, weight=1)
        self.window.columnconfigure(4, weight=1)
        self.window.columnconfigure(5, weight=1)
        self.window.configure(bg='#FEF7FF')

        self.topLabel = Label(self.window, text="Fetch post from JSONPlaceholder", font=("Arial Bold", 24), bg='#65558F', fg='#ffffff', height=2)
        self.topLabel.grid(column=0, row=0, columnspan=6, sticky='ew')

        self.getIDLabel = Label(self.window, height=2, text="Enter ID of post (1-100):", font=("Arial Bold", 16), bg='#FEF7FF')
        self.getIDLabel.grid(column=1, row=1)

        self.getIDEntry = Entry(self.window, width=10, font=("Arial Bold", 16), bd=1, relief="solid", highlightbackground='#65558F')
        self.getIDEntry.grid(column=3, row=1)

        self.getIDBtn = Button(self.window, text="Get post", font=("Arial Bold", 16), bd=1, relief="solid", highlightbackground='#65558F', command=self.fetch_post)
        self.getIDBtn.grid(column=4, row=1)

        self.displayPost = Text(self.window, height=10, width=50, font=("Arial", 12), bd=1, relief="solid", highlightbackground='#65558F')
        self.displayPost.grid(column=1, row=2, columnspan=4, sticky='ew')

        self.saveBtn = Button(self.window, text="Save post", font=("Arial Bold", 16), bd=1, relief="solid", highlightbackground='#65558F', command=self.save_post)
        self.saveBtn.grid(column=1, row=4, pady=10, columnspan=4, sticky='ew')

    def get_post(self, id):
        try:
            id = int(id)
            if id not in range(1, 101):
                return 'Error: ID is out of range'
            response = requests.get(f"https://jsonplaceholder.typicode.com/posts/{id}")
            post = response.json()
            return json.dumps(post, indent=4)
        except:
            return 'Error: Invalid ID'

    def fetch_post(self):
        id = self.getIDEntry.get()
        post = self.get_post(id)
        self.displayPost.delete(1.0, END)
        self.displayPost.insert(END, post)

    def save_post(self):
        postID = self.getIDEntry.get()
        post = str(self.displayPost.get(1.0, END))
        if postID == '' or post.startswith('Error'):
            messagebox.showwarning("Warning", "No post to save!")
            return
        try:
            folder_path = filedialog.askdirectory()
            if folder_path:
                file_path = os.path.join(folder_path, f"post{postID}.json")
                with open(file_path, 'w') as file:
                    file.write(post)
                messagebox.showinfo("Success", "Post saved successfully!")
            else:
                messagebox.showwarning("Warning", "No folder selected!")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")

if __name__ == '__main__':
    root = Tk()
    app = PostFetcher(root)
    root.mainloop()