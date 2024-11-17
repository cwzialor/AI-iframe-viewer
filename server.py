import http.server
import socketserver
import json
import subprocess
import requests

PORT = 8080

class RequestHandler(http.server.SimpleHTTPRequestHandler):
    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)
        user_input = json.loads(post_data.decode('utf-8'))['text']

        # Call Ollama with the user input
        ollama_response = self.call_ollama(user_input)

        # Send response back to the client
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        self.wfile.write(json.dumps(ollama_response).encode('utf-8'))

    def call_ollama(self, text):
        url = "http://127.0.0.1:11434/api/chat"
        payload = {
            "model": "granite-code",
            "messages": [
                {
                    "role": "system",
                    "content": "You are a web development assistant. When asked about HTML, provide working code examples."
                },
                { "role": "user", "content": text }
            ],
            "stream": False
        }
        
        try:
            response = requests.post(url, json=payload)
            response.raise_for_status()
            data = response.json()
            
            # Extract the message content from Ollama's response
            response_text = data.get("message", {}).get("content", "No response")
            
            # Look for HTML code blocks in the response
            html_content = response_text
            if "```html" in response_text.lower():
                # Extract HTML between ```html and ``` tags
                start = response_text.lower().find("```html") + 7
                end = response_text.find("```", start)
                if end != -1:
                    html_content = response_text[start:end].strip()
            else:
                # Wrap non-HTML responses in basic HTML structure
                html_content = f"""
                <!DOCTYPE html>
                <html>
                <head>
                    <meta charset="UTF-8">
                    <title>Response</title>
                </head>
                <body>
                    <p>{html_content}</p>
                </body>
                </html>
                """
            
            # Ensure the HTML content is properly formatted
            if not html_content.strip().startswith('<!DOCTYPE'):
                html_content = f"""
                <!DOCTYPE html>
                <html>
                <head>
                    <meta charset="UTF-8">
                    <title>Response</title>
                </head>
                <body>
                    {html_content}
                </body>
                </html>
                """
            
            return {
                "full_text": response_text,
                "html": html_content.strip()  # Remove extra whitespace
            }
        except requests.exceptions.RequestException as e:
            print(f"Error communicating with Ollama: {e}")
            return {
                "full_text": f"Error communicating with Ollama: {e}",
                "html": f"<p>Error occurred: {e}</p>"
            }

with socketserver.TCPServer(("", PORT), RequestHandler) as httpd:
    print(f"Serving on port {PORT}")
    httpd.serve_forever() 