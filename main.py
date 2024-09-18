import sys

from buttons import ButtonsGrid
from display import Display
from info import Info
from main_window import MainWindow
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QApplication
from styles import setupTheme
from environment import WINDOW_ICON_PATH


if __name__ == '__main__':
    # Cria a Aplicação
    app = QApplication(sys.argv)
    setupTheme(app)
    window = MainWindow()
    
    # Define o ícone
    icon = QIcon(str(WINDOW_ICON_PATH))
    window.setWindowIcon(icon)
    app.setWindowIcon(icon)
    
    # Info
    info = Info("")
    window.addWidgetToVLayout(info)
    
    # Criando o Display
    display = Display()
    window.addWidgetToVLayout(display)
    
    # Grid
    # buttonsGrid = ButtonsGrid(display, info, window)
    buttonsGrid = ButtonsGrid(display, info, window)
    window.vLayout.addLayout(buttonsGrid)
        
    # Configuração para o icon aparecer na taskbar do Windows
    if sys.platform.startswith('win'):
        import ctypes
        ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(
            u'CompanyName.ProductName.SubProduct.VersionInformation')
        
    # Executa a Aplicação
    window.adjustFixedSize()
    window.show()
    app.exec()