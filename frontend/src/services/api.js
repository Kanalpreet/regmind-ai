const BASE_URL = "http://127.0.0.1:8000";

export const askAI = async (sessionId, query) => {

    const response = await fetch(`${BASE_URL}/ask-ai`, {

        method: "POST",

        headers: {
            "Content-Type": "application/json",
        },

        body: JSON.stringify({
            session_id: sessionId,
            query: query,
        }),
    });

    if (!response.ok) {

        throw new Error("Failed to fetch AI response");
    }

    return await response.json();
};

export const detectConflict = async (query) => {

    const response = await fetch(`${BASE_URL}/detect-conflict`, {

        method: "POST",

        headers: {
            "Content-Type": "application/json",
        },

        body: JSON.stringify({
            query,
        }),
    });

    if (!response.ok) {

        throw new Error("Failed to detect conflict");
    }

    return await response.json();
};