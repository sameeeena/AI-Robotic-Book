import os
import requests
import frontmatter
import glob

def extract_text_from_markdown(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Use frontmatter library to parse frontmatter and content
        try:
            post = frontmatter.loads(content)
            # Extract content, ignoring any YAML frontmatter
            text_content = post.content
        except Exception:
            # If frontmatter parsing fails, assume no frontmatter
            text_content = content
        
        # Further cleanup: remove code blocks, multiple newlines, etc.
        lines = text_content.splitlines()
        cleaned_lines = []
        in_code_block = False
        for line in lines:
            if line.strip().startswith('```'):
                in_code_block = not in_code_block
                continue # Skip code block delimiters
            if not in_code_block:
                cleaned_lines.append(line)
        
        cleaned_text = '\n'.join(cleaned_lines)
        # Remove excessive newlines and trim whitespace
        cleaned_text = os.linesep.join([s for s in cleaned_text.splitlines() if s])
        return cleaned_text.strip()
    except Exception as e:
        print(f"Error reading {file_path}: {e}")
        return None

def embed_text_via_api(text, filename, embed_url="http://localhost:8000/embed"):
    headers = {"Content-Type": "application/json"}
    # Prepend filename to text for better searchability
    enriched_text = f"Source: {filename}\n\n{text}"
    payload = {"text": enriched_text}
    try:
        response = requests.post(embed_url, json=payload, headers=headers)
        response.raise_for_status()  # Raise an exception for HTTP errors
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error embedding text: {e}")
        return None

if __name__ == '__main__':
    # Adjust path to point to docusauras/docs which contains all modules
    script_dir = os.path.dirname(__file__)
    docs_path = os.path.abspath(os.path.join(script_dir, '..', '..', 'docusauras', 'docs'))
    
    print(f"Searching for chapters in {docs_path}...")
    
    # Find all .md files in all subdirectories of docs_path
    chapter_files = glob.glob(os.path.join(docs_path, '**', '*.md'), recursive=True)

    print(f"Found {len(chapter_files)} chapters.")
    
    success_count = 0
    for file_path in chapter_files:
        filename = os.path.basename(file_path)
        print(f"Processing {filename}...")
        
        extracted_text = extract_text_from_markdown(file_path)
        
        if extracted_text:
            # Split large texts into smaller chunks (Docusaurus chapters are manageable)
            embedding_response = embed_text_via_api(extracted_text, filename)
            if embedding_response:
                print(f"Successfully embedded '{filename}'.")
                success_count += 1
            else:
                print(f"Failed to embed '{filename}'.")
        else:
            print(f"No extractable text from '{filename}'.")
    
    print(f"Embedding process complete. Successfully embedded {success_count}/{len(chapter_files)} chapters.")