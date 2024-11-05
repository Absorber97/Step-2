#!/usr/bin/env python
# coding: utf-8

from typing import List, Dict, Union, Any
from dataclasses import dataclass, field

@dataclass
class SourceConfig:
    """Configuration for document sources"""
    sources: List[Dict[str, str]] = field(default_factory=list)

    @classmethod
    def default_config(cls) -> 'SourceConfig':
        """Create default source configuration"""
        return cls(sources=[
            {"PDF": "sources/sfbu-2024-2025-university-catalog-8-20-2024.pdf"},
            {"PDF": "sources/sfbu-2024-2025-university-catalog-8-20-2024.pdf"},  # Duplicate
            {"URL": "sources/sfbu-health-insurance-url.txt"},
            {"YouTube": "sources/youtube-mba-spotlight.txt"}
        ])

    def validate(self) -> bool:
        """Validate source configuration"""
        valid_types = {"PDF", "URL", "YouTube"}
        try:
            if not self.sources:
                return False
            for source in self.sources:
                if len(source) != 1:
                    return False
                source_type = list(source.keys())[0]
                if source_type not in valid_types:
                    return False
            return True
        except Exception:
            return False 