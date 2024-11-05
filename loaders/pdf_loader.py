#!/usr/bin/env python
# coding: utf-8

import os
from typing import List, Optional
from dotenv import load_dotenv, find_dotenv
from langchain_community.document_loaders import PyPDFLoader
from langchain.schema import Document

_ = load_dotenv(find_dotenv())

def load_pdf(pdf_path: str) -> List[Document]:
    """
    Load and process a PDF document
    Args:
        pdf_path (str): Path to the PDF file
    Returns:
        List[Document]: List of Document objects containing page content
    """
    try:
        if not os.path.exists(pdf_path):
            raise FileNotFoundError(f"PDF file not found at path: {pdf_path}")
            
        loader = PyPDFLoader(pdf_path)
        return loader.load()
    except Exception as e:
        print(f"Error loading PDF: {e}")
        return []