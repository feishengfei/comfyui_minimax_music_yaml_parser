"""Top-level package for minimax_music_yaml_parser."""

__all__ = [
    "NODE_CLASS_MAPPINGS",
    "NODE_DISPLAY_NAME_MAPPINGS",
    "WEB_DIRECTORY",
]

__author__ = """comfyui-minimax-music-yaml-parser"""
__email__ = "feishengfei@126.com"
__version__ = "0.0.1"

from .src.minimax_music_yaml_parser.nodes import NODE_CLASS_MAPPINGS
from .src.minimax_music_yaml_parser.nodes import NODE_DISPLAY_NAME_MAPPINGS

WEB_DIRECTORY = "./web"
