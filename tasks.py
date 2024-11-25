from celery_app import celery
from googletrans import Translator, LANGUAGES
import logging

# Setup logging untuk debugging
logging.basicConfig(level=logging.INFO)

@celery.task
def translate_text(text, src_lang, dest_lang):
    """
    Tugas untuk menerjemahkan teks dari satu bahasa ke bahasa lain.
    Menambahkan penanganan kesalahan dan validasi bahasa.
    """
    # Validasi bahasa yang digunakan
    if src_lang not in LANGUAGES or dest_lang not in LANGUAGES:
        return {'error': 'Invalid source or destination language.'}
    
    try:
        translator = Translator()
        result = translator.translate(text, src=src_lang, dest=dest_lang)

        # Menambahkan log untuk melacak hasil terjemahan
        logging.info(f"Translation result: {result}")

        # Periksa apakah hasil terjemahan tidak None
        if result and hasattr(result, 'text'):
            return result.text
        else:
            return {'error': 'Failed to get a valid translation result.'}

    except Exception as e:
        # Menangani kesalahan jaringan atau kesalahan lainnya
        logging.error(f"An error occurred: {str(e)}")
        return {'error': f'An error occurred: {str(e)}'}
