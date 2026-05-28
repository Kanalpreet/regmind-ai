from langchain_text_splitters import RecursiveCharacterTextSplitter

from backend.config import CHUNK_SIZE, CHUNK_OVERLAP


def detect_topic(text):

    text = text.lower()

    if "kyc" in text:
        return "KYC"

    elif "customer due diligence" in text:
        return "CDD"

    elif "aml" in text:
        return "AML"

    elif "wire transfer" in text:
        return "WIRE_TRANSFER"

    return "GENERAL"


def detect_chunk_type(text):

    text = text.lower()

    if "shall" in text or "must" in text:
        return "COMPLIANCE_CLAUSE"

    elif "penalty" in text:
        return "PENALTY"

    elif "procedure" in text:
        return "PROCEDURE"

    return "GENERAL"


def chunk_documents(documents):

    splitter = RecursiveCharacterTextSplitter(

    chunk_size=CHUNK_SIZE,

    chunk_overlap=CHUNK_OVERLAP,

    separators=[
        "\n\n",
        "\n",
        ". ",
        " ",
        ""
    ]
)

    final_chunks = []

    for doc in documents:

        chunks = splitter.split_text(doc["text"])

        for chunk in chunks:

            chunk_data = {

                "document_name": doc["document_name"],

                "page_number": doc["page_number"],

                "chunk_text": chunk,

                # NEW METADATA
                "topic": detect_topic(chunk),

                "chunk_type": detect_chunk_type(chunk)
            }

            final_chunks.append(chunk_data)

    return final_chunks