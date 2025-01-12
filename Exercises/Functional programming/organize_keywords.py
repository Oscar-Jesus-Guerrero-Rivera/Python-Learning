def find_keywords(document):
    keywords = [
        "functional",
        "immutable",
        "declarative",
        "higher-order",
        "lambda",
        "deterministic",
        "side-effects",
        "memoization",
        "referential transparency",
    ]
    return [keyword for keyword in keywords if keyword in document]


def map_keywords(document, document_map):
    document_map_copy = document_map.copy()
    
    if document in document_map_copy:
        return document_map_copy[document], document_map_copy
    
    found_keywords = find_keywords(document)
    document_map_copy[document] = found_keywords

    return found_keywords, document_map_copy


# Sample document and document map
document = "Functional programming focuses on immutable data and declarative logic."
document_map = {}

# Map keywords
keywords_found, updated_document_map = map_keywords(document, document_map)

print("Keywords Found:", keywords_found)
print("Updated Document Map:", updated_document_map)
