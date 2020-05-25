# word2number 
This is a python program with GUI to translate word numbers to digit numbers in both English and Persian.

این یک برنامه پایتون با ظاهر گرافیکی برای تبدیل عدد با حروف به عدد با رقم به زبان فارسی و انگلیسی است

***
If you're not a developer, download the **compiler.exe** file in **Release(GitHub)**.

اگر برنامه نویس نیستید ، در قسمت **ریلیز** در سایت گیت هاب **فایل اجرایی** رو دانلود و باز کنید.
***

Otherwise, translate letters and words with yours. 

**/Main directory/**

Compiler: Linux executable. 

Compiler.py: a script to connect python to Qt, and a little smarter.

Moin.db: Persian words database. 

**/Programfiles/** 

number_changer.ui: GUI designed with PyQt5 designer. 

number_changer.py: generated from the UI file.

Persian_calculator.py: The main program for Persian words. 

English_calculator.py: The main program for English words. 

## How to use :
Type your numbers in words 

برای استفاده ، اعداد را با حروف وارد کنید

## Notice : 
To convert py file to executable in windows and linux use these commands (in cmd,powershell,terminal or similar):
  cd word2number
  pyinstaller --onefile --noconsole --icon='.\ProgramFile\Pirate Icon 21.ico' .\compiler.py

#### To convert the UI file to py :
  cd ProgramFile 
  Pyuic5 -x -o number_changer.py number_changer.ui


![Program Logo](/ProgramFile/Logo.png)
