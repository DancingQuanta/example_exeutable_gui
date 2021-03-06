import sys

import pkg_resources

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import (QAction, QApplication, QDesktopWidget, QDialog, QFileDialog,
                             QHBoxLayout, QLabel, QMainWindow, QToolBar, QVBoxLayout, QWidget)


class Toy_GUI(QMainWindow):
    """Create the main window that stores all of the widgets necessary for the application."""

    def __init__(self, parent=None):
        """Initialize the components of the main window."""
        super(Toy_GUI, self).__init__(parent)
        self.resize(1024, 768)
        self.setWindowTitle('Toy_GUI')
        window_icon = pkg_resources.resource_filename('toy_gui.images',
                                                      'ic_insert_drive_file_black_48dp_1x.png')
        self.setWindowIcon(QIcon(window_icon))

        self.widget = QWidget()
        self.layout = QVBoxLayout(self.widget)
        self.layout.setAlignment(Qt.AlignVCenter)

        # Create a message box
        self.msg_box = QLabel()
        self.msg_box.setAlignment(Qt.AlignCenter)
        self.layout.addWidget(self.msg_box)

        # Menus
        self.menu_bar = self.menuBar()
        self.about_dialog = AboutDialog()

        self.file_menu()
        self.help_menu()


    def file_menu(self):
        """Create a file submenu with an Open File item that opens a file dialog."""
        self.file_sub_menu = self.menu_bar.addMenu('File')

        self.open_action = QAction('Open File', self)
        self.open_action.setStatusTip('Open a file into Toy_GUI.')
        self.open_action.setShortcut('CTRL+O')
        self.open_action.triggered.connect(self.open_file)

        self.exit_action = QAction('Exit Application', self)
        self.exit_action.setStatusTip('Exit the application.')
        self.exit_action.setShortcut('CTRL+Q')
        self.exit_action.triggered.connect(lambda: QApplication.quit())

        self.file_sub_menu.addAction(self.open_action)
        self.file_sub_menu.addAction(self.exit_action)

    def help_menu(self):
        """Create a help submenu with an About item tha opens an about dialog."""
        self.help_sub_menu = self.menu_bar.addMenu('Help')

        self.about_action = QAction('About', self)
        self.about_action.setStatusTip('About the application.')
        self.about_action.setShortcut('CTRL+H')
        self.about_action.triggered.connect(lambda: self.about_dialog.exec_())

        self.help_sub_menu.addAction(self.about_action)

    

    def open_file(self):
        """Open a QFileDialog to allow the user to open a file into the application."""
        filename, accepted = QFileDialog.getOpenFileName(self, 'Open File')

        if accepted:
            with open(filename) as file:
                file.read()

    def display_msg(self, msg):
        """Display a message"""
        print('test')
        self.msg_box.setText(msg)


class AboutDialog(QDialog):
    """Create the necessary elements to show helpful text in a dialog."""

    def __init__(self, parent=None):
        """Display a dialog that shows application information."""
        super(AboutDialog, self).__init__(parent)

        self.setWindowTitle('About')
        help_icon = pkg_resources.resource_filename('toy_gui.images',
                                                    'ic_help_black_48dp_1x.png')
        self.setWindowIcon(QIcon(help_icon))
        self.resize(300, 200)

        author = QLabel('Andrew Tolmie')
        author.setAlignment(Qt.AlignCenter)

        icons = QLabel('Material design icons created by Google')
        icons.setAlignment(Qt.AlignCenter)

        github = QLabel('GitHub: DancingQuanta')
        github.setAlignment(Qt.AlignCenter)

        self.layout = QVBoxLayout()
        self.layout.setAlignment(Qt.AlignVCenter)

        self.layout.addWidget(author)
        self.layout.addWidget(icons)
        self.layout.addWidget(github)

        self.setLayout(self.layout)

class App(QApplication):
    def __init__(self, sys_argv):
        super(App, self).__init__(sys_argv)

        self.window = Toy_GUI()

        desktop = QDesktopWidget().availableGeometry()
        width = (desktop.width() - self.window.width()) / 2
        height = (desktop.height() - self.window.height()) / 2
        self.window.show()
        self.window.move(width, height)


def cli():
    app = App(sys.argv)
    app.window.display_msg('console_scripts')
    sys.exit(app.exec_())

def gui():
    app = App(sys.argv)
    app.window.display_msg('gui_scripts')
    sys.exit(app.exec_())
