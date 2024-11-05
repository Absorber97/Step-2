#!/usr/bin/env python
# coding: utf-8

import os
from typing import List, Optional
from dotenv import load_dotenv, find_dotenv
from langchain_community.document_loaders import WebBaseLoader
from langchain.schema import Document

_ = load_dotenv(find_dotenv())

def load_url(url: Optional[str] = None, source_file: Optional[str] = None) -> List[Document]:
    """
    Load and process content from a URL
    Args:
        url (str, optional): Direct URL to load
        source_file (str, optional): Path to file containing URL
    Returns:
        List[Document]: List of Document objects containing web content
    """
    try:
        if source_file:
            if not os.path.exists(source_file):
                raise FileNotFoundError(f"Source file not found: {source_file}")
            with open(source_file, 'r') as f:
                url = f.read().strip()
                
        if not url:
            raise ValueError("No URL provided")
            
        loader = WebBaseLoader(url)
        return loader.load()
    except Exception as e:
        print(f"Error loading URL: {e}")
        return []