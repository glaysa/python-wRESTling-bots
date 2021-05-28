START py -m venv myvenv
CMD .\myvenv\Scripts\activate.bat
CMD pip install -r requirements.txt
CMD py main.py
PAUSE
