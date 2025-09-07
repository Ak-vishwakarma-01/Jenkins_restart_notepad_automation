import subprocess
import urllib.request

# Download Notepad++ installer
url = "https://github.com/notepad-plus-plus/notepad-plus-plus/releases/latest/download/npp.8.6.9.Installer.x64.exe"
installer_path = r"C:\Users\ak_vishwakarma_0\Downloads\npp_installer.exe"
urllib.request.urlretrieve(url, installer_path)

# Run installer silently
subprocess.run([installer_path, "/S"])  # /S for silent installation
print("Notepad++ installed.")
