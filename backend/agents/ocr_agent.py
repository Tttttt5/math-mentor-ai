import easyocr

# Load OCR model once
reader = easyocr.Reader(['en'])


def extract_text_from_image(image_path):

    try:

        results = reader.readtext(image_path)

        extracted_words = []

        for bbox, text, confidence in results:
            extracted_words.append(text)

        extracted_text = " ".join(extracted_words)

        print("OCR RESULT:", extracted_text)

        if len(extracted_text.strip()) < 3:
            return "", True

        return extracted_text, False

    except Exception as e:

        print("OCR ERROR:", e)

        return "", True