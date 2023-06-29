from typing import Optional
from browse.domain.metadata import DocMetadata

from browse.services.database import get_latexml_status_for_document

import logging

def get_latexml_url (article: DocMetadata) -> Optional[str]:
    LATEXML_URI_BASE = "https://services.dev.arxiv.org/html"
    status = get_latexml_status_for_document(article.arxiv_id, article.version)
    path = f'{article.arxiv_id}v{article.version}/{article.arxiv_id}v{article.version}.html'
    return f'{LATEXML_URI_BASE}/{path}' if status == 1 else None