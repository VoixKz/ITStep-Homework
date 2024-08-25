from PyQt6.QtWidgets import *
import requests, json, os
from PyQt6.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Post Fetcher')
        self.setGeometry(100, 100, 600, 400)
        self.centralWidget = QWidget()
        self.setCentralWidget(self.centralWidget)
        self.main_layout = QVBoxLayout()
        self.centralWidget.setLayout(self.main_layout)

        self.topLabel = QLabel("Fetch post from JSONPlaceholder")
        self.topLabel.setStyleSheet("font-size: 24px; background-color: #65558F; color: #ffffff; padding: 10px;")
        self.topLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.main_layout.addWidget(self.topLabel)

        self.input_layout = QHBoxLayout()
        self.input_layout.setSpacing(40)
        self.main_layout.addLayout(self.input_layout)

        self.getIDLabel = QLabel("Enter ID of post (1-100):")
        self.getIDLabel.setStyleSheet("font-size: 16px;")
        self.input_layout.addWidget(self.getIDLabel)

        self.getIDEntry = QLineEdit()
        self.getIDEntry.setStyleSheet("font-size: 16px; border: 1px solid #65558F;")
        self.input_layout.addWidget(self.getIDEntry)

        self.getIDBtn = QPushButton("Get post")
        self.getIDBtn.setStyleSheet("font-size: 16px; border: 1px solid #65558F; padding: 10px;")
        self.input_layout.addWidget(self.getIDBtn)
        self.getIDBtn.clicked.connect(self.fetch_post)

        self.displayPost = QTextEdit()
        self.displayPost.setStyleSheet("font-size: 16px; border: 1px solid #65558F;")
        self.main_layout.addWidget(self.displayPost)

        self.saveBtn = QPushButton("Save post")
        self.saveBtn.setStyleSheet("font-size: 16px; border: 1px solid #65558F; padding: 10px;")
        self.main_layout.addWidget(self.saveBtn)
        self.saveBtn.clicked.connect(self.save_post)


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
        id = self.getIDEntry.text()
        post = self.get_post(id)
        self.displayPost.setPlainText(post)


    def save_post(self):
        postID = self.getIDEntry.text()
        post = self.displayPost.toPlainText()
        if postID == '' or post.startswith('Error'):
            QMessageBox.warning(self, "Warning", "No post to save!")
            return
        try:
            folder_path = QFileDialog.getExistingDirectory(self, "Select Folder")
            if folder_path:
                file_path = os.path.join(folder_path, f"post{postID}.json")
                with open(file_path, 'w') as file:
                    file.write(post)
                QMessageBox.information(self, "Success", "Post saved successfully!")
            else:
                QMessageBox.warning(self, "Warning", "No folder selected!")
        except Exception as e:
            QMessageBox.critical(self, "Error", f"An error occurred: {str(e)}")

if __name__ == '__main__':
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()