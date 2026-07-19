import React, { useState } from "react";
import { detectConflict } from "../services/api";
import "../styles/conflict.css";

const ConflictDetection = () => {
  const [query, setQuery] = useState("");
  const [loading, setLoading] = useState(false);
  const [result, setResult] = useState(null);
  const [error, setError] = useState("");

  const handleConflictCheck = async () => {
    if (!query.trim()) {
      setError("Please describe the policy or scenario.");
      return;
    }

    try {
      setLoading(true);
      setError("");

      const response = await detectConflict(query);

      console.log("Conflict Response:", response);

      setResult(response);
    } catch (err) {
      setError(err.message || "Failed to analyze conflicts.");
    } finally {
      setLoading(false);
    }
  };

  const getSeverityClass = (severity) => {
    const s = severity?.toLowerCase();

    if (s === "high" || s === "critical") return "severity-high";
    if (s === "medium") return "severity-medium";

    return "severity-low";
  };

  return (
    <div className="conflict-page">
      {/* HEADER */}

      <section className="conflict-header">
        <div className="header-pill">AI POLICY COMPARISON</div>

        <h1>Policy Conflict Detection</h1>

        <p>
          Cross-reference internal policies against regulatory guidance using
          comparative AI reasoning.
        </p>
      </section>

      {/* SEARCH */}

      <section className="conflict-search">
        <div className="search-card">
          <label>Describe Policy or Scenario</label>

          <textarea
            className="conflict-input"
            placeholder="Describe the policy or compliance scenario..."
            value={query}
            onChange={(e) => setQuery(e.target.value)}
          />

          <div className="search-footer">
            <span>{query.length} characters</span>

            <button
              className="analyze-btn"
              onClick={handleConflictCheck}
              disabled={loading}
            >
              {loading ? "Analyzing..." : "Check Conflicts"}
            </button>
          </div>
        </div>

        {error && <div className="error-box">{error}</div>}
      </section>

      {/* LOADING */}

      {loading && (
        <div className="loading-box">
          <div className="loader"></div>

          <p>
            Comparing internal policies with regulatory frameworks...
          </p>
        </div>
      )}

      {/* RESULTS */}

      {result && !loading && (
        <section className="results-section">
          {/* SUMMARY */}

          <div
            className={`summary-banner ${
              result.conflict_detected
                ? "has-conflict"
                : "no-conflict"
            }`}
          >
            <div className="summary-icon">
              {result.conflict_detected ? "!" : "✓"}
            </div>

            <div>
              <h3>
                {result.conflict_detected
                  ? "Potential Conflict Detected"
                  : "No Major Conflicts Found"}
              </h3>

              <p>{result.reason}</p>
            </div>
          </div>

          {/* MAIN GRID */}

          <div className="analysis-grid">
            {/* COMPARISON */}

            <div className="glass-card">
              <div className="card-top">
                <h3>Detailed Comparison</h3>

                {result.risk_level && (
                  <span
                    className={`severity-badge ${getSeverityClass(
                      result.risk_level
                    )}`}
                  >
                    {result.risk_level} Risk
                  </span>
                )}
              </div>

              <div className="comparison-layout">
                {/* INTERNAL POLICY */}

                <div>
                  <div className="section-label">
                    Internal Policy
                  </div>

                  <div className="content-box">
                    {result.internal_policy_position}
                  </div>
                </div>

                {/* DIVIDER */}

                <div className="vs-divider">VS</div>

                {/* Reference framework */}

                <div>
                  <div className="section-label">
                    Reference Framework
                  </div>

                  <div className="content-box regulation">
                    {result.rbi_position}
                  </div>
                </div>
              </div>
            </div>

            {/* RECOMMENDATION */}

            <div className="glass-card">
              <h3>Recommendation</h3>

              <div className="recommendation-list">
                <div className="recommendation-item">
                  <div className="rec-number">1</div>

                  <p>{result.recommendation}</p>
                </div>
              </div>
            </div>
          </div>

          {/* RAW JSON (Helpful for debugging) */}

          <div className="glass-card" style={{ marginTop: "25px" }}>
            <h3>AI Response</h3>

            <pre
              style={{
                whiteSpace: "pre-wrap",
                color: "#d9d9d9",
                fontSize: "14px",
              }}
            >
              {JSON.stringify(result, null, 2)}
            </pre>
          </div>
        </section>
      )}
    </div>
  );
};

export default ConflictDetection;
