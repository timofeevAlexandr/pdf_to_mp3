from pathlib import Path

from gtts import gTTS
from art import tprint
import pdfplumber


def pdf_to_mp3(file_path:str, language:str ='en') -> str:
    if Path(file_path).is_file() and Path(file_path).suffix == '.pdf':
        # File exists.
        print(f'[+] Original name {file_path}')
        print('[+] Processing...')
        with pdfplumber.PDF(open(file=file_path, mode='rb')) as pdf:
            pages = [page.extract_text() for page in pdf.pages]
        text = '.'.join(pages)
        text = text.replace('\n', '')
        my_audio = gTTS(text=text, lang=language, slow=false)
        file_name = Path(file_path).stem
        my_audio.save(f'{file_name}.mp3')
        return f'[+] {file_name}.mp3 saved successfully...'
    else:
        return 'File not exists'

def main():
    tprint('PDF_TO_MP3', font='bulbhead')
    file_path = input('\nEnter PDF file path:')
    language = input('Enter PDF language. Example: en, ru:')
    pdf_to_mp3(file_path, language)

if __name__ == 'main':
    main()