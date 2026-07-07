import React from "react";
import "../App.css";
import { Link } from "react-router-dom";

const Home = () => {
  return (
    <div className="landing-page">

      {/* HERO SECTION */}
      <section className="hero">

        <div className="hero-grid"></div>

        <div className="hero-left">

          <div className="status-badge">
            <div className="status-dot"></div>
            SYSTEM ONLINE
          </div>

          <h1>
           RegMind AI
          </h1>
         

          <p>
           RegMind AI is an AI-powered compliance intelligence platform that uses Hybrid RAG, comparative AI reasoning, and risk analysis to evaluate RBI regulations against internal compliance policies, detect regulatory conflicts, identify compliance gaps, and provide actionable insights before they become business risks.
          </p>

          <div className="hero-actions">
            <Link to="/ask-ai">
              <button className="primary-btn">Ask AI</button>
            </Link>
            <Link to="/detect-conflict">
              <button className="secondary-btn">Conflict Detection</button>
            </Link>
          </div>

        </div>

        {/* DASHBOARD CARD — RIGHT SIDE */}
        <div className="hero-right">
  <div className="dashboard-card">
    <div className="dashboard-card-header">
      <span>RegMind AI Analysis Preview</span>
      <span className="live-badge">
        Live
      </span>
    </div>
    {/* Query */}
    <div className="preview-section">
      <div className="preview-label">
        Query
      </div>
      <div className="preview-content">
        KYC Verification Process
      </div>
    </div>
    {/* Sources */}
    <div className="preview-section">
      <div className="preview-label">
        Sources Retrieved
      </div>
      <div className="preview-content">
        RBI Master Direction on KYC
        <br />
        Internal Customer Onboarding SOP
      </div>
    </div>
    {/* Findings */}
    <div className="preview-section">
      <div className="preview-label">
        AI Findings
      </div>
      <div className="preview-content">
        ✓ Video KYC permitted for low-risk customers
        <br />
        <br />
        ⚠ Internal SOP requires mandatory physical verification
      </div>
    </div>
    {/* Risk */}
    <div className="dashboard-row">
      <span>Conflict Status</span>
      <span className="val-medium">
        Medium Risk
      </span>
    </div>
    {/* References */}
    <div className="preview-section">
      <div className="preview-label">
        References
      </div>
      <div className="preview-content">
        RBI KYC Direction – Page 14
        <br />
        Internal SOP – Section 3.2
      </div>
    </div>
  </div>
</div>

      </section>

      {/* FEATURES */}
      <section className="features-section">
        <div className="section-header">
          <span>CORE FEATURES</span>
          <h2>Enterprise Compliance Infrastructure</h2>
        </div>
        <div className="features-grid">
          <div className="feature-card">
            <div className="feature-icon"></div>
            <h3>Hybrid RAG Retrieval</h3>
            <p>BM25 and dense vector retrieval work together for precise compliance search.</p>
          </div>
          <div className="feature-card">
            <div className="feature-icon"></div>
            <h3>Dual Collection Analysis</h3>
            <p>Compare RBI regulations with internal SOPs simultaneously using AI reasoning.</p>
          </div>
          <div className="feature-card">
            <div className="feature-icon"></div>
            <h3>LLM Reasoning Engine</h3>
            <p>Powered by Groq and Llama models for advanced comparative compliance intelligence.</p>
          </div>
          <div className="feature-card">
            <div className="feature-icon"></div>
            <h3>Risk Classification</h3>
            <p>Detects policy conflicts and categorizes them into structured risk levels.</p>
          </div>
        </div>
      </section>

      {/* WORKFLOW */}
      <section className="workflow-section">
        <div className="section-header center">
          <span>WORKFLOW</span>
          <h2>How RegMind AI Works</h2>
        </div>
        <div className="workflow-grid">
          <div className="workflow-card">
            <div className="step">01</div>
            <h3>Upload Documents</h3>
            <p>Upload RBI circulars and internal compliance SOPs.</p>
          </div>
          <div className="workflow-card">
            <div className="step">02</div>
            <h3>AI Retrieval</h3>
            <p>Hybrid retrieval fetches relevant clauses from both sources.</p>
          </div>
          <div className="workflow-card">
            <div className="step">03</div>
            <h3>Comparative Analysis</h3>
            <p>AI compares compliance rules and identifies contradictions.</p>
          </div>
          <div className="workflow-card">
            <div className="step">04</div>
            <h3>Risk Reporting</h3>
            <p>Structured conflict reports with risk level and references.</p>
          </div>
        </div>
      </section>

    </div>
  );
};

export default Home;