import mysql.connector

# Connect to MySQL
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Chiluveri@123",  # Replace with your MySQL password
    database="blog_db"
)
cursor = conn.cursor()

def create_post():
    title = input("Enter post title: ")
    content = input("Enter post content: ")
    tags_input = input("Enter tags (comma-separated): ")
    tags = [tag.strip() for tag in tags_input.split(',')]

    # Insert post
    cursor.execute("INSERT INTO posts (title, content) VALUES (%s, %s)", (title, content))
    post_id = cursor.lastrowid

    # Handle tags
    for tag in tags:
        cursor.execute("SELECT id FROM tags WHERE name = %s", (tag,))
        result = cursor.fetchone()
        if result:
            tag_id = result[0]
        else:
            cursor.execute("INSERT INTO tags (name) VALUES (%s)", (tag,))
            tag_id = cursor.lastrowid

        cursor.execute("INSERT INTO post_tags (post_id, tag_id) VALUES (%s, %s)", (post_id, tag_id))

    conn.commit()
    print("Post created successfully!\n")

def view_all_titles():
    cursor.execute("SELECT title FROM posts")
    posts = cursor.fetchall()
    if posts:
        print("Post Titles:")
        for (title,) in posts:
            print(f"- {title}")
    else:
        print("No posts found.")
    print()

def view_post_by_title():
    title = input("Enter post title to view: ")
    cursor.execute("SELECT content FROM posts WHERE title = %s", (title,))
    result = cursor.fetchone()
    if result:
        print(f"\nContent:\n{result[0]}")
    else:
        print("Post not found.")
    print()

def search_posts_by_tag():
    tag = input("Enter tag to search posts: ").strip()
    cursor.execute("""
        SELECT posts.title 
        FROM posts 
        JOIN post_tags ON posts.id = post_tags.post_id
        JOIN tags ON tags.id = post_tags.tag_id
        WHERE tags.name = %s
    """, (tag,))
    results = cursor.fetchall()
    if results:
        print("Posts with tag:", tag)
        for (title,) in results:
            print(f"- {title}")
    else:
        print("No posts found for this tag.")
    print()

def main():
    while True:
        print("=== Blog Manager ===")
        print("1. Create a new post")
        print("2. View all post titles")
        print("3. View post content by title")
        print("4. Search posts by tag")
        print("5. Exit")
        choice = input("Choose an option (1-5): ")

        if choice == '1':
            create_post()
        elif choice == '2':
            view_all_titles()
        elif choice == '3':
            view_post_by_title()
        elif choice == '4':
            search_posts_by_tag()
        elif choice == '5':
            break
        else:
            print("Invalid choice, try again.\n")

if __name__ == "__main__":
    main()
