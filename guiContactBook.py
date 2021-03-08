# Creating an application object that will present the overall application
from qtpy.QtWidgets import QApplication
# from qtpy.QtWidgets import QLabel
from qtpy.QtWidgets import QPushButton
# from qtpy.QtWidgets import QMenu

# Initialize application
app = QApplication([])

# Create label widget
# label = QLabel('Hello, Ketty!')
# label.show()


# function that will get executed when the user clicks a button
def say_hello(event):
    print("Hello, Love!!")


# Create Button widget
button = QPushButton('Say hello')
button.clicked.connect(say_hello)
button.show()
if __name__ == '__main__':
    # Start 'event loop'
    app.exec_()
