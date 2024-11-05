#!/usr/bin/env python
# coding: utf-8

from typing import List, Dict, Any, Optional
from langchain.schema import Document

class VectorSearch:
    def __init__(self, vectordb):
        """
        Initialize vector search
        Args:
            vectordb: Chroma vector store instance
        """
        self.vectordb = vectordb
        
    def basic_similarity_search(self, query: str, k: int = 3) -> List[Document]:
        """
        Perform basic similarity search
        Args:
            query (str): Search query
            k (int): Number of results to return
        Returns:
            list: List of relevant Document objects
        """
        try:
            return self.vectordb.similarity_search(query, k=k)
        except Exception as e:
            print(f"Error in similarity search: {e}")
            return []
            
    def advanced_similarity_search(
        self, 
        query: str, 
        k: int = 3, 
        filter_criteria: Optional[Dict[str, Any]] = None
    ) -> List[Document]:
        """
        Perform advanced similarity search with filtering
        Args:
            query (str): Search query
            k (int): Number of results to return
            filter_criteria (dict): Metadata filters for search
        Returns:
            list: List of relevant Document objects
        """
        try:
            if filter_criteria:
                return self.vectordb.similarity_search(
                    query,
                    k=k,
                    filter=filter_criteria
                )
            return self.basic_similarity_search(query, k)
        except Exception as e:
            print(f"Error in advanced similarity search: {e}")
            return []