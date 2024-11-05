#!/usr/bin/env python
# coding: utf-8

from typing import List, Dict
from langchain.schema import Document
from .pdf_loader import load_pdf
from .url_loader import load_url
from .youtube_loader import load_youtube
from utils.content_formatter import ContentFormatter

class DocumentLoaderFactory:
    """Factory for creating document loaders"""
    
    def __init__(self):
        self.formatter = ContentFormatter()
    
    def load_documents(self, sources: List[Dict[str, str]], verbose: bool = True) -> List[Document]:
        """
        Load documents from multiple sources
        Args:
            sources: List of source configurations
            verbose: Whether to print loading details
        Returns:
            List of Document objects
        """
        documents = []
        
        if verbose:
            print("\nLoading documents from sources:")
            print("=" * 50)
        
        for source in sources:
            source_type = list(source.keys())[0]
            source_path = source[source_type]
            
            try:
                if verbose:
                    print(f"\nLoading {source_type} from: {source_path}")
                
                if source_type == "PDF":
                    docs = load_pdf(source_path)
                elif source_type == "URL":
                    docs = load_url(source_file=source_path)
                elif source_type == "YouTube":
                    docs = load_youtube(source_file=source_path)
                else:
                    print(f"Unsupported source type: {source_type}")
                    continue
                    
                if docs:
                    # Format documents and add metadata
                    docs = self.formatter.format_documents(docs)
                    for doc in docs:
                        doc.metadata["source_type"] = source_type
                        doc.metadata["source"] = source_path
                    
                    documents.extend(docs)
                    
                    if verbose:
                        print(f"\nSuccessfully loaded {len(docs)} documents")
                        if docs:
                            # Print sample document
                            self.formatter.print_document_info(docs[0])
                    
            except Exception as e:
                print(f"Error loading {source_type} from {source_path}: {e}")
                continue
        
        if verbose:
            self.formatter.print_documents_summary(documents)
            
        return documents