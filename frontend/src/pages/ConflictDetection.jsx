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

      setError(
        "Please describe the policy or scenario."
      );

      return;
    }

    try {

      setLoading(true);
      setError("");

      const response =
        await detectConflict(query);

      setResult(response);

    } catch (err) {

      setError(
        err.message ||
        "Failed to analyze conflicts."
      );

    } finally {

      setLoading(false);
    }
  };

  const getSeverityClass = (severity) => {

    const s = severity?.toLowerCase();

    if (s === "high" || s === "critical")
      return "severity-high";

    if (s === "medium")
      return "severity-medium";

    return "severity-low";
  };

  return (

    <div className="conflict-page">

      {/* HEADER */}

      <section className="conflict-header">

        <div className="header-pill">
          AI POLICY COMPARISON
        </div>

        <h1>
          Policy Conflict Detection
        </h1>

        <p>
          Cross-reference internal policies against
          RBI regulations using comparative AI reasoning.
        </p>

      </section>

      {/* INPUT */}

      <section className="conflict-search">

        <div className="search-card">

          <label>
            Describe Policy or Scenario
          </label>

          <textarea

            className="conflict-input"

            placeholder="Describe the policy or compliance scenario..."

            value={query}

            onChange={(e) =>
              setQuery(e.target.value)
            }

          />

          <div className="search-footer">

            <span>
              {query.length} characters
            </span>

            <button

              className="analyze-btn"

              onClick={handleConflictCheck}

              disabled={loading}

                     >

            {loading
              ? "Analyzing..."
              : "Check Conflicts"}

          </button>

          </div>

        </div>

        {error && (

          <div className="error-box">
            {error}
          </div>

        )}

      </section>

      {/* LOADING */}

      {loading && (

        <div className="loading-box">

          <div className="loader"></div>

          <p>
            Comparing internal policies with
            RBI compliance frameworks...
          </p>

        </div>

      )}

      {/* RESULTS */}

      {result && !loading && (

        <section className="results-section">

          {/* SUMMARY */}

          <div className={`summary-banner ${result.conflict_found
            ? "has-conflict"
            : "no-conflict"
          }`}>

            <div className="summary-icon">

              {result.conflict_found
                ? "!"
                : "✓"}

            </div>

            <div>

              <h3>

                {result.conflict_found
                  ? "Potential Conflict Detected"
                  : "No Major Conflicts Found"}

              </h3>

              <p>
                {result.summary ||
                  "Initial compliance scan completed."}
              </p>

            </div>

          </div>

          {/* MAIN GRID */}

          <div className="analysis-grid">

            {/* COMPARISON */}

            <div className="glass-card">

              <div className="card-top">

                <h3>
                  Detailed Comparison
                </h3>

                {result.severity && (

                  <span
                    className={`severity-badge ${getSeverityClass(
                      result.severity
                    )}`}
                  >

                    {result.severity} Risk

                  </span>

                )}

              </div>

              <div className="comparison-layout">

                {/* POLICY */}

                <div>

                  <div className="section-label">
                    Your Policy
                  </div>

                  <div className="content-box">

                    {result.policy_statement || query}

                  </div>

                </div>

                {/* DIVIDER */}

                <div className="vs-divider">
                  VS
                </div>

                {/* RBI */}

                <div>

                  <div className="section-label">
                    RBI Regulation
                  </div>

                  <div className="content-box regulation">

                    {result.regulation_statement ||
                      "Relevant RBI regulation will appear here."}

                  </div>

                </div>

              </div>

            </div>

            {/* RECOMMENDATIONS */}

            <div className="glass-card">

              <h3>
                Remediation Plan
              </h3>

              <div className="recommendation-list">

                {result.recommendations?.map(
                  (rec, index) => (

                  <div
                    className="recommendation-item"
                    key={index}
                  >

                    <div className="rec-number">

                      {index + 1}

                    </div>

                    <p>{rec}</p>

                  </div>

                ))}

              </div>

            </div>

          </div>

        </section>

      )}

    </div>

  );
};

export default ConflictDetection;