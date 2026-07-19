import React from 'react';
import { NavLink } from 'react-router-dom';

const Sidebar = () => {
  const navItems = [
    {
      name: 'Overview',
      path: '/',
      icon: <><path d="M3.5 10.5 12 3l8.5 7.5v9a1.5 1.5 0 0 1-1.5 1.5H5a1.5 1.5 0 0 1-1.5-1.5v-9Z" /><path d="M9 21v-6h6v6" /></>,
    },
    {
      name: 'Ask RegMind',
      path: '/ask-ai',
      icon: <><path d="M20.5 11.5a7.8 7.8 0 0 1-8 7.5 9.5 9.5 0 0 1-3.3-.6L4 20l1.5-4a7.3 7.3 0 0 1-1-3.7 7.8 7.8 0 0 1 8-7.5 7.8 7.8 0 0 1 8 6.7Z" /><path d="M9 12h.01M12.5 12h.01M16 12h.01" strokeWidth="3" strokeLinecap="round" /></>,
    },
    {
      name: 'Conflict Scan',
      path: '/conflict-detection',
      icon: <><path d="M12 21s7.5-3.8 7.5-9.5V5.3L12 2.5 4.5 5.3v6.2C4.5 17.2 12 21 12 21Z" /><path d="M12 8v4M12 16h.01" strokeLinecap="round" /></>,
    },
  ];

  return (
    <aside className="sidebar" aria-label="Primary navigation">
      <div className="sidebar-ambient" aria-hidden="true" />

      <div className="sidebar-header">
        <div className="brand-mark" aria-hidden="true">
          <span className="brand-orbit brand-orbit-one" />
          <span className="brand-orbit brand-orbit-two" />
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2.1">
            <path d="m12 2.8 7.7 4.1L12 11 4.3 6.9 12 2.8Z" />
            <path d="m4.3 11.5 7.7 4.1 7.7-4.1M4.3 16.1l7.7 4.1 7.7-4.1" />
          </svg>
        </div>
        <div className="brand-copy">
          <span className="brand-name">RegMind</span>
          <span className="brand-subtitle">REGULATORY INTELLIGENCE</span>
        </div>
      </div>

      <div className="workspace-pill">
        <span className="workspace-pulse" />
        <span>LIVE WORKSPACE</span>
        <span className="workspace-key">01</span>
      </div>

      <nav className="nav-menu">
        <p className="nav-caption">Command center</p>
        {navItems.map((item, index) => (
          <NavLink
            key={item.path}
            to={item.path}
            end={item.path === '/'}
            className={({ isActive }) => `nav-item ${isActive ? 'active' : ''}`}
          >
            <span className="nav-index">0{index + 1}</span>
            <span className="nav-icon"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="1.8">{item.icon}</svg></span>
            <span className="nav-label">{item.name}</span>
            <span className="nav-arrow" aria-hidden="true">↗</span>
          </NavLink>
        ))}
      </nav>

      <div className="sidebar-footer">
        <div className="footer-scanline" aria-hidden="true" />
        <div className="system-status">
          <span className="status-beacon"><span /></span>
          <div>
            <span className="status-label">System status</span>
            <strong>All systems operational</strong>
          </div>
        </div>
        <div className="footer-meta"><span>SECURE SESSION</span><span>•</span><span>v1.0</span></div>
      </div>

      <style dangerouslySetInnerHTML={{ __html: `
        .sidebar {
          --sidebar-surface: rgba(5, 12, 31, .93);
          width: 280px;
          height: 100dvh;
          position: fixed;
          inset: 0 auto 0 0;
          display: flex;
          flex-direction: column;
          padding: 1.55rem 1.15rem 1.2rem;
          z-index: 1000;
          overflow: hidden;
          color: var(--text-primary);
          background: linear-gradient(160deg, rgba(11, 22, 49, .97) 0%, var(--sidebar-surface) 43%, rgba(3, 8, 24, .98) 100%);
          border-right: 1px solid rgba(148, 163, 184, .13);
          box-shadow: 20px 0 55px rgba(0, 0, 0, .2);
          isolation: isolate;
        }
        .sidebar::after { content: ''; position: absolute; inset: 0 0 0 auto; width: 1px; background: linear-gradient(transparent, rgba(96, 165, 250, .6), transparent); opacity: .65; }
        .sidebar-ambient { position: absolute; width: 230px; height: 230px; right: -90px; top: -60px; z-index: -1; background: radial-gradient(circle, rgba(59, 130, 246, .24), transparent 67%); filter: blur(8px); pointer-events: none; }
        .sidebar-header { display: flex; align-items: center; gap: .78rem; padding: .32rem .48rem 1.45rem; }
        .brand-mark { width: 43px; height: 43px; position: relative; display: grid; place-items: center; overflow: hidden; border: 1px solid rgba(147, 197, 253, .4); border-radius: 14px; color: #dbeafe; background: linear-gradient(140deg, rgba(59, 130, 246, .86), rgba(99, 102, 241, .55)); box-shadow: 0 10px 26px rgba(37, 99, 235, .34), inset 0 1px rgba(255,255,255,.25); }
        .brand-mark svg { width: 25px; position: relative; z-index: 1; }
        .brand-orbit { position: absolute; display: block; border: 1px solid rgba(255,255,255,.22); border-radius: 50%; }
        .brand-orbit-one { width: 61px; height: 27px; transform: rotate(-34deg); }
        .brand-orbit-two { width: 51px; height: 22px; transform: rotate(41deg); opacity: .6; }
        .brand-copy { display: grid; gap: .14rem; min-width: 0; }
        .brand-name { font-size: 1.15rem; font-weight: 750; line-height: 1; letter-spacing: -.055em; color: #f8fbff; }
        .brand-subtitle, .nav-caption, .workspace-pill, .footer-meta, .status-label { font-size: .59rem; font-weight: 700; letter-spacing: .13em; text-transform: uppercase; }
        .brand-subtitle { color: #7f97bd; white-space: nowrap; }
        .workspace-pill { display: flex; align-items: center; gap: .48rem; margin: 0 .27rem 1.7rem; padding: .56rem .7rem; border: 1px solid rgba(96, 165, 250, .14); border-radius: 9px; color: #8ea8ce; background: rgba(15, 34, 68, .34); }
        .workspace-pulse { width: 6px; height: 6px; border-radius: 50%; background: #34d399; box-shadow: 0 0 0 3px rgba(52,211,153,.1), 0 0 14px #34d399; }
        .workspace-key { margin-left: auto; color: #5f769a; }
        .nav-menu { display: flex; flex: 1; flex-direction: column; gap: .34rem; }
        .nav-caption { margin: 0 0 .54rem .82rem; color: #60769a; }
        .nav-item { position: relative; display: flex; align-items: center; min-height: 52px; gap: .75rem; padding: .58rem .7rem; overflow: hidden; border: 1px solid transparent; border-radius: 12px; color: #9aacc7; text-decoration: none; transition: color .23s ease, background .23s ease, border-color .23s ease, transform .23s ease; }
        .nav-item::before { content: ''; position: absolute; top: 15%; bottom: 15%; left: -1px; width: 2px; border-radius: 99px; background: #7dd3fc; box-shadow: 0 0 12px #38bdf8; opacity: 0; transform: scaleY(.35); transition: opacity .23s ease, transform .23s ease; }
        .nav-index { width: 17px; color: #4d6284; font-size: .57rem; font-weight: 700; letter-spacing: .03em; transition: color .23s ease; }
        .nav-icon { display: grid; width: 30px; height: 30px; place-items: center; flex: 0 0 auto; border: 1px solid rgba(148,163,184,.11); border-radius: 9px; color: #a7b8d2; background: rgba(148,163,184,.055); transition: color .23s ease, background .23s ease, border-color .23s ease, transform .23s ease; }
        .nav-icon svg { width: 17px; height: 17px; }
        .nav-label { font-size: .88rem; font-weight: 580; letter-spacing: -.01em; }
        .nav-arrow { margin-left: auto; color: #7690b8; font-size: .86rem; opacity: 0; transform: translate(-5px, 5px); transition: opacity .23s ease, transform .23s ease; }
        .nav-item:hover { color: #e8f2ff; background: rgba(75, 114, 172, .1); border-color: rgba(148,163,184,.08); transform: translateX(3px); }
        .nav-item:hover .nav-icon { color: #dbeafe; border-color: rgba(125,211,252,.26); background: rgba(59,130,246,.14); transform: scale(1.05); }
        .nav-item:hover .nav-arrow { opacity: .9; transform: translate(0); }
        .nav-item.active { color: #f5f9ff; border-color: rgba(96,165,250,.2); background: linear-gradient(100deg, rgba(59,130,246,.2), rgba(79,70,229,.11) 78%, transparent); box-shadow: inset 0 1px rgba(255,255,255,.035), 0 6px 20px rgba(2,8,23,.2); }
        .nav-item.active::before { opacity: 1; transform: scaleY(1); }
        .nav-item.active .nav-index { color: #8dc7ff; }
        .nav-item.active .nav-icon { color: #e9f6ff; border-color: rgba(125,211,252,.4); background: linear-gradient(135deg, rgba(14,165,233,.32), rgba(99,102,241,.27)); box-shadow: 0 0 18px rgba(59,130,246,.18); }
        .nav-item.active .nav-arrow { color: #b8e5ff; opacity: 1; transform: translate(0); }
        .sidebar-footer { position: relative; margin: auto .27rem 0; padding: 1.1rem .45rem .18rem; border-top: 1px solid rgba(148,163,184,.12); }
        .footer-scanline { position: absolute; top: -1px; left: 0; width: 52px; height: 1px; background: #60a5fa; box-shadow: 0 0 10px #3b82f6; }
        .system-status { display: flex; align-items: center; gap: .65rem; }
        .status-beacon { display: grid; width: 27px; height: 27px; place-items: center; border: 1px solid rgba(52,211,153,.2); border-radius: 50%; background: rgba(16,185,129,.07); }
        .status-beacon span { width: 7px; height: 7px; border-radius: 50%; background: #34d399; box-shadow: 0 0 10px #34d399; animation: sidebar-pulse 2.4s infinite; }
        .status-label { display: block; margin-bottom: .09rem; color: #60769a; font-size: .55rem; }
        .system-status strong { display: block; color: #b9c8dc; font-size: .7rem; font-weight: 570; }
        .footer-meta { display: flex; gap: .38rem; margin: .82rem 0 0 2.25rem; color: #506786; font-size: .51rem; }
        @keyframes sidebar-pulse { 50% { transform: scale(.72); opacity: .5; } }
        @media (max-width: 1024px) { .sidebar { width: 280px; } }
        @media (prefers-reduced-motion: reduce) { .sidebar *, .sidebar *::before { transition: none !important; animation: none !important; } }
      ` }} />
    </aside>
  );
};

export default Sidebar;
