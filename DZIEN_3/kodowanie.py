import chardet

def detect_encoding(file_path):
    with open(file_path, 'rb') as file:
        raw_data = file.read()
        result = chardet.detect(raw_data)
        encoding = result['encoding']
        confidence = result['confidence']
        
        print(f"Wykryte kodowanie: {encoding}")
        print(f"Pewność: {confidence:.2%}")
        return encoding

# Przykład użycia
file_path = "mojedane/movies.dat"
detect_encoding(file_path)
