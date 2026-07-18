from langchain_text_splitters import RecursiveCharacterTextSplitter

from backend.config import CHUNK_SIZE, CHUNK_OVERLAP


# ======================================================
# DETECT TOPIC
# ======================================================

def detect_topic(text):

    text = text.lower()

    if "beneficial owner" in text or "beneficial ownership" in text:
        return "BENEFICIAL_OWNERSHIP"

    elif "know your customer" in text or "kyc" in text:
        return "KYC"

    elif "customer due diligence" in text:
        return "CDD"

    elif "aml" in text or "anti money laundering" in text:
        return "AML"

    elif "wire transfer" in text:
        return "WIRE_TRANSFER"

    elif "politically exposed person" in text or "pep" in text:
        return "PEP"

    elif "risk" in text:
        return "RISK"

    return "GENERAL"


# ======================================================
# DETECT ENTITY TYPE
# ======================================================

def detect_entity(text):

    text = text.lower()

    if "customer is a company" in text:
        return "COMPANY"

    elif "partnership firm" in text:
        return "PARTNERSHIP"

    elif "trust" in text:
        return "TRUST"

    elif "unincorporated association" in text:
        return "UNINCORPORATED_ASSOCIATION"

    elif "body of individuals" in text:
        return "BODY_OF_INDIVIDUALS"

    elif "natural person" in text:
        return "NATURAL_PERSON"

    return "GENERAL"


# ======================================================
# DETECT CHUNK TYPE
# ======================================================

def detect_chunk_type(text):

    text = text.lower()

    if any(word in text for word in [
        "shall",
        "must",
        "required",
        "mandatory"
    ]):
        return "COMPLIANCE_CLAUSE"

    elif "penalty" in text or "fine" in text:
        return "PENALTY"

    elif any(word in text for word in [
        "procedure",
        "process",
        "steps"
    ]):
        return "PROCEDURE"

    elif "definition" in text or "means" in text:
        return "DEFINITION"

    return "GENERAL"


# ======================================================
# CHUNK DOCUMENTS
# ======================================================

def chunk_documents(documents):

    splitter = RecursiveCharacterTextSplitter(

        chunk_size=CHUNK_SIZE,

        chunk_overlap=CHUNK_OVERLAP,

        separators=[
            "\n\n",
            "\n",
            "\n(a)",
            "\n(b)",
            "\n(c)",
            "\n(d)",
            "\n(e)",
            "\n(f)",
            "\n(i)",
            "\n(ii)",
            "\n(iii)",
            "\n(iv)",
            "\n(v)",
            "\n1.",
            "\n2.",
            "\n3.",
            "\n4.",
            ". ",
            ";",
            ",",
            " ",
            ""
        ]
    )

    final_chunks = []

    for doc in documents:

        chunks = splitter.split_text(doc["text"])

        for i, chunk in enumerate(chunks):

            chunk = chunk.strip()

            if len(chunk) < 40:
                continue

            chunk_data = {

                "document_name": doc["document_name"],

                "page_number": doc["page_number"],

                "chunk_id": f"{doc['page_number']}_{i}",

                "chunk_text": chunk,

                "topic": detect_topic(chunk),

                "entity": detect_entity(chunk),

                "chunk_type": detect_chunk_type(chunk),

                "chunk_length": len(chunk)
            }

            final_chunks.append(chunk_data)

    return final_chunks