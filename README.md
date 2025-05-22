{\rtf1\ansi\ansicpg936\cocoartf2822
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fswiss\fcharset0 Helvetica;\f1\fmodern\fcharset0 Courier;\f2\fmodern\fcharset0 Courier-Bold;
\f3\fnil\fcharset0 .SFNS-RegularItalic;\f4\fnil\fcharset0 .SFNS-Regular;\f5\fnil\fcharset0 .AppleSystemUIFontMonospaced-Regular;
\f6\fnil\fcharset0 .SFNS-Bold;\f7\fnil\fcharset0 .AppleSystemUIFontMonospaced-RegularItalic;\f8\fnil\fcharset0 HelveticaNeue-Bold;
}
{\colortbl;\red255\green255\blue255;\red135\green5\blue129;\red0\green0\blue0;\red181\green0\blue19;
\red14\green14\blue14;\red20\green0\blue196;\red111\green90\blue30;\red13\green100\blue1;}
{\*\expandedcolortbl;;\cssrgb\c60784\c13725\c57647;\csgray\c0;\cssrgb\c76863\c10196\c8627;
\cssrgb\c6700\c6700\c6700;\cssrgb\c10980\c0\c81176;\cssrgb\c51373\c42353\c15686;\cssrgb\c0\c45490\c0;}
\paperw11900\paperh16840\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\pard\tx560\tx1120\tx1680\tx2240\tx2800\tx3360\tx3920\tx4480\tx5040\tx5600\tx6160\tx6720\sl324\slmult1\pardirnatural\partightenfactor0

\f0\fs24 \cf0 \
\
\pard\tx560\tx1120\tx1680\tx2240\tx2800\tx3360\tx3920\tx4480\tx5040\tx5600\tx6160\tx6720\pardirnatural\partightenfactor0

