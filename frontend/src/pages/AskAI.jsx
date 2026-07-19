
import React, { useState } from "react";
import { askAI } from "../services/api";
import "../styles/Askai.css";

const AskAI = () => {

  const [query, setQuery] = useState("");
  const [loading, setLoading] = useState(false);
  const [result, setResult] = useState(null);
  const [error, setError] = useState("");
  const [sessionId] = useState(() => crypto.randomUUID());

  const handleAskAI = async () => {

    if (!query.trim()) {
      setError("Please enter a compliance query.");
      return;
    }

    try {

      setLoading(true);
      setError("");

      const response = await askAI(query,sessionId);

      setResult(response);

    } catch (err) {

      setError(
        err.message ||
        "Unable to process compliance analysis."
      );

    } finally {

      setLoading(false);

    }
  };

  const getRiskClass = (risk) => {

    const r = risk?.toLowerCase();

    if (r === "high") return "risk-high";
    if (r === "medium") return "risk-medium";

    return "risk-low";
  };

  return (

    <div className="ask-page">

      <section className="ask-header">

        <div className="header-badge">
          AI COMPLIANCE ENGINE
        </div>

        <h1>
          Ask RegMind AI
        </h1>

        <p>
          Analyze regulatory guidance, internal SOPs,
          and compliance frameworks using hybrid AI retrieval.
        </p>

      </section>

      <section className="search-section">

        <div className="search-card">

          <textarea
            className="query-input"
            placeholder="Ask a compliance-related query..."
            value={query}
            onChange={(e) => setQuery(e.target.value)}
          />

          <div className="search-footer">

            <span className="char-count">
              {query.length} characters
            </span>

            <button
              className="analyze-btn"
              onClick={handleAskAI}
              disabled={loading}
            >
              {loading
                ? "Analyzing..."
                : "Analyze Query"}
            </button>

          </div>

        </div>

        {error && (
          <div className="error-box">
            {error}
          </div>
        )}

      </section>

      {loading && (

        <div className="loading-box">

          <div className="loader"></div>

          <p>
            Scanning compliance documents...
          </p>

        </div>

      )}

     {result && !loading && (

  <section className="results-section">

    {/* MAIN RESULT */}

    <div className="result-card">

      <div className="result-top">

        <div className="verified-pill">
          VERIFIED AI ANALYSIS
        </div>

        <div
          className={`risk-pill ${getRiskClass(
            result?.risk_analysis?.risk_level
          )}`}
        >

          {result?.risk_analysis?.risk_level || "Low"} Risk

        </div>

      </div>

      {/* ANSWER */}

      <div className="answer-block">

        <h3>Executive Summary</h3>

        <p>
          {result?.answer}
        </p>

      </div>

      {/* SUMMARY */}

      {result?.summary && (

        <div className="summary-box">

          <h3>Compliance Summary</h3>

          <p>
            {result.summary}
          </p>

        </div> 

      )}

      {/* COMPLIANCE POINTS */}

      {result?.compliance_points?.length > 0 && (

        <div className="points-section">

          <h3>
            Key Compliance Points
          </h3>

          <div className="points-grid">

            {result.compliance_points.map(
              (point, index) => (

              <div
                className="point-card"
                key={index}
              >

                {point}

              </div>

            ))}

          </div>

        </div>

      )}

    </div>

    {/* META GRID */}

    <div className="meta-grid">

      {/* SOURCE EVIDENCE */}

<div className="meta-card">

  <h3>📄 Source Evidence</h3>

  <div className="sources-list">

    {result?.source_evidence?.length ? (

      result.source_evidence.map((item, index) => (

        <div
          className="source-item"
          key={index}
        >

          <div className="source-dot"></div>

          <div>

            <p className="source-name">

              {item.source === "rbi"
                ? "🏛 Regulatory Guidance"
                : "🏦 Internal Policy"}

            </p>

            <p
              className="source-page"
              style={{
                fontWeight: 600,
                color: "#0f172a",
                marginTop: "4px"
              }}
            >
              {item.document}
            </p>

            <p
              style={{
                fontSize: "13px",
                color: "#64748b",
                marginTop: "2px"
              }}
            >
              Page {item.page}
            </p>

          </div>

        </div>

      ))

    ) : (

      <p>No supporting evidence available.</p>

    )}

  </div>

</div>
      

     
      {/* AI COMPLIANCE RISK */}

  <div className="meta-card">

  <h3>AI Compliance Risk Assessment</h3>

  <div
    style={{
      display: "flex",
      flexDirection: "column",
      gap: "15px"
    }}
  >

    {/* Risk Badge */}

    <div
      className={`risk-pill ${getRiskClass(
        result?.risk_analysis?.risk_level
      )}`}
      style={{
        width: "fit-content"
      }}
    >
      {result?.risk_analysis?.risk_level} Risk
    </div>

    {/* SYSTEM EVALUATION */}

<div className="meta-card">

  <h3>📊 System Evaluation</h3>

  <div className="evaluation-grid">

    <div className="evaluation-row">
      <span>Response Time</span>
      <strong>{result?.response_time ?? "--"} sec</strong>
    </div>

    <div className="evaluation-row">
      <span>Retrieved Chunks</span>
      <strong>{result?.retrieved_chunks ?? "--"}</strong>
    </div>

    <div className="evaluation-row">
      <span>Source Documents</span>
      <strong>{result?.source_documents ?? "--"}</strong>
    </div>

    <div className="evaluation-row">
      <span>Retrieval Method</span>
      <strong>{result?.retrieval_method}</strong>
    </div>

    <div className="evaluation-row">
      <span>Vector Database</span>
      <strong>{result?.vector_database}</strong>
    </div>

    <div className="evaluation-row">
      <span>Offline Model Accuracy</span>
      <strong>{result?.model_accuracy}</strong>
    </div>

  </div>

</div>

    {/* Confidence */}

    <div>

      <strong>Confidence</strong>

      <p
        style={{
          marginTop: "6px",
          fontSize: "18px",
          fontWeight: "600"
        }}
      >
        {result?.risk_analysis?.confidence ?? 0}%
      </p>

    </div>

    {/* Risk Drivers */}

    <div>

      <strong>Top Risk Drivers</strong>

      <div
        style={{
          marginTop: "10px"
        }}
      >

        {result?.risk_analysis?.risk_factors?.length ? (

          result.risk_analysis.risk_factors.map(
            (factor, index) => (

              <div
                key={index}
                className="risk-row"
              >
                ✓ {factor}
              </div>

            )
          )

        ) : (

          <p>No significant risk indicators detected.</p>

        )}

      </div>

    </div>

  </div>

</div>
    </div> {/* End meta-grid */}

  </section>

)}

    </div>

  );
};

export default AskAI;
