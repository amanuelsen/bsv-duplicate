import pytest
from src.util.detector import detect_duplicates

@pytest.mark.unit
class TestDuplicateDetector:
    def test_empty_input(self):
        """T1: Test empty input handling"""
        with pytest.raises(ValueError):
            detect_duplicates("")

    def test_single_entry(self):
        """T2: Test single valid entry"""
        data = """
        @article{key1,
            title={Test},
            doi={10.1/123}
        }
        """
        result = detect_duplicates(data)
        assert len(result) == 0

    def test_exact_duplicate(self):
        """T3: Test exact duplicate detection"""
        data = """
        @article{key1,
            doi={10.1/123}
        }
        @article{key1,
            doi={10.1/123}
        }
        """
        result = detect_duplicates(data)
        assert len(result) == 1

    def test_no_doi_duplicate(self):
        """T6: Test duplicate detection without DOI"""
        data = """
        @article{key1,
            title={Test}
        }
        @article{key1,
            title={Different}
        }
        """
        result = detect_duplicates(data)
        assert len(result) == 1

    def test_mixed_doi_scenario(self):
        """T7: Test mixed DOI scenario"""
        data = """
        @article{key1,
            doi={10.1/123}
        }
        @article{key1,
            doi={10.1/123}
        }
        @article{key1,
        }
        """
        result = detect_duplicates(data)
        assert len(result) == 2