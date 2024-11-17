Create a similar page by coding a python HTTP server programme with the following requirements:
1. When the user accesses the localhost:8080 through the browser they will see the fontend. The frontend using html, tailwindcss and iframe. On the left, the fontend will have a dialogue box with a coversation input box at the bottom and a conversation record box at the top. One the right, the front end will have a iframe box.
2. When the user enters text into the conversation inputbox the text will be sent to the local python server which runs granite-code using Ollama. The ouput is then displayed in the conversation record box and the HTML, CSS and JavaScript in the most recent reply is previewed in the iframe box. The default comment is as follows:
```HTML
<!DOCTYPE html>
<html>
<head>
<title>Page Title</title>
</head>
<body>

<h1>This is a Heading</h1>
<p>This is a paragraph.</p>

</body>
</html>
```

3. After the python server recives the text, it will be sent to Ollama installed on the local machine and wait for Ollama to reply.
4. After the python server recives the Ollama reply it will then send the reply the fontend programme. The full text will be sent to the dialogue box. The HTML, CSS and JavaScript will be send to the iframe box.
5. After the front end recives the reply it will display the full reply in the dialogue box and the HTML, CSS and JavaScript in the iframe box.
6. The conversation dialo9gue box will display all the conversation texts in a chronological order with time records. The iframe box will display the HTML, CSS and JavaScript from the most recent post.