\f1\fs28 \cf2 # Statistics Quiz \uc0\u55357 \u56541 \cf3 \
\
A lightweight multiple-choice quiz program that helps you review\
introductory statistics concepts.  \
Developed as the 
\f2\b **COMP9001 Python Project Challenge (5 %)**
\f1\b0  to\
demonstrate object-oriented design, file I/O, simple data analytics and a\
GUI built purely with Tkinter.\
\
---\
\
\cf2 ## 1 \'b7 Quick Start\cf3 \
\
\cf4 ```bash\
# clone / unzip the project, then:\
cd stat_quiz_project_v3\
\
# install runtime dependencies\
pip install matplotlib          # Tkinter is pre-installed with Python\
\
# launch\
python main.py
\f0\fs24 \cf0 \
\
\pard\tx560\tx1120\tx1680\tx2240\tx2800\tx3360\tx3920\tx4480\tx5040\tx5600\tx6160\tx6720\sl324\slmult1\pardirnatural\partightenfactor0

\f3\i\fs28 \cf5 Python 3.9 or newer is recommended.
\f4\i0 \
On macOS, if the GUI fails to open, run 
\f5 brew reinstall python-tk
\f4 .\
\pard\tx560\tx1120\tx1680\tx2240\tx2800\tx3360\tx3920\tx4480\tx5040\tx5600\tx6160\tx6720\pardirnatural\partightenfactor0

\f0\fs24 \cf0 \
\uc0\u11835 \
\pard\tx560\tx1120\tx1680\tx2240\tx2800\tx3360\tx3920\tx4480\tx5040\tx5600\tx6160\tx6720\sl324\slmult1\pardirnatural\partightenfactor0

\f4\fs28 \cf5 \
\pard\tx560\tx1120\tx1680\tx2240\tx2800\tx3360\tx3920\tx4480\tx5040\tx5600\tx6160\tx6720\sl324\slmult1\pardirnatural\partightenfactor0

\f6\b\fs34 \cf5 2 \'b7 Folder Layout
\f0\b0\fs24 \cf0 \
\
\pard\tx560\tx1120\tx1680\tx2240\tx2800\tx3360\tx3920\tx4480\tx5040\tx5600\tx6160\tx6720\pardirnatural\partightenfactor0

\f1\fs28 \cf3 .\
\uc0\u9500 \u9472  main.py                 # entry point\
\uc0\u9500 \u9472  login.py\
\uc0\u9500 \u9472  main_menu.py\
\uc0\u9500 \u9472  quiz_game.py            # quiz & wrong-question windows\
\uc0\u9500 \u9472  stats.py                # accuracy charts (Matplotlib)\
\uc0\u9500 \u9472  question_bank.py\
\uc0\u9500 \u9472  user_manager.py\
\uc0\u9500 \u9472  data/\
\uc0\u9474    \u9500 \u9472  banks/\
\uc0\u9474    \u9474    \u9492 \u9472  statistics.json   # \cf6 50\cf3  unique questions\
\uc0\u9474    \u9492 \u9472  users/                # generated per-user at runtime\
\uc0\u9492 \u9472  README.md
\f0\fs24 \cf0 \
\
\pard\tx560\tx1120\tx1680\tx2240\tx2800\tx3360\tx3920\tx4480\tx5040\tx5600\tx6160\tx6720\sl324\slmult1\pardirnatural\partightenfactor0

\f3\i\fs28 \cf5 Deleting 
\f7 data/users/
\f3  resets all user progress.
\f4\i0 \
\pard\tx560\tx1120\tx1680\tx2240\tx2800\tx3360\tx3920\tx4480\tx5040\tx5600\tx6160\tx6720\pardirnatural\partightenfactor0

\f0\fs24 \cf0 \
\uc0\u11835 \
\pard\tx560\tx1120\tx1680\tx2240\tx2800\tx3360\tx3920\tx4480\tx5040\tx5600\tx6160\tx6720\sl324\slmult1\pardirnatural\partightenfactor0

\f4\fs28 \cf5 \
\pard\tx560\tx1120\tx1680\tx2240\tx2800\tx3360\tx3920\tx4480\tx5040\tx5600\tx6160\tx6720\sl324\slmult1\pardirnatural\partightenfactor0

\f6\b\fs34 \cf5 3 \'b7 Key Features
\f0\b0\fs24 \cf0 \
\
\pard\tx560\tx1120\tx1680\tx2240\tx2800\tx3360\tx3920\tx4480\tx5040\tx5600\tx6160\tx6720\sl324\slmult1\pardirnatural\partightenfactor0

\f6\b\fs26 \cf5 Function
\f0\b0\fs24 \cf0 	
\f6\b\fs26 \cf5 Details
\f0\b0\fs24 \cf0 \
\pard\tx560\tx1120\tx1680\tx2240\tx2800\tx3360\tx3920\tx4480\tx5040\tx5600\tx6160\tx6720\sl324\slmult1\pardirnatural\partightenfactor0

\f8\b\fs26 \cf5 Login / Register
\f0\b0\fs24 \cf0 	
\f4\fs26 \cf5 Enter any username \uc0\u8594  profile auto-created
\f0\fs24 \cf0 \

\f8\b\fs26 \cf5 Random Quiz
\f0\b0\fs24 \cf0 	
\f4\fs26 \cf5 10 questions per session, instant \'93Correct / Incorrect\'94 pop-ups
\f0\fs24 \cf0 \

\f8\b\fs26 \cf5 Wrong-Question Redo
\f0\b0\fs24 \cf0 	
\f4\fs26 \cf5 Loops until every wrong question is answered correctly (or you exit)
\f0\fs24 \cf0 \

\f8\b\fs26 \cf5 Persistent Storage
\f0\b0\fs24 \cf0 	
\f4\fs26 \cf5 User history & wrong list saved as JSON
\f0\fs24 \cf0 \

\f8\b\fs26 \cf5 Statistics Dashboard
\f0\b0\fs24 \cf0 	
\f4\fs26 \cf5 Daily / Weekly / Monthly / Yearly accuracy with Matplotlib line chart (labels show attempts)
\f0\fs24 \cf0 \

\f8\b\fs26 \cf5 Finish & Save vs Exit
\f0\b0\fs24 \cf0 	
\f3\i\fs26 \cf5 Finish & Save
\f4\i0  records current progress; 
\f3\i Exit
\f4\i0  skips the current question and returns to menu
\f0\fs24 \cf0 \
\
\pard\tx560\tx1120\tx1680\tx2240\tx2800\tx3360\tx3920\tx4480\tx5040\tx5600\tx6160\tx6720\pardirnatural\partightenfactor0
\cf0 \
\uc0\u11835 \
\pard\tx560\tx1120\tx1680\tx2240\tx2800\tx3360\tx3920\tx4480\tx5040\tx5600\tx6160\tx6720\sl324\slmult1\pardirnatural\partightenfactor0

\f4\fs28 \cf5 \
\pard\tx560\tx1120\tx1680\tx2240\tx2800\tx3360\tx3920\tx4480\tx5040\tx5600\tx6160\tx6720\sl324\slmult1\pardirnatural\partightenfactor0

\f6\b\fs34 \cf5 4 \'b7 Editing the Question Bank
\f4\b0\fs28 \
\
Open 
\f5 data/banks/statistics.json
\f4 ; each object:
\f0\fs24 \cf0 \
\
\pard\tx560\tx1120\tx1680\tx2240\tx2800\tx3360\tx3920\tx4480\tx5040\tx5600\tx6160\tx6720\pardirnatural\partightenfactor0

\f1\fs28 \cf3 \{\
  \cf7 "question"\cf3 : \cf4 "Approximately what percentage of observations fall within \'b12\uc0\u963 ?"\cf3 ,\
  \cf7 "options"\cf3 : [\cf4 "68 %"\cf3 , \cf4 "95 %"\cf3 , \cf4 "99.7 %"\cf3 , \cf4 "50 %"\cf3 ],\
  \cf7 "answer"\cf3 : \cf6 1\cf3                \cf8 // zero-based index\cf3 \
\}
\f0\fs24 \cf0 \
\
\pard\tx560\tx1120\tx1680\tx2240\tx2800\tx3360\tx3920\tx4480\tx5040\tx5600\tx6160\tx6720\sl324\slmult1\pardirnatural\partightenfactor0

\f4\fs28 \cf5 Append or modify questions as needed.\
The app reloads the file at startup.\
\pard\tx560\tx1120\tx1680\tx2240\tx2800\tx3360\tx3920\tx4480\tx5040\tx5600\tx6160\tx6720\pardirnatural\partightenfactor0

\f0\fs24 \cf0 \
\uc0\u11835 \
\pard\tx560\tx1120\tx1680\tx2240\tx2800\tx3360\tx3920\tx4480\tx5040\tx5600\tx6160\tx6720\sl324\slmult1\pardirnatural\partightenfactor0

\f4\fs28 \cf5 \
\pard\tx560\tx1120\tx1680\tx2240\tx2800\tx3360\tx3920\tx4480\tx5040\tx5600\tx6160\tx6720\sl324\slmult1\pardirnatural\partightenfactor0

\f6\b\fs34 \cf5 5 \'b7 Troubleshooting
\f0\b0\fs24 \cf0 \
\
\pard\tx560\tx1120\tx1680\tx2240\tx2800\tx3360\tx3920\tx4480\tx5040\tx5600\tx6160\tx6720\sl324\slmult1\pardirnatural\partightenfactor0

\f6\b\fs26 \cf5 Issue
\f0\b0\fs24 \cf0 	
\f6\b\fs26 \cf5 Fix
\f0\b0\fs24 \cf0 \
\pard\tx560\tx1120\tx1680\tx2240\tx2800\tx3360\tx3920\tx4480\tx5040\tx5600\tx6160\tx6720\sl324\slmult1\pardirnatural\partightenfactor0

\f5\fs26 \cf5 ModuleNotFoundError: matplotlib
\f0\fs24 \cf0 	
\f5\fs26 \cf5 pip install matplotlib
\f0\fs24 \cf0 \
\pard\tx560\tx1120\tx1680\tx2240\tx2800\tx3360\tx3920\tx4480\tx5040\tx5600\tx6160\tx6720\sl324\slmult1\pardirnatural\partightenfactor0

\f4\fs26 \cf5 Tk window too small / font tiny on Mac
\f0\fs24 \cf0 	
\f5\fs26 \cf5 brew reinstall python-tk
\f0\fs24 \cf0 \

\f4\fs26 \cf5 Statistics chart window empty
\f0\fs24 \cf0 	
\f4\fs26 \cf5 Make sure you have completed at least one quiz so history exists
\f0\fs24 \cf0 \
\
\pard\tx560\tx1120\tx1680\tx2240\tx2800\tx3360\tx3920\tx4480\tx5040\tx5600\tx6160\tx6720\pardirnatural\partightenfactor0
\cf0 \
\uc0\u11835 \
\pard\tx560\tx1120\tx1680\tx2240\tx2800\tx3360\tx3920\tx4480\tx5040\tx5600\tx6160\tx6720\sl324\slmult1\pardirnatural\partightenfactor0

\f4\fs28 \cf5 \
\pard\tx560\tx1120\tx1680\tx2240\tx2800\tx3360\tx3920\tx4480\tx5040\tx5600\tx6160\tx6720\sl324\slmult1\pardirnatural\partightenfactor0

\f6\b\fs34 \cf5 6 \'b7 License
\f4\b0\fs28 \
\
MIT \'97 feel free to fork / adapt for educational purposes.\
\pard\tx560\tx1120\tx1680\tx2240\tx2800\tx3360\tx3920\tx4480\tx5040\tx5600\tx6160\tx6720\pardirnatural\partightenfactor0

\f0\fs24 \cf0 \
}