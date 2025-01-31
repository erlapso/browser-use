import pytest

from browser_use.dom.views import DOMElementNode, DOMTextNode

class TestDOMElementNode:
    def test_get_file_upload_element(self):
        """
        Test the get_file_upload_element method of DOMElementNode.

        This test creates a mock DOM structure with a file input element
        and verifies that the method correctly identifies and returns it.
        """
        # Create a mock DOM structure
        root = DOMElementNode(
            is_visible=True,
            parent=None,
            tag_name="div",
            xpath="/html/body/div",
            attributes={},
            children=[],
            is_interactive=False
        )

        form = DOMElementNode(
            is_visible=True,
            parent=root,
            tag_name="form",
            xpath="/html/body/div/form",
            attributes={},
            children=[],
            is_interactive=False
        )
        root.children.append(form)

        file_input = DOMElementNode(
            is_visible=True,
            parent=form,
            tag_name="input",
            xpath="/html/body/div/form/input",
            attributes={"type": "file"},
            children=[],
            is_interactive=True
        )
        form.children.append(file_input)

        text_input = DOMElementNode(
            is_visible=True,
            parent=form,
            tag_name="input",
            xpath="/html/body/div/form/input[2]",
            attributes={"type": "text"},
            children=[],
            is_interactive=True
        )
        form.children.append(text_input)

        # Test finding the file input from the root
        assert root.get_file_upload_element() == file_input

        # Test finding the file input from a sibling
        assert text_input.get_file_upload_element() == file_input

        # Test when there's no file input
        no_file_input_root = DOMElementNode(
            is_visible=True,
            parent=None,
            tag_name="div",
            xpath="/html/body/div",
            attributes={},
            children=[text_input],
            is_interactive=False
        )
        assert no_file_input_root.get_file_upload_element() is None