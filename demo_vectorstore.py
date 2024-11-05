#!/usr/bin/env python
# coding: utf-8

import os
from config.sources import SourceConfig
from loaders.loader_factory import DocumentLoaderFactory
from vectorstore import EmbeddingsStore, VectorSearch

def test_pdf_search(search: VectorSearch):
    """Test PDF-specific search"""
    print("\nPDF Search Test:")
    print("=" * 50)
    query = "What are the MBA program requirements?"
    print(f"Query: '{query}'")
    print("Searching only in PDF documents...")
    
    filter_criteria = {"source_type": "PDF"}
    results = search.advanced_similarity_search(query, k=2, filter_criteria=filter_criteria)
    for i, doc in enumerate(results, 1):
        print(f"\nResult {i}:")
        print(f"Source Type: {doc.metadata.get('source_type', 'Unknown')}")
        print(f"Content: {doc.page_content[:200]}...")

def test_youtube_search(search: VectorSearch):
    """Test YouTube-specific search"""
    print("\nYouTube Search Test:")
    print("=" * 50)
    query = "What did the MBA student say about their experience at SFBU?"
    print(f"Query: '{query}'")
    print("Searching only in YouTube transcripts...")
    
    filter_criteria = {"source_type": "YouTube"}
    results = search.advanced_similarity_search(query, k=2, filter_criteria=filter_criteria)
    for i, doc in enumerate(results, 1):
        print(f"\nResult {i}:")
        print(f"Source Type: {doc.metadata.get('source_type', 'Unknown')}")
        print(f"Content: {doc.page_content[:200]}...")

def test_url_search(search: VectorSearch):
    """Test URL-specific search"""
    print("\nURL Search Test:")
    print("=" * 50)
    query = "What are the health insurance requirements for students?"
    print(f"Query: '{query}'")
    print("Searching only in web content...")
    
    filter_criteria = {"source_type": "URL"}
    results = search.advanced_similarity_search(query, k=2, filter_criteria=filter_criteria)
    for i, doc in enumerate(results, 1):
        print(f"\nResult {i}:")
        print(f"Source Type: {doc.metadata.get('source_type', 'Unknown')}")
        print(f"Content: {doc.page_content[:200]}...")

def test_combined_search(search: VectorSearch):
    """Test search across all sources"""
    print("\nCombined Search Test:")
    print("=" * 50)
    query = "Tell me about SFBU's MBA program requirements and student experiences"
    print(f"Query: '{query}'")
    print("Searching across all document types...")
    
    results = search.basic_similarity_search(query, k=3)
    for i, doc in enumerate(results, 1):
        print(f"\nResult {i}:")
        print(f"Source Type: {doc.metadata.get('source_type', 'Unknown')}")
        print(f"Content: {doc.page_content[:200]}...")

def test_edge_cases(search: VectorSearch):
    """Test edge cases similar to those in vectorstores_and_embeddings.py"""
    print("\nEdge Cases Test:")
    print("=" * 50)
    
    # Test duplicate content handling
    print("\n1. Duplicate Content Test:")
    query = "What are the MBA admission requirements and prerequisites?"
    print(f"Query: '{query}'")
    print("Testing for duplicate content in results...")
    
    results = search.basic_similarity_search(query, k=4)
    seen_content = set()
    duplicates_found = 0
    for doc in results:
        content_hash = hash(doc.page_content)
        if content_hash in seen_content:
            duplicates_found += 1
        seen_content.add(content_hash)
    print(f"Duplicates found: {duplicates_found}")
    
    # Test source-specific query with mixed results
    print("\n2. Source Specificity Test:")
    query = "What did students say about the MBA program in the YouTube video?"
    print(f"Query: '{query}'")
    print("Testing if results mix different source types...")
    
    results = search.basic_similarity_search(query, k=3)
    source_types = [doc.metadata.get('source_type', 'Unknown') for doc in results]
    print(f"Source types in results: {source_types}")
    
    # Test semantic similarity
    print("\n3. Semantic Similarity Test:")
    print("Testing semantic understanding with similar phrases...")
    store = EmbeddingsStore()
    pairs = [
        ("The university requires health insurance", "Students must have medical coverage"),
        ("The MBA program has prerequisites", "There are requirements for the MBA"),
        ("The campus is in Fremont", "The university is located somewhere else")
    ]
    for s1, s2 in pairs:
        similarity = store.compare_sentences(s1, s2)
        print(f"\nSentence 1: '{s1}'")
        print(f"Sentence 2: '{s2}'")
        print(f"Similarity Score: {similarity:.4f}")

def main():
    # Initialize source configuration
    config = SourceConfig.default_config()
    if not config.validate():
        print("Invalid source configuration")
        return
        
    # Initialize document loader
    loader = DocumentLoaderFactory()
    
    # Load all documents
    print("\nLoading documents...")
    documents = loader.load_documents(config.sources, verbose=True)
    if not documents:
        print("No documents loaded")
        return
    
    print(f"Loaded {len(documents)} documents")
    
    # Initialize embeddings store
    print("\nInitializing embeddings store...")
    store = EmbeddingsStore()
    
    # Create vector store
    print("Creating vector store...")
    vectordb = store.process_documents(documents)
    if not vectordb:
        print("Failed to create vector store")
        return
        
    # Initialize search
    search = VectorSearch(vectordb)
    
    # Run all tests
    test_pdf_search(search)
    test_youtube_search(search)
    test_url_search(search)
    test_combined_search(search)
    test_edge_cases(search)

if __name__ == "__main__":
    main() 