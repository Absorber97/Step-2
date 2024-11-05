#!/usr/bin/env python
# coding: utf-8

from typing import List, Dict, Any
from langchain.schema import Document

class ContentFormatter:
    """Format and validate document content"""
    
    @staticmethod
    def format_content(text: str) -> str:
        """
        Clean and format text content
        Args:
            text (str): Raw text content
        Returns:
            str: Formatted text content
        """
        # Remove excessive whitespace
        lines = text.split('\n')
        lines = [line.strip() for line in lines]
        lines = [line for line in lines if line]
        return '\n'.join(lines)
    
    @staticmethod
    def format_document(doc: Document) -> Document:
        """
        Format a single document
        Args:
            doc (Document): Document to format
        Returns:
            Document: Formatted document
        """
        formatted_content = ContentFormatter.format_content(doc.page_content)
        return Document(
            page_content=formatted_content,
            metadata=doc.metadata
        )
    
    @staticmethod
    def format_documents(docs: List[Document]) -> List[Document]:
        """
        Format a list of documents
        Args:
            docs (List[Document]): Documents to format
        Returns:
            List[Document]: Formatted documents
        """
        return [ContentFormatter.format_document(doc) for doc in docs]
    
    @staticmethod
    def print_document_info(doc: Document, max_content_length: int = 200) -> None:
        """
        Print formatted document information
        Args:
            doc (Document): Document to print
            max_content_length (int): Maximum content length to display
        """
        print("\nDocument Information:")
        print("=" * 50)
        print(f"Source Type: {doc.metadata.get('source_type', 'Unknown')}")
        print(f"Source: {doc.metadata.get('source', 'Unknown')}")
        print("\nContent Preview:")
        print("-" * 50)
        content = doc.page_content[:max_content_length]
        if len(doc.page_content) > max_content_length:
            content += "..."
        print(content)
        print("=" * 50)
    
    @staticmethod
    def print_documents_summary(docs: List[Document]) -> None:
        """
        Print summary of loaded documents
        Args:
            docs (List[Document]): Documents to summarize
        """
        source_counts: Dict[str, int] = {}
        for doc in docs:
            source_type = doc.metadata.get('source_type', 'Unknown')
            source_counts[source_type] = source_counts.get(source_type, 0) + 1
        
        print("\nDocument Loading Summary:")
        print("=" * 50)
        for source_type, count in source_counts.items():
            print(f"{source_type}: {count} documents")
        print("-" * 50)
        print(f"Total: {len(docs)} documents") 