- beadunk egy x órás kampány felvételt
- use casek:
	1. beszélünk hozzá
	2. foglalja össze az eddigi történéseket
	3. rajzolja le, amikor harcoltunk XY-nal
	4. csináljon egy térképet, merre jártunk
	5. (szabálykérdések)

# To use:
```
python -m pip install -r requirements.txt
python -m chainlit run dnd_chatbot.py
```
# The files
We have 2 custom made Langchain tools: 
 * `text_summarization_tool`: this tool extracts information from the transcript of the role playing session that is relevant to the user query
 * `image_generation_tool`: this tool generates an image based on the passed text

With these tools, we create a Langchain ReAct agent, and built a chainlit frontend for it.
