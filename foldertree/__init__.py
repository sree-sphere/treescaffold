"""
FolderTree Generator - Create folder structures from various input formats
"""

from .core import TreeParser, TreeGenerator, TreeNode
from .cli import main

__version__ = "1.3.2"
__all__ = ["TreeParser", "TreeGenerator", "TreeNode", "main"]