# Local AI iframe HTML viewer

## Description

This project was made for the course DES8105 Web Product Design (互联网产品设计) at Shanghai Jiao Tong University. The critera was as follows:
- replicate the interface of an existing web product (e.g. WeChat),
- modify part of the interface,
- add AI chat function and explain the reasons for the modification;
- submit a Figma design plan, executable code (if you feel AIGC programming is too difficult for you, just skip it)[...]

The existing web product I chose is the try it function on [www.w3schools.com](https://www.w3schools.com/html/tryit.asp?filename=tryhtml_basic)

Figma prototype below: 

[![AI-iframe-viewer](https://github.com/user-attachments/assets/007692fc-9b5d-497c-a9f6-2fc0b2ee29da)](https://www.figma.com/proto/LG4OiGRPa7dVepRjOomGWj/AI-iframe-viewer?node-id=0-1&t=utdk5RwAAbr0Hf13-1)


This is a python HTTP server programme with the following features:

1. When the user accesses the localhost:8080 through the browser they will see the fontend with a dialogue box with a coversation box (to speak with local AI) and an iframe box (to preview the HTML).
2. When the user enters text into the conversation inputbox the text will be sent to the local python server which runs granite-code using Ollama. The ouput is then displayed in the conversation record box and the HTML in the most recent reply is previewed in the iframe box. The default comment is as follows:

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
4. After the python server recives the Ollama reply it will then send the reply the fontend programme. The full text will be sent to the dialogue box. The HTML will be send to the iframe box.
5. After the front end recives the reply it will display the full reply in the dialogue box and the HTML in the iframe box.
6. The conversation dialogue box will display all the conversation texts in a chronological order with time records. The iframe box will display the HTML from the most recent post.

## Set up IBM granite-code using Ollama

```
sudo pacman -Sy ollama 
ollama serve &> /dev/null &
ollama run granite-code &> /dev/null &
```

## Setup the localhost 

```
git clone 'https://github.com/cwzialor/AI-iframe-viewer.git'

cd 'AI-iframe-viewer'

chmod +x server.py

python ./server.py &> /dev/null &
```

In your browser go to `http://localhost:8080/` to start.


