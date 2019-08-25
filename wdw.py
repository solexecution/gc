from urllib.request import urlopen
with urlopen('https://www.redkiteintelligence.com/careers') as story:
   story_words = []
   for line in story:
      line_words = line.split()
      for word in line_words:
          story_words.append(word)
print(story_words)
