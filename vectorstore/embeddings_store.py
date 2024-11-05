#!/usr/bin/env python
# coding: utf-8

import os
import numpy as np
from typing import Optional, List
from dotenv import load_dotenv, find_dotenv
from langchain_openai import OpenAIEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain.schema import Document

# Load environment variables
_ = load_dotenv(find_dotenv())

class EmbeddingsStore:
    def __init__(self, persist_directory: str = 'docs/chroma/'):
        """
        Initialize the embeddings store
        Args:
            persist_directory (str): Directory to persist the vector store
        """
        try:
            import chromadb
            self.persist_directory = persist_directory
            self.embedding = OpenAIEmbeddings()
            self.text_splitter = RecursiveCharacterTextSplitter(
                chunk_size=1500,
                chunk_overlap=150
            )
        except ImportError:
            raise ImportError(
                "Could not import chromadb. Please install it with `pip install chromadb`"
            )
        
    def process_documents(self, documents: List[Document]) -> Optional[Chroma]:
        """
        Process documents and create embeddings
        Args:
            documents (list): List of Document objects
        Returns:
            Chroma: Vector store with embedded documents
        """
        try:
            # Create persist directory if it doesn't exist
            os.makedirs(self.persist_directory, exist_ok=True)
            
            # Split documents into chunks
            splits = self.text_splitter.split_documents(documents)
            
            # Create vector store
            vectordb = Chroma.from_documents(
                documents=splits,
                embedding=self.embedding,
                persist_directory=self.persist_directory
            )
            
            return vectordb
        except Exception as e:
            print(f"Error processing documents: {e}")
            return None
            
    def compare_sentences(self, sentence1: str, sentence2: str) -> Optional[float]:
        """
        Compare similarity between two sentences
        Args:
            sentence1 (str): First sentence
            sentence2 (str): Second sentence
        Returns:
            float: Similarity score between 0 and 1
        """
        try:
            embedding1 = self.embedding.embed_query(sentence1)
            embedding2 = self.embedding.embed_query(sentence2)
            
            similarity = np.dot(embedding1, embedding2)
            return similarity
        except Exception as e:
            print(f"Error comparing sentences: {e}")
            return None