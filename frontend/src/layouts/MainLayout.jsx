import React, { useState } from 'react';
import { useLocation } from 'react-router-dom';
import Sidebar from '../components/Sidebar';

const pageDetails = {
  '/ask-ai': {
    eyebrow: 'Intelligence workspace',
    title: 'Regulatory inquiry',
    signal: 'Evidence engine ready',
  },
  '/conflict-detection': {
    eyebrow: 'Comparative review',
    title: 'Policy conflict scan',
    signal: 'Comparison engine ready',
  },
};

const RegMindMark = () => (
  <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2.1" aria-hidden="true">
    <path d="m12 2.8 7.7 4.1L12 11 4.3 6.9 12 2.8Z" />
    <path d="m4.3 11.5 7.7 4.1 7.7-4.1M4.3 16.1l7.7 4.1 7.7-4.1" />
  </svg>
);

const MainLayout = ({ children }) => {
  const [isSidebarOpen, setIsSidebarOpen] = useState(false);
  const location = useLocation();
  const page = pageDetails[location.pathname] ?? pageDetails['/ask-ai'];

  const toggleSidebar = () => setIsSidebarOpen((isOpen) => !isOpen);
  const closeSidebar = () => setIsSidebarOpen(false);

  return (
    <div className="app-container intelligence-shell">
      <header className="mobile-header">
        <div className="mobile-brand">
          <span className="mobile-mark"><RegMindMark /></span>
          <div>
            <span>RegMind</span>
            <small>INTELLIGENCE OS</small>
          </div>
        </div>
        <button className="mobile-toggle" onClick={toggleSidebar} aria-label={isSidebarOpen ? 'Close navigation' : 'Open navigation'} aria-expanded={isSidebarOpen}>
          <span /><span /><span />
        </button>
      </header>

      <div className={`sidebar-wrapper ${isSidebarOpen ? 'mobile-open' : ''}`}>
        <button className="sidebar-overlay" onClick={closeSidebar} aria-label="Close navigation" />
        <Sidebar />
      </div>

      <main className="main-content workspace-content">
        <div className="workspace-topbar">
          <div className="workspace-context">
            <span className="context-kicker">{page.eyebrow}</span>
            <div className="context-title-row">
              <span className="context-node" aria-hidden="true" />
              <span>{page.title}</span>
            </div>
          </div>
          <div className="workspace-signals">
            <div className="signal-chip">
              <span className="signal-rings"><i /></span>
              <span>{page.signal}</span>
            </div>
          </div>
        </div>
        <div className="workspace-divider" aria-hidden="true"><span /></div>
        <div className="workspace-stage">{children}</div>
      </main>

      <style dangerouslySetInnerHTML={{ __html: `
        .intelligence-shell { position: relative; min-height: 100vh; }
        .workspace-content { position: relative; padding: 1.35rem clamp(1.5rem, 3vw, 3rem) 3rem; }
        .workspace-content::before { content: ''; position: fixed; width: 480px; height: 480px; top: -190px; right: -180px; z-index: -1; border-radius: 50%; pointer-events: none; background: radial-gradient(circle, rgba(30, 64, 175, .13), transparent 67%); filter: blur(4px); }
        .workspace-topbar { display: flex; align-items: center; justify-content: space-between; max-width: 1300px; min-height: 58px; margin: 0 auto; }
        .workspace-context { display: grid; gap: .25rem; }
        .context-kicker { color: #6681a9; font-size: .6rem; font-weight: 750; letter-spacing: .15em; text-transform: uppercase; }
        .context-title-row { display: flex; align-items: center; gap: .52rem; color: #dce9fb; font-size: .83rem; font-weight: 610; letter-spacing: -.01em; }
        .context-node { width: 7px; height: 7px; display: inline-block; border: 1px solid #8cd4ff; border-radius: 50%; background: #2563eb; box-shadow: 0 0 0 3px rgba(59,130,246,.13), 0 0 12px rgba(56,189,248,.85); }
        .workspace-signals { display: flex; align-items: center; gap: .8rem; }
        .signal-chip { display: flex; align-items: center; gap: .47rem; padding: .42rem .65rem .42rem .48rem; border: 1px solid rgba(96, 165, 250, .14); border-radius: 999px; color: #90a9ca; background: rgba(14, 32, 62, .28); font-size: .62rem; font-weight: 650; letter-spacing: .025em; }
        .signal-rings { display: grid; width: 18px; height: 18px; place-items: center; border: 1px solid rgba(52,211,153,.28); border-radius: 50%; }
        .signal-rings i { width: 5px; height: 5px; display: block; border-radius: 50%; background: #34d399; box-shadow: 0 0 9px #34d399; animation: layout-signal 2.5s ease-in-out infinite; }
        .framework-chip { display: flex; overflow: hidden; border: 1px solid rgba(148,163,184,.12); border-radius: 7px; color: #8097b8; font-size: .55rem; font-weight: 750; letter-spacing: .11em; }
        .framework-chip span { padding: .43rem .52rem; }
        .framework-chip span + span { border-left: 1px solid rgba(148,163,184,.12); color: #536b8f; }
        .workspace-divider { position: relative; max-width: 1300px; height: 1px; margin: 0 auto 2.2rem; background: linear-gradient(90deg, rgba(96,165,250,.24), rgba(148,163,184,.1) 38%, transparent 80%); }
        .workspace-divider span { position: absolute; left: 0; top: -1px; width: 82px; height: 2px; background: linear-gradient(90deg, #38bdf8, #6366f1); box-shadow: 0 0 14px rgba(59,130,246,.65); }
        .workspace-stage { max-width: 1300px; margin: 0 auto; animation: workspace-enter .5s ease-out both; }
        .mobile-header { display: none; }
        @keyframes layout-signal { 50% { opacity: .45; transform: scale(.72); } }
        @keyframes workspace-enter { from { opacity: 0; transform: translateY(6px); } to { opacity: 1; transform: translateY(0); } }
        @media (max-width: 1024px) {
          .workspace-content { padding: calc(66px + 1.1rem) var(--space-lg) 2.25rem; }
          .workspace-topbar { min-height: 45px; }
          .mobile-header { position: fixed; inset: 0 0 auto; z-index: 1100; display: flex; align-items: center; justify-content: space-between; height: 66px; padding: 0 1.25rem; border-bottom: 1px solid rgba(148,163,184,.12); background: rgba(4, 11, 28, .8); backdrop-filter: blur(18px); -webkit-backdrop-filter: blur(18px); }
          .mobile-brand { display: flex; align-items: center; gap: .6rem; color: #f4f8ff; font-size: .95rem; font-weight: 720; letter-spacing: -.035em; }
          .mobile-brand > div { display: grid; gap: .04rem; }
          .mobile-brand small { color: #7189ac; font-size: .48rem; font-weight: 750; letter-spacing: .14em; }
          .mobile-mark { display: grid; width: 31px; height: 31px; place-items: center; border: 1px solid rgba(125,211,252,.4); border-radius: 10px; color: #e0f2fe; background: linear-gradient(135deg, #2563eb, #4f46e5); box-shadow: 0 6px 18px rgba(37,99,235,.3); }
          .mobile-mark svg { width: 19px; }
          .mobile-toggle { display: grid; width: 38px; height: 38px; place-content: center; gap: 4px; border: 1px solid rgba(148,163,184,.16); border-radius: 10px; color: #c7ddf8; background: rgba(15, 31, 60, .55); cursor: pointer; }
          .mobile-toggle span { display: block; width: 15px; height: 1.5px; border-radius: 2px; background: currentColor; transition: transform .2s ease, opacity .2s ease; }
          .mobile-toggle[aria-expanded="true"] span:nth-child(1) { transform: translateY(5.5px) rotate(45deg); }
          .mobile-toggle[aria-expanded="true"] span:nth-child(2) { opacity: 0; }
          .mobile-toggle[aria-expanded="true"] span:nth-child(3) { transform: translateY(-5.5px) rotate(-45deg); }
          .sidebar-wrapper { position: fixed; inset: 0; z-index: 1200; visibility: hidden; pointer-events: none; transition: visibility .25s ease; }
          .sidebar-wrapper.mobile-open { visibility: visible; pointer-events: auto; }
          .sidebar-overlay { position: absolute; inset: 0; width: 100%; border: 0; background: rgba(0, 5, 18, .68); backdrop-filter: blur(5px); opacity: 0; transition: opacity .25s ease; cursor: pointer; }
          .sidebar-wrapper.mobile-open .sidebar-overlay { opacity: 1; }
          .sidebar-wrapper .sidebar { transform: translateX(-105%); transition: transform .32s cubic-bezier(.2,.8,.2,1); }
          .sidebar-wrapper.mobile-open .sidebar { transform: translateX(0); }
        }
        @media (max-width: 640px) {
          .workspace-content { padding: calc(66px + .9rem) 1rem 2rem; }
          .workspace-signals { gap: .4rem; }
          .signal-chip { padding: .38rem; }
          .signal-chip > span:last-child { display: none; }
          .framework-chip { display: none; }
          .workspace-divider { margin-bottom: 1.45rem; }
        }
        @media (prefers-reduced-motion: reduce) { .workspace-stage, .signal-rings i { animation: none !important; } }
      ` }} />
    </div>
  );
};

export default MainLayout;
