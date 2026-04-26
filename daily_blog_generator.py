import datetime
import random

# Define content pieces for the blog
titles = [
    "Why Same-Day Flower Delivery Is a Game-Changer for Last-Minute Gifts",
    "Send Flowers Today: Guaranteed Same-Day Delivery with FloriStone",
    "Fresh Flowers, Delivered Same Day: The Benefits of Same-Day Delivery",
    "How FloriStone Makes Last-Minute Flower Orders Effortless"
]

intro_paragraphs = [
    "Looking for a quick way to brighten someone's day? FloriStone offers fast, reliable same-day flower delivery so you never miss an opportunity to send a thoughtful gift.",
    "Need to send flowers today? FloriStone guarantees same-day delivery on a wide variety of stunning bouquets. Whether it's a birthday or a special occasion, we've got you covered.",
    "When it comes to expressing your feelings, flowers are a timeless gift. With FloriStone's same-day delivery, you can be sure that your flowers will arrive fresh and on time.",
    "Life can get busy, but that doesn't mean you have to miss out on sending a thoughtful gift. With FloriStone’s same-day delivery service, you can send flowers right away!"
]

why_choose_floriStone = [
    "Fast, reliable service with guaranteed same-day delivery.",
    "Wide selection of beautiful bouquets for any occasion.",
    "Secure online ordering process for your convenience.",
    "Competitive pricing with exclusive offers through our affiliate link."
]

how_to_order = [
    "Browse FloriStone's wide selection of same-day flowers.",
    "Select the perfect bouquet for your loved one.",
    "Ensure your order is placed by 2:00 PM local time for same-day delivery.",
    "Complete your purchase securely through our affiliate link."
]

# Get today's date
today = datetime.date.today()

# Format the content
blog_title = random.choice(titles)
intro = random.choice(intro_paragraphs)
why_floriStone = random.choice(why_choose_floriStone)
order_steps = random.choice(how_to_order)

# Prepare content for the blog
blog_content = f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="Send same-day flowers to your loved ones. Fast, reliable delivery with guaranteed on-time service. Order today through FloriStone!">
    <meta name="keywords" content="same-day flowers, flower delivery, same-day flower delivery, send flowers today, same-day delivery, flowers for any occasion">
    <title>{blog_title} - Send Same-Day Flowers with FloriStone</title>
    <style>
        body {{
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 0;
            background-color: #f7f7f7;
            color: #333;
        }}
        header {{
            background-color: #003366;
            color: white;
            padding: 20px;
            text-align: center;
        }}
        header h1 {{
            margin: 0;
            font-size: 36px;
        }}
        .container {{
            width: 80%;
            margin: 0 auto;
            padding: 20px;
        }}
        .section {{
            margin-bottom: 30px;
        }}
        .section h2 {{
            color: #003366;
        }}
        .section p {{
            font-size: 16px;
            line-height: 1.6;
        }}
        .cta-button {{
            background-color: #FF2E63;
            color: white;
            padding: 15px 25px;
            font-size: 18px;
            text-decoration: none;
            border-radius: 5px;
            display: inline-block;
            margin-top: 20px;
        }}
        .cta-button:hover {{
            background-color: #E02456;
        }}
        footer {{
            background-color: #003366;
            color: white;
            text-align: center;
            padding: 15px;
            position: relative;
            bottom: 0;
            width: 100%;
        }}
    </style>
</head>
<body>

<header>
    <h1>{blog_title}</h1>
</header>

<div class="container">

    <div class="section">
        <h2>Send Flowers Today with Same-Day Delivery!</h2>
        <p>{intro}</p>
        <p><strong>Order now and send flowers instantly! Same-day delivery with FloriStone.</strong></p>
        <a href="https://www.floristone.com/main.cfm?occ=sd&source_id=aff&AffiliateID=2013017799" class="cta-button" target="_blank">Order Same-Day Flowers Now</a>
    </div>

    <div class="section">
        <h2>Why Choose FloriStone for Same-Day Flower Delivery?</h2>
        <ul>
            <li><strong>{why_floriStone}</strong></li>
        </ul>
        <a href="https://www.floristone.com/main.cfm?occ=sd&source_id=aff&AffiliateID=2013017799" class="cta-button" target="_blank">Send Flowers Today!</a>
    </div>

    <div class="section">
        <h2>How to Order Same-Day Flowers</h2>
        <ol>
            <li>{order_steps}</li>
        </ol>
        <p><strong>Don’t miss out! Order now for same-day flower delivery and brighten someone's day!</strong></p>
        <a href="https://www.floristone.com/main.cfm?occ=sd&source_id=aff&AffiliateID=2013017799" class="cta-button" target="_blank">Order Same-Day Flowers Now</a>
    </div>

</div>

<footer>
    <p>&copy; {today.year} Send Flowers Online. All rights reserved. Delivered by FloriStone.</p>
</footer>

</body>
</html>
"""

# Save the blog content to a file
blog_filename = f"daily_blog_{today}.html"
with open(blog_filename, 'w') as blog_file:
    blog_file.write(blog_content)

print(f"Daily blog post for {today} generated successfully: {blog_filename}")
