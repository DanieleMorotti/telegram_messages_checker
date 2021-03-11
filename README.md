# telegram_messages_checker
A simple script to check if messages containing certain words arrive on your telegram account. A song is played to alert you or to wake you up in case you are waiting for an important message during the night.

## Get started
An installed version of [Python](https://www.python.org) is required, i tested this script with Python3, some libraries may not work with a Python2 installation.
You first need to get your own api id on [telegram site](https://core.telegram.org/api/obtaining_api_id). When you got it, insert the api_id and the api_hash in 'check_notification.py' file to connect with your account when the script is run.
I wrote 2 secondary scripts, 'check_process.ps1' works with Windows Powershell and 'check_process.sh' works in Linux systems. The goal of these scripts is to check if the python script stop working for connection error or any other problem. If you don't need it you can directly run 'check_notification.py'. I recommend to create a virtual environment with python before running the script, the first command below is used to install virtualenv if it is not present in your pc, the second one is for creating the environment.
```python
#go to your project directory and prompt the following command
pip install virtualenv
virtualenv env #write the name you prefer for the virtual environment
```
Now your virtual environment is ready, activate it with 
```python
source env/bin/activate (Linux)
.\env\Scripts\activate (Windows)
```
and run 'pip install -r requirements.txt' if you're on Windows, requirements_linux.txt for Linux users.

## Run the scripts
You need to insert some data in the python script to customize your search. Check these lines:
- lines 7-8, you need to insert your own api id as said previously;
- line 14, you have to insert here the words you want to be warned about;
- line 25, if you want to check if some messages are arrived in some chats while you are offline or the python script had stopped working;

If you want to execute the python script only run 'check_notification.py', the first time you run it a message appear to log into your Telegram account. After that a 'session_file.session' file is created and if you don't delete it the following times you don't need to log in again.
I used the playsound library for simplicity but it doesn't offer many features,therefore it's necessary to stop the song with 'ctrl+c'.

If you prefer to launch the Powershell or Bash script to restore the program automatically if its execution is interrupted simply launch the script which automatically run the python file.
On Microsoft Windows, it may be required to enable script execution. You can do this by issuing the following PowerShell command:
```Powershell
PS C:> Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```
See About [Execution Policies](https://docs.microsoft.com/en-us/powershell/module/microsoft.powershell.security/set-executionpolicy?view=powershell-7.1) for more information.