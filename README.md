# Document Vector Search

This project implements semantic search across multiple document types using vector embeddings and ChromaDB. It supports searching through PDFs, YouTube transcripts, and web content with advanced filtering capabilities.

Step 1: https://github.com/Absorber97/RAG-Document-Loader
Step 2 (This Project): https://github.com/Absorber97/Vectorstores-Embedding

## Overview

The project demonstrates advanced document processing and semantic search capabilities by:
1. Loading content from multiple sources (PDF, YouTube, URLs)
2. Converting text into vector embeddings using OpenAI
3. Storing embeddings in a vector database (ChromaDB)
4. Performing semantic similarity searches
5. Handling edge cases and duplicates

## Features

### Multi-Source Support
- **PDF Processing**: Extract and process text from PDF documents
- **YouTube Integration**: Transcribe video content using OpenAI Whisper
- **Web Scraping**: Extract content from web pages
- **Duplicate Handling**: Detect and manage duplicate content

### Advanced Search Capabilities
- **Semantic Search**: Find content based on meaning, not just keywords
- **Source Filtering**: Search within specific document types
- **Similarity Scoring**: Compare semantic similarity between texts
- **Cross-Source Search**: Search across all document types simultaneously

### Modular Architecture
- **Factory Pattern**: Extensible document loader system
- **Content Formatting**: Standardized content processing
- **Error Handling**: Robust error management and recovery
- **Persistent Storage**: Durable vector store for embeddings

## Installation

1. Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Create a .env file with your OpenAI API key:
```
OPENAI_API_KEY=your_api_key_here
```

4. Install ffmpeg for YouTube audio processing:
- macOS: `brew install ffmpeg`
- Ubuntu: `sudo apt-get install ffmpeg`
- Windows: Download from https://ffmpeg.org/download.html

## Project Structure

```
project/
├── config/
│   └── sources.py         # Source configuration
├── loaders/
│   ├── loader_factory.py  # Document loader factory
│   ├── pdf_loader.py      # PDF processing
│   ├── youtube_loader.py  # YouTube transcription
│   └── url_loader.py      # Web content loading
├── utils/
│   └── content_formatter.py  # Content formatting utilities
├── vectorstore/
│   ├── embeddings_store.py  # Document embeddings
│   └── vector_search.py     # Search implementation
├── sources/               # Source files
├── docs/               
│   └── chroma/           # Vector store data
└── requirements.txt
```

## Usage

### Basic Usage
```bash
python demo_vectorstore.py
```

### Source Configuration
Configure document sources in `config/sources.py`:
```python
sources = [
    {"PDF": "path/to/document.pdf"},
    {"YouTube": "path/to/video_url.txt"},
    {"URL": "path/to/webpage_url.txt"}
]
```

### Search Examples
The demo script includes various search tests:
- **PDF Search**: Search within PDF documents
- **YouTube Search**: Search through video transcripts
- **URL Search**: Search web page content
- **Combined Search**: Search across all sources
- **Edge Cases**: Test duplicate handling and source mixing

## Testing

The project includes comprehensive tests for:

1. Source-Specific Searches
   - PDF content retrieval
   - YouTube transcript search
   - Web content search

2. Cross-Source Functionality
   - Combined source searching
   - Source type filtering
   - Result relevance checking

3. Edge Case Handling
   - Duplicate content detection
   - Mixed source results
   - Content formatting issues

4. Semantic Analysis
   - Similarity comparisons
   - Meaning-based matching
   - Context understanding

## Dependencies

### Core Functionality
- **langchain & langchain-community**: Document processing framework
- **langchain-openai**: OpenAI integration
- **openai**: Embeddings and transcription
- **chromadb**: Vector storage and retrieval

### Media Processing
- **pypdf**: PDF document handling
- **yt-dlp**: YouTube video downloading
- **pydub**: Audio file processing

### Utilities
- **python-dotenv**: Environment management
- **numpy**: Numerical operations
- **tiktoken**: Token counting
- **sentence-transformers**: Text embeddings

## Implementation Notes

### Document Processing
- Automatic content cleaning and formatting
- Metadata enrichment for each document
- Chunk size optimization for better search

### Vector Search
- Semantic similarity calculation
- Source-specific filtering
- Duplicate detection
- Result ranking

### Error Handling
- Graceful failure recovery
- Detailed error reporting
- Automatic cleanup of temporary files

### Performance Considerations
- Optimized chunk sizes
- Efficient vector storage
- Cached embeddings
- Parallel processing where possible

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.
