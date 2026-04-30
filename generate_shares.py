import os

AVATAR_MAP = {
    "avatar_01": {"name": "Avocado", "subtitle": "The Complete Package", "emoji": "🥑"},
    "avatar_02": {"name": "Blueberry", "subtitle": "The Spontaneous Foodie", "emoji": "🫐"},
    "avatar_03": {"name": "Broccoli", "subtitle": "The Devoted Classic", "emoji": "🥦"},
    "avatar_04": {"name": "Strawberry", "subtitle": "The Loyal Home Cook", "emoji": "🍓"},
    "avatar_05": {"name": "Onion", "subtitle": "The Disciplined Explorer", "emoji": "🧅"},
    "avatar_06": {"name": "Cheese", "subtitle": "The Social Foodie", "emoji": "🧀"},
    "avatar_07": {"name": "Garlic", "subtitle": "The Devoted Planner", "emoji": "🧄"},
    "avatar_08": {"name": "Mushroom", "subtitle": "The Quiet Technician", "emoji": "🍄"},
    "avatar_09": {"name": "Tomato", "subtitle": "The Passionate Planner Who Outsources The Cooking", "emoji": "🍅"},
    "avatar_10": {"name": "Apple", "subtitle": "The Inspired Improviser", "emoji": "🍎"},
    "avatar_11": {"name": "Carrot", "subtitle": "The Thoughtful Organiser", "emoji": "🥕"},
    "avatar_12": {"name": "Celery", "subtitle": "The Minimalist", "emoji": "🥬"},
    "avatar_13": {"name": "Chocolate", "subtitle": "The Discerning Planner", "emoji": "🍫"},
    "avatar_14": {"name": "Ice Cream", "subtitle": "The Inspired Chaos Agent", "emoji": "🍦"},
    "avatar_15": {"name": "Pizza", "subtitle": "The Universal Crowd-Pleaser", "emoji": "🍕"},
    "avatar_16": {"name": "French Fry", "subtitle": "Gloriously, Peacefully Unhinged", "emoji": "🍟"},
}

BASE_URL = "https://forkcast.me/foodsona"

def generate_share_pages():
    share_dir = "share"
    if not os.path.exists(share_dir):
        os.makedirs(share_dir)

    template = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>{title}</title>
  
  <!-- Open Graph / Facebook -->
  <meta property="og:type" content="website">
  <meta property="og:url" content="{share_url}">
  <meta property="og:title" content="{title}">
  <meta property="og:description" content="{description}">
  <meta property="og:image" content="{image_url}">

  <!-- Twitter -->
  <meta property="twitter:card" content="summary_large_image">
  <meta property="twitter:url" content="{share_url}">
  <meta property="twitter:title" content="{title}">
  <meta property="twitter:description" content="{description}">
  <meta property="twitter:image" content="{image_url}">

  <style>
    body {{ font-family: sans-serif; display: flex; align-items: center; justify-content: center; height: 100vh; background: #FFF6E5; color: #630E03; text-align: center; padding: 20px; margin:0; }}
    .loader {{ border: 4px solid #F9DAB7; border-top: 4px solid #F2A93B; border-radius: 50%; width: 40px; height: 40px; animation: spin 1s linear infinite; margin: 0 auto 20px; }}
    @keyframes spin {{ 0% {{ transform: rotate(0deg); }} 100% {{ transform: rotate(360deg); }} }}
    a {{ color: #F2A93B; text-decoration: none; font-weight: bold; }}
  </style>

  <script>
    window.location.href = "/foodsona/?foodsona={avatar_id}";
  </script>
</head>
<body>
  <div>
    <div class="loader"></div>
    <h1>Loading your Foodsona...</h1>
    <p>If you are not redirected, <a href="/foodsona/?foodsona={avatar_id}">click here</a>.</p>
  </div>
</body>
</html>"""

    for avatar_id, data in AVATAR_MAP.items():
        title = f"I'm a {data['name']}! {data['emoji']} | Forkcast Foodsona"
        description = f"I discovered my Foodsona: {data['name']} ({data['subtitle']}). Take the quiz and find yours! 🥑✨"
        image_url = f"{BASE_URL}/assets/{avatar_id}.png"
        share_url = f"{BASE_URL}/share/{data['name'].lower().replace(' ', '')}.html"

        content = template.format(
            title=title,
            description=description,
            image_url=image_url,
            share_url=share_url,
            avatar_id=avatar_id
        )

        filename = f"{data['name'].lower().replace(' ', '')}.html"
        filepath = os.path.join(share_dir, filename)
        
        with open(filepath, "w") as f:
            f.write(content)
        print(f"Generated {filepath}")

if __name__ == "__main__":
    generate_share_pages()
