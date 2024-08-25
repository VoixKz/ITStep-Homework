from tkinter import *
from tkinter import filedialog, messagebox
import requests, json, os

def get_post(id):
    try:
        id = int(id)
        if id not in range(1, 101):
            return 'Error: ID is out of range'
        response = requests.get(f"https://jsonplaceholder.typicode.com/posts/{id}")
        post = response.json()
        return json.dumps(post, indent=4)
    except:
        return 'Error: Invalid ID'

window = Tk()
window.title("Fetch post from JSONPlaceholder")
window.geometry('600x400')
window.columnconfigure(0, weight=1)
window.columnconfigure(1, weight=1)
window.columnconfigure(2, weight=1)
window.columnconfigure(3, weight=1)
window.columnconfigure(4, weight=1)
window.columnconfigure(5, weight=1)
window.configure(bg='#FEF7FF')

topLabel = Label(window, text="Fetch post from JSONPlaceholder", font=("Arial Bold", 24), bg='#65558F', fg='#ffffff', height=2)
topLabel.grid(column=0, row=0, columnspan=6, sticky='ew')

getIDLabel = Label(window, height=2, text="Enter ID of post (1-100):", font=("Arial Bold", 16), bg='#FEF7FF')
getIDLabel.grid(column=1, row=1)

getIDEntry = Entry(window, width=10, font=("Arial Bold", 16), bd=1, relief="solid", highlightbackground='#65558F')
getIDEntry.grid(column=3, row=1)

def fetch_post():
    id = getIDEntry.get()
    post = get_post(id)
    displayPost.delete(1.0, END)
    displayPost.insert(END, post)

getIDBtn = Button(window, text="Get post", font=("Arial Bold", 16), bd=1, relief="solid", highlightbackground='#65558F', command=fetch_post)
getIDBtn.grid(column=4, row=1)

displayPost = Text(window, height=10, width=50, font=("Arial", 12), bd=1, relief="solid", highlightbackground='#65558F')
displayPost.grid(column=1, row=2, columnspan=4, sticky='ew')

def save_post():
    postID = getIDEntry.get()
    post = str(displayPost.get(1.0, END))
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

saveBtn = Button(window, text="Save post", font=("Arial Bold", 16), bd=1, relief="solid", highlightbackground='#65558F', command=save_post)
saveBtn.grid(column=1, row=4, pady=10, columnspan=4, sticky='ew')

window.configure(bg='#FEF7FF')
window.mainloop()