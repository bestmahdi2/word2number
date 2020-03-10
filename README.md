# word2number
This is a python program with GUI to convert word numbers to digit numbers in both English and Persian.

این یک برنامه پایتون با ظاهر گرافیکی برای تبدیل عدد با حروف به عدد با رقم به زبان فارسی و انگلیسی است

***
IIf your not a developer just download the compiler.exe file in Releases(Github)

اگر برنامه نویس نیستید ، در قسمت ریلیزیز در سایت گیت هاب فایل اجرایی رو دانلود و باز کنید.
***

Otherwise, you may want to translate letters and words with yours.


/Main directory/

Compiler : Linux executable .

Compiler.py: just a script to connect python to Qt, and a little smarter. 

Moin.db: Persian words database.


/Programfiles/ 

number_changer.ui : GUI designed with PyQt5 designer . 

number_changer.py : generated from ui file . 

Persian_calculator.py : Main program for Persian words.

English_calculator.py : Main program for English words.

# Notice : 
To convert py file to executable in windows and linux use these commands (in cmd,powershell,terminal or similar):
> cd word2number

> pyinstaller --onefile --noconsole --icon='.\ProgramFile\Pirate Icon 21.ico' .\compiler.py

To convert ui file to py :
> cd ProgramFile 

> Pyuic5 -x -o number_changer.py number_changer.ui
