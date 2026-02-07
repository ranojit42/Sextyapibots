from bots_data import bots
import json
from urllib.parse import unquote

def handler(request):
    # Vercel passes query params as request['query'] or request.GET
    username = request.GET.get('username', '').lower().replace('@','')
    
    for bot in bots:
        if bot["username"].lower().replace("@","") == username:
            return {
                "statusCode": 200,
                "headers": { "Content-Type": "application/json" },
                "body": json.dumps(bot)
            }
    
    # Not found → return all bots panel HTML
    from flask import render_template_string
    from pathlib import Path

    html_file = Path(__file__).parent.parent / "templates" / "panel.html"
    html_content = html_file.read_text(encoding="utf-8")
    return {
        "statusCode": 200,
        "headers": { "Content-Type": "text/html" },
        "body": html_content
    }