import os

# Define your affiliate ID
affiliate_id = '2013017799'  # Replace with your actual affiliate ID

# Define the path to your directory containing HTML files
directory = './your-website-folder'

# Function to update links in the HTML file
def update_affiliate_links(file_path, affiliate_id):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # Replace placeholder with your affiliate link
    content = content.replace("YOUR_AFFILIATE_ID_PLACEHOLDER", affiliate_id)
    
    # Cross-linking: You can add more links to related blog posts here
    content = content.replace("<a href='/related-post1'>", "<a href='/related-post1' title='Related post 1'>")
    content = content.replace("<a href='/related-post2'>", "<a href='/related-post2' title='Related post 2'>")

    # SEO optimization: Add meta description, keywords, etc.
    meta_description = "Send same-day flowers today with guaranteed delivery from Floristone. Order now through our exclusive affiliate link."
    meta_keywords = "same-day flowers, send flowers, flower delivery, Floristone, same-day delivery"

    content = content.replace("<head>", f"<head>\n    <meta name='description' content='{meta_description}'>\n    <meta name='keywords' content='{meta_keywords}'>")
    
    # Cross-link related pages for better SEO
    content = content.replace("</body>", """
    <a href="/page1" rel="noopener noreferrer" title="Check out our latest flower arrangements!">Our New Flower Arrangements</a>
    <a href="/page2" rel="noopener noreferrer" title="Learn about the benefits of same-day flower delivery">Why Same-Day Delivery?</a>
    </body>""")
    
    # Save the updated content
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(content)

# Loop through all HTML files in the specified directory
for filename in os.listdir(directory):
    if filename.endswith(".html"):
        file_path = os.path.join(directory, filename)
        update_affiliate_links(file_path, affiliate_id)
        print(f"Updated affiliate links and SEO for: {filename}")
