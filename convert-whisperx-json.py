import json
import sys

doublefps=False

file=sys.argv[1]
if (len(file)<2):
	print("no file!")
with open("whisperx/"+file+".json", 'r') as fileh:
	whisperjson = json.load(fileh)

for s in whisperjson['segments']:
	s['text']=s['text'].lower()
	s['content']=s['text']
	
	try:
		if doublefps:
			s['start']=0.5*s['start']
			s['end']=0.5*s['end']
	except:
		pass
	
	words=[]
	for w in s['words']:
		try:
			if doublefps:
				w['start']=0.5*w['start']
				w['end']=0.5*w['end']
		except:
			pass
		
		try:
			w['word']=w['word'].lower()
			words.append(w)
		except:
			#print(w)
			pass
		
		try:
			w['conf']=w['score']
			words.append(w)
		except:
			#print(w)
			pass
	s['words']=words

jsonstring=json.dumps(whisperjson['segments'])
text_file = open(file+".json", "w")
text_file.write(jsonstring)
text_file.close()

print("Done.")