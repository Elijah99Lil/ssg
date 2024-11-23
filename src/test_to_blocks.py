import unittest
from to_blocks import markdown_to_blocks, block_to_block_type

class TestToBlocks(unittest.TestCase):

#Markdown to Block tests
    def test_to_blocks(self):
        test_md = """# Header

Paragraph with
multiple lines

* List item 1
* List item 2

"""

        result = markdown_to_blocks(test_md)
    
    def test_multiple_consecutive_lines(self):
        test_md = "Block 1\n\n\n\nBlock 2"
        result = markdown_to_blocks(test_md)

    def test_spaces_between_blocks(self):
        test_md = "Block 1\n  \n\t\nBlock 2"
        result = markdown_to_blocks(test_md)

    def test_empty_strings(self):
        test_md = ""
        result = markdown_to_blocks(test_md)

    def test_only_whitespace(self):
        test_md = "   \n\n  \t  \n"
        result = markdown_to_blocks(test_md)

    def test_no_separators(self):
        test_md = "Just one block"
        result = markdown_to_blocks(test_md)

    def test_trailing_or_leading_whitespace(self):
        test_md = "  Block 1  \n\n  Block 2  "
        result = markdown_to_blocks(test_md)

#Block type tests
    def test_heading(self):
        blocks = ["#### This is a heading."]
        result = block_to_block_type(blocks)
        assert result == ['heading']

    def test_empty_string(self):
        blocks = [""]
        result = block_to_block_type(blocks)
        assert result == ['paragraph']

    def test_single_character_blocks(self):
        blocks = ["#"]
        result = block_to_block_type(blocks)
        assert result == ['paragraph']

    def test_multi_character_alternatives(self):
        blocks = ["## Heading"]
        result = block_to_block_type(blocks)
        assert result == ['heading']

    def test_incorrect_list_format(self):
        blocks = ['''1no. list
        2 list gay 
        3 gay list''']
        result = block_to_block_type(blocks)
        assert result == ['paragraph']

    def test_mixed_format_lines(self):
        blocks = ["```if gay == True: "]
        result = block_to_block_type(blocks)
        assert result == ['paragraph']

    def test_spaces_before_tokens(self):
        blocks = [" # Heading..?"]
        result = block_to_block_type(blocks)
        assert result == ['paragraph']

    def test_non_incrementing_ordered_list(self):
        blocks = ["3. peepee, 5. poopoo"]
        result = block_to_block_type(blocks)
        assert result == ['ordered list']

    def test_multi_format(self):
        blocks = ["# > ``` shit fuck fard cum 4. AHHHHHH THE EIGHT LEGGED CREATURE ARISES!!"]
        result = block_to_block_type(blocks)
        assert result == ['heading']

    def test_fake_quotes(self):
        blocks = ["> >> Actually a quote"]
        result = block_to_block_type(blocks)
        assert result == ['quote']

    def test_wrong_quote_syntax(self):
        blocks = [">> > Actually not a quote"]
        result = block_to_block_type(blocks)
        assert result == ['paragraph']

