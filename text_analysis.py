import sys

def text_analysis(filename):
    try:
        with open(filename, 'r') as f:
            file = str(f.readlines()).lower()
            lines = len(file.split('\\n'))
            letters = len(file)
            file.replace('.', '')
            file.replace(',', '')
            words = file.split(' ')
            characters = len(words)
            average_length_word = int(sum(len(word) for word in words) / characters)
            unique_words = set(words)
            populations = {}
            for word in unique_words:
                populations[word] = words.count(word)
            most_popular_words = sorted(populations.items(), key=lambda x: x[1], reverse=True)
            most_popular_10 = most_popular_words[:10]
            return f'In this file you have:\n{lines} : lines\n{letters} : letters\n{characters} : characters\nthe average word length is : {average_length_word}\n10 Most popular words are : {most_popular_10}' 
    except FileNotFoundError:
        return f"Can not find a {filename}"

if __name__ == '__main__':
    if len(sys.argv) > 1:
        filename = sys.argv[1]
        print(text_analysis(filename))
    else:
        print('Enter a filename as argument.')
