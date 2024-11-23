def markdown_to_blocks(markdown):
    blocks = markdown.split("\n\n")
    cleaned_blocks = []
    for block in blocks:
        cleaned_block = block.strip()
        if cleaned_block:
            cleaned_blocks.append(cleaned_block)
    return cleaned_blocks

def block_to_block_type(cleaned_blocks):
    block_type = []
    for cleaned_block in cleaned_blocks:
        if cleaned_block.startswith('#') and ' ' in cleaned_block:
            space_index = cleaned_block.find(' ')
            if space_index > 0 and all(char == '#' for char in cleaned_block[:space_index]):
                block_type.append('heading')
        elif cleaned_block.startswith("```") and cleaned_block.endswith("```"):
            block_type.append('code')
        elif cleaned_block.startswith('> '):
            block_type.append('quote')
        elif cleaned_block.startswith(('*', '-')):
            block_type.append('unordered list')
        elif len(cleaned_block) > 2 and cleaned_block[0].isdigit() and cleaned_block[1:3] == '. ':
             block_type.append('ordered list')
        else: 
            block_type.append('paragraph')
    return block_type

